import argparse
import time
import io
from contextlib import redirect_stdout
import os
import spacy, en_core_web_sm
import nltk
from nltk.corpus import stopwords
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.stem import WordNetLemmatizer
import scispacy
import spacy
from spacy import displacy
from scispacy.abbreviation import AbbreviationDetector
from scispacy.umls_linking import UmlsEntityLinker
from PyDictionary import PyDictionary


# download corpuses

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download("vader_lexicon")
#nltk.download('stopwords')


# load tools 

#stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
nlp = spacy.load('en_core_web_sm')
dictionary = PyDictionary()



# ************************************ PROCESSING FUNCTIONS ***************************************** #

def has_important_words(sentence, nontrivial_parts_of_speech):
	tokens = nlp(line)
	for token in tokens:
		if token.pos_ in nontrivial_parts_of_speech:
			return token.text
	return False


def lemmatize_word(word):
	lemmatized = lemmatizer.lemmatize(word)
	# lemmatizer.lemmatize("better", pos ="a")) # adjective synonym search, resulting in 'good'
	#lemmatized = lemmatized.replace('\t', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')
	lemmatized_without_letters = [c for c in lemmatized.lower() if c not in 'abcdefghijklmnopqrstuvwxyz']
	if len(lemmatized_without_letters) < len(lemmatized):
		return lemmatized
	return 'xxxxxx' # not likely to be found in entities where this function is used

# *************************************************************************************************** #




# ************************************ SIMILARITY FUNCTIONS ***************************************** #

''' - to do: optimize these
def check_sentiment(sentence):
	positive = ['increase', 'upregulate', 'enable', 'intensif']
	neutral = ['modulate', 'change']
	negative = ['decrease', 'reduce', 'downregulate', 'disrupt', 'inhibit', 'prevents', 'limits']
	analyzer = SentimentIntensityAnalyzer()
	sentiment = analyzer.polarity_scores(sentence)
	if sentiment['compound'] > 0.5:
		return 'positive'
	elif sentiment['compound'] < -0.5:
		return 'negative'
	return 'neutral'

def check_similarity(string1, string2):
	similarity_nlp = spacy_universal_sentence_encoder.load_model('en_use_lg')
	string1_nlp = similarity_nlp(string1)
	string2_nlp = similarity_nlp(string2)
	similarity = string1_nlp.similarity(string2_nlp)
	if similarity > 0.9:
		return 'similar'
	return 'different'
'''

def find_similar_words_using_custom_abstract_corpus(corpus_dir, abstracts, treatments_to_compare, nontrivial_parts_of_speech):
	# to do: add option to use other possible_treatments instead of treatments_to_compare
	# identify similar words by context (such as identifying 'voraconazole' from 'fluconazole') using custom corpus of abstracts
	new_corpus = PlaintextCorpusReader(corpus_dir, r'.*\.txt')
	#print('new corpus words', new_corpus.words())
	all_text = nltk.Text(new_corpus.words())
	# find substances with similar contexts (used in similar ways in the sentence) as 'eugenol', a known treatment
	all_similar_alt_treatments = []
	not_used_alt_treatments = set()
	for known_treatment in known_treatments:
		f = io.StringIO()
		with redirect_stdout(f):
			all_text.similar(known_treatment)
		out = f.getvalue()			
		if out is not None:
			alt_treatments = set()
			for sentence in out.split('\n'):
				for item in sentence.split(' '):
					tokens = nlp(item)
					for token in tokens:
						# exclude adjectives like 'complete', 'clinical', 'major', etc and adverbs like 'only'
						if token.pos_ not in nontrivial_parts_of_speech and token.pos_ not in ['ADJ', 'ADV']:
							lemmatized_alt_treatment = lemmatize_word(token.text)
							if lemmatized_alt_treatment not in ''.join(terms_to_exclude) and lemmatized_alt_treatment not in ''.join(known_treatments):
								#alt_treatments.add(token.text.replace('\t', ' ').replace('  ', ' ').replace('  ', ' '))
								alt_treatments.add(token.text)
							else:
								if token.text not in [None, 'None']:
									not_used_alt_treatments.add(token.text)
						else:
							not_used_alt_treatments.add(token.text)
			if len(alt_treatments) > 0:
				print('known_treatment', known_treatment, 'alt_treatments', alt_treatments)
				similar_alt_treatments = set()
				for item in alt_treatments:
					if item is not None:
						medical_term = check_if_medical_term_using_dictionary(item)
						if medical_term:
							similar_alt_treatments.add(medical_term)
						else:
							not_used_alt_treatments.add('not a medical term: ' + item)
				all_similar_alt_treatments.append(known_treatment + ' ~ ' + ','.join([item for item in similar_alt_treatments]))
	print('not_used_alt_treatments', not_used_alt_treatments)
	return all_similar_alt_treatments

# *************************************************************************************************** #




# ********************************************* GET DATA ********************************************* # 

def check_if_medical_term_using_dictionary(phrase):
	for word in phrase.split(' '):
		if word not in already_looked_up:
			for medical_term in medical_terms_to_check:
				if medical_term in word:
					return word
			already_looked_up.add(word)
			just_nonletters = ''.join([c for c in word.lower() if c not in 'abcdefghijklmnopqrstuvwxyz'])
			if len(just_nonletters) < len(word): # this isnt just numbers/punctuation, it has letters
				# assume its a medical term if there is a '. ' indicating an abbreviated species and there are no numbers in it
				if '.' in word and len([c for c in word if c in '0123456789']) == 0:
					return word 
				try:
					results = dictionary.meaning(word, disable_errors=True)
					if results and results is not None:
						for part_of_speech, definitions in results.items():
							#print('result', phrase, definitions)
							if part_of_speech == 'NOUN':
								if len(definitions) > 0:
									all_definitions = ','.join(definitions)
									for medical_term in medical_terms_to_check:
										if medical_term in all_definitions:
											return True
					else:
						no_dictionary_term_found.add(word)
				except Exception as e:
					print('dictionary exception', word, e)
	return False

def check_if_medical_term_using_wiki(word):
	# to do: add check for similar articles by using synonym search from custom corpus
	# also add check for more common word from lemmatizer for disambiguation
	# results = wikipedia.search(word) # search doesnt disambiguate
	try:
		if word not in already_looked_up:
			already_looked_up.add(word)
			for medical_term in medical_terms_to_check:
				if medical_term in word:
					return word
			just_nonletters = ''.join([c for c in word.lower() if c not in 'abcdefghijklmnopqrstuvwxyz'])
			if len(just_nonletters) < len(word): # this isnt just numbers/punctuation, it has letters
				# assume its a medical term if there is a '. ' indicating an abbreviated species and there are no numbers in it
				if '.' in word and len([c for c in word if c in '0123456789']) == 0:
					return word
				summary = wikipedia.summary(word)
				all_categories = ','.join(wikipedia.page(word).categories)
				print('categories', word, all_categories)	
				if len([item for item in medical_terms_to_check if item in all_categories or item in summary]) > 0:
					return word
				else:
					no_dictionary_term_found.add(word)
	except wikipedia.DisambiguationError as e:
		print('e options', e.options)
		for suggestion in e.options:
			suggested_term_found = check_if_medical_term_using_wiki(suggestion)
			print('suggested_term_found', suggested_term_found, suggestion)
			if suggested_term_found:
				return suggested_term_found			
	return False

def get_abstracts_from_pubmed_api(search_text, result_limit, email):
	pubmed = PubMed(tool="Finding possible treatments for a condition", email=email)
	results = pubmed.query(search_text, max_results=result_limit)
	abstracts = [result.abstract for result in results]
	keywords = [result.keywords for result in results]
	abstracts = [[' '.join(abstract[0].strip().replace('\t', ' ').replace('      ', ' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ').lower().split('\n'))] for abstract in abstracts] # dont add a blank line for the corpus reader
	return abstracts, keywords

def get_abstracts_from_pubmed_download(saved_pubmed_download):
	found_abstract = False
	abstracts = []
	keywords = set()
	with open(saved_pubmed_download, 'r') as f:
		for line in f.readlines():
			if 'OT  - ' in line:
				line = line.replace('OT  - ', '')
				for word in condition.split(' '):
					if word not in line:
						if len([item for item in terms_to_exclude if item in line]) == 0:
							keywords.add(line.strip())
			elif 'AB  - ' in line:
				abstract = [line.replace('AB  - ', '').strip()]
				found_abstract = True
			elif found_abstract:
				if ' - ' in line[0:8]:
					abstracts.append('\n'.join(abstract))
					found_abstract = False
					abstract = []
				else:
					abstract.append(line)
	abstracts = [[' '.join(abstract.lower().replace('      ', ' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ').split('\n'))] for abstract in abstracts if abstract != []] # dont add a blank line for the corpus reader
	return abstracts, keywords

# **************************************************************************************************** # 




# **************************************** GET ENTITIES ********************************************** #

def extract_entities_from_abstract_and_keywords(abstracts, keywords):
	# to do: check if word is similar to a word already used, such as 'c neoformans' and 'cryptococcus neoformans'
	lemmatized_entities = set()
	possible_treatments = set()
	not_possible_treatments = {'not_medical_term': set(), 'already_lemmatized': set(), 'not_noun_or_verb': set()}
	for abstract in abstracts:
		# filter abstract using scispacy entity detector, to create the most filtered list using entity recognition
		tokens = nlp(abstract[0].lower().strip()) # sentences = list(doc.sents)
		for entity in tokens.ents:
			lemmatized_entities, possible_treatments, not_possible_treatments = identify_useful_entities(entity.text, lemmatized_entities, possible_treatments, not_possible_treatments)
	for keyword in keywords:
		lemmatized_entities, possible_treatments, not_possible_treatments = identify_useful_entities(keyword, lemmatized_entities, possible_treatments, not_possible_treatments)
	print('possible_treatments', possible_treatments)
	print('not_possible_treatments', not_possible_treatments)
	return possible_treatments, not_possible_treatments

def identify_useful_entities(entity_or_keyword, lemmatized_entities, possible_treatments, not_possible_treatments):
	#entity_text = entity_or_keyword.replace('\t', ' ').replace('      ', ' ').replace('    ', ' ').replace('  ', ' ').strip()
	entity_text = entity_or_keyword
	just_nonletters = ''.join([c for c in entity_text.lower() if c not in 'abcdefghijklmnopqrstuvwxyz'])
	if len(just_nonletters) < len(entity_text): # this isnt just numbers/punctuation, it has letters
		# make sure its a noun (verbs can be nouns in the spacy lib)
		for token in nlp(entity_text):
			if token.pos_ in ['NOUN', 'PROPN', 'VERB']: # spacy tags some nouns as verbs
				lemmatized_entity = lemmatize_word(entity_text)
				if len(lemmatized_entity) > 4:
					if lemmatized_entity not in lemmatized_entities:
						# this is a new word, so add it to entities
						lemmatized_entities.add(lemmatized_entity)
						# make sure it doesnt have any terms_to_exclude
						if len([term for term in terms_to_exclude if lemmatize_word(term) in token.text]) == 0:
							# make sure its a medical term
							medical_term = check_if_medical_term_using_dictionary(entity_text)
							if medical_term:
								possible_treatments.add(entity_text)
							else:
								not_possible_treatments['not_medical_term'].add(entity_text)
					else:
						not_possible_treatments['already_lemmatized'].add(entity_text)
				else:
					possible_treatments.add(entity_text) # add it in case its an acronym rather than a root word, 'upr' of 'upregulation' could be an acronym
			else:
				not_possible_treatments['not_noun_or_verb'].add(entity_text)
	return lemmatized_entities, possible_treatments, not_possible_treatments

# **************************************************************************************************** #




# ************************************ VARIABLES ***************************************** #

# example: python3 parse_pubmed_download.py -c 'fungal treatment' -k 'sitosterol, fluconazole, choline, eugenol' -t 'biology'
parser = argparse.ArgumentParser(prog='Find Possible Treatments', description='Parses Pubmed data for possible treatments')
parser.add_argument('-c', '--condition', required=True, help="(Required) Enter the search term used to create the Pubmed search, such as 'fungal treatment'")
parser.add_argument('-k', '--known_treatments', required=False, help="(Optional) Enter the known treatments to check for similar alternatives, such as 'fluconazole, sitosterol'")
parser.add_argument('-t', '--terms_to_exclude', required=False, help="(Optional) Enter the terms to exclude if found in possible treatments, like 'biology'")
args = parser.parse_args()
print('\ncondition:', args.condition, 'known_treatments:', args.known_treatments, 'terms_to_exclude:', args.terms_to_exclude)
condition = args.condition
known_treatments = [item.strip() for item in args.known_treatments.split(',')] if args.known_treatments.strip() != '' else []
terms_to_exclude = condition.split(' ') if condition is not None and condition != '' else [item.strip() for item in args.terms_to_exclude] if args.terms_to_exclude.strip() != '' else []

# **************************************************************************************** #



script_start_time = time.time()

already_looked_up = set() # track words that have already been looked up
no_dictionary_term_found = set()
# to do: get common categories from wiki of terms in pubmed articles
# to do: also check for 'letter-number' mixes as those are likely to be medical terms
medical_terms_to_check = [
	'pathogen', 'microb', 'chemical', 'compound', 'medic', 'substance', 'some', 'sis', 'sus', 'oid', 'ose', 'ceph', 'aly', 'leu', 'ate', 'delt', 'yl', 'ster', 'amphi', 
	'meth', 'oxy', 'kary', 'cere', 'sia', 'eri', 'sept', 'ima', 'ora', 'benz', 'ase', 'ii', 'il', 'rin', 'amin', 'tion', 'ae', 'ius', 'cus', 'ia', 'mab', 'ica', 'lic', 
	'lis', 'ila', 'lin', 'lus', 'ean', 'cyt', 'arth', 'derm', 'trich', 'staph', 'ete', 'iso', 'ana', 'spor', 'gen', 'zym', 'san', 'era', 'rus', 'tum', 'eum', 'osa', 
	'geno', 'pheno', 'tis', 'ans', 'zol', 'nis', 'cia', 'alde', 'cin', 'sin', 'iva', 'ola', 'sil', 'ane', 'vin', 'ese', 'phy', 'gin', 'mis', 'iol', 'one', 'chol', 'ion',
	'ens', 'occ', 'glu', 'tol', 'nol', 'rol', 'element', 'vor', 'zol', 'cin', 'prot', 'bet', 'alph', 'ium', 'ella', 'ala', 'dia', 'itis', 'myc', 'disease', 'bio', 'dend',
	'treatment', 'health', 'therap', 'bac', 'fung', 'vir', 'escher','ryp', 'fol', 'anth', 'aqu', 'tissue', 'lymph', 'trans', 'globul', 'trid', 'chy', 'aden', 'xyl', 'thy', 
	'gamma', 'morph', 'syl', 'terp', 'oma', 'pyr', 'epi', 'phe', 'ris', 'glyc', 'ite', 'ize', 'flav', 'plat', 'aca', 'guan', 'xan', 'cyn', 'ima', 'ida', 'sys', 'ken', 
	'organism', 'organ', 'plas', 'immun', 'vitam', 'nutrient', 'inflamm', 'ein', 'tin', 'ide', 'ine', 'methyl', 'lysis', 'acetyl', 'oxid', 'mechanism', 'strain', 'avi', 
	'species', 'gene', 'cell', 'prot', 'enzyme', 'acid', 'base', 'non', 'mono', 'bi', 'tri', 'quat', 'pent', 'dna', 'rna', 'prop', 'eryth', 'euk', 'proto', 'eus', 'sum', 
	'sugar', 'alcohol', 'energy', 'metab', 'carbo', 'hydr', 'lipid', 'anti', 'anti', 'ria', 'fluro', 'chia', 'acti', 'eal', 'din', 'pha', 'poly', 'mer', 'chlo', 
	'um', 'oxi', 'kin', 'mico', 'aly', 'spl', 'rsi', 'nic', 'mos', 'neut', 'tox', 'oxo', 'idi', 'oe', 'mic', 'eu',
]
trivial_parts_of_speech = ['AUX', 'DET', 'ADP', 'PART', 'PUNCT', 'CCONJ', 'PRON'] 
# AUX = is, DET = the, ADP = of, PART = to, CCONJ = both, ADJ = clinical, only, major, new, PRON = the, which 
nontrivial_parts_of_speech = ['PROPN', 'NOUN', 'VERB', 'ADV', 'ADJ'] 
# PROPN = 'Citicoline', NOUN = CDP, choline, VERB = phosphatidylcholine, interacting, increase, is, ADV = especially, ADJ = generic, endogenous, able, central, nervous, cellular, especially

# create filename from variables and create directories
filename = ''.join([c for c in condition.lower() if c in 'abcdefghijklmnopqrstuvwxyz'])[0:10]
saved_pubmed_download = f"pubmed-{filename}-set.txt"
print('\nusing file', saved_pubmed_download)
output_dir = f"{filename}_output"
corpus_dir = os.getcwd() + f"/{filename}_corpus"
for new_dir in [output_dir, corpus_dir]:
	if not os.path.exists(new_dir):
		os.mkdir(new_dir)

# to do: consolidate keywords and possible_treatments as possible_treatments and add a check of wikipedia to identify pathogens, compounds, processes
print('\nformatting & storing abstract and keyword lists, to identify possible treatments in keywords')
# format abstracts/keywords as a list from the downloaded pubmed file or the pubmed api
#abstracts, keywords = get_abstracts_from_pubmed_api(condition, 500, 'jonijezewski@outlook.com')
abstracts, keywords = get_abstracts_from_pubmed_download(saved_pubmed_download)
open(f"{output_dir}/keywords_{filename}.txt", 'w').write('\n'.join([item for item in keywords]))
open(f"{corpus_dir}/abstracts_{filename}.txt", 'w').write('\n'.join([abstract[0] for abstract in abstracts]))

print('\nextracting medical entities from abstracts to identify possible treatments')
# get entities (included and excluded from treatment list based on terms_to_exclude) and abstracts
possible_treatments, not_possible_treatments = extract_entities_from_abstract_and_keywords(abstracts, keywords)
# add not_possible_treatments['not_medical_term'] to possible_treatments as terms not in dictionary are often medical terms
possible_treatments.update([item for item in not_possible_treatments['not_medical_term']])
open(f"{output_dir}/not_possible_treatments_{filename}.txt", 'w').write('\n'.join([item for item in not_possible_treatments]))
open(f"{output_dir}/possible_treatments_{filename}.txt", 'w').write('\n'.join([item for item in possible_treatments]))

# find similar treatments based on similar sentence structure and word usages
treatments_to_compare = known_treatments if len(known_treatments) > 0 else possible_treatments
treatments_to_compare_name = 'known_treatments' if len(known_treatments) > 0 else 'possible_treatments'
print('\nfinding similar treatments based on sentence structure and word usage, using', treatments_to_compare_name)
all_similar_alt_treatments = find_similar_words_using_custom_abstract_corpus(corpus_dir, abstracts, treatments_to_compare, nontrivial_parts_of_speech)
# to do: include no_dictionary_term_found which are often medical terms
print('\nno_dictionary_term_found', no_dictionary_term_found)
open(f"{output_dir}/similar_treatments_to_{treatments_to_compare_name}_{filename}.txt", 'w').write('\n'.join(all_similar_alt_treatments))

print('\nscript time', str((time.time() - script_start_time)/ 7) + ' minutes')

'''
- identifying the 'adjacent sequences of structures', 'size/separators of common substructures (like vowel ratios/positions)', 'position of common sub-structures' and 'common equivalent alternates of substructures', 
	and 'the common adjacent sequences of substructures' and 'common equivalent variants of substructures and substructure sequences'
	seems to be the highest-value set of variables in determining similarity of words with the fewest variables, 
- similarly, identifying 'uncommon sequences', 'substructures/structures that change/dont change the meaning of the structure/structure sequence', 
	'structures that are dissimilar in substructure but similar in meaning (and the opposite)' are similarly useful to identify
- similarly, identifying 'nonadjacent relevance structures like a prefacing clause indicating truthhood of the following clause' 
	(clause sequence -> truthhood of adjacent clauses -> 'meaning change' of structure, 
	so the first clause is relevant to identifying the meaning and therefore similarity of the word, 
	as the meaning of a word here is 'its interaction with other structures'),
	and identifying 'differences from this structure, given its importance to identify' (adjacent changes of truthhood) are similarly a useful variable set.
- these are 'similarly high variation variable sets that offer complementary info, as opposed to redundant info'

bc 'common', 'equivalent alternate', 'subset', 'position', 'sequence', 'adjacent' seem to be enough to cover more relevance in language, 
although there are relevant terms without these attributes, they just require more work and may not always have a reason why the work is justified, so are less common
alternate structure (synonyms)
adjacent structure (implication)
opposing structures (non/anti)
sub-structures
	cross-sub-structure (sub-structure sequences, what does it connect/interact/change with)
	alternate sub-structure ('equivalent alternates', what else can it be replaced with)
	common/rare sub-structures ('what are its useful values within a complex variable like interface variables', what is its sub-value type of the 'probability' variable)
	position of sub-structure (what position does it occupy in sequences)
	changes in sub-structures (like ine/ane/ate indicating a variety, as in what are its variants)
	potential of sub-structures (what else does it interact with, what else can it become/change, what is it almost/never or what does it lead to adjacently, what cant it become, as in what interactions are prevented by its other structures)
    required sub-structures (what does it require, like a sequence or position)
inter-structure (across terms, such as term sequence)
'''