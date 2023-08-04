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
	lemmatized = lemmatized.replace('  ', ' ').replace('\t', ' ')
	lemmatized_without_letters = [c for c in lemmatized if c not in 'abcdefghijklmnopqrstuvwxyz']
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

def find_similar_words_using_custom_abstract_corpus(corpus_dir, abstracts, known_treatments, nontrivial_parts_of_speech):
	# identify similar words by context (such as identifying 'voraconazole' from 'fluconazole') using custom corpus of abstracts
	new_corpus = PlaintextCorpusReader(corpus_dir, r'.*\.txt')
	#print('new corpus words', new_corpus.words())
	all_text = nltk.Text(new_corpus.words())
	# find substances with similar contexts (used in similar ways in the sentence) as 'eugenol', a known treatment
	all_similar_treatments = []
	for known_treatment in known_treatments:
		f = io.StringIO()
		with redirect_stdout(f):
			similar_treatments = all_text.similar(known_treatment)
		out = f.getvalue()
		if similar_treatments:
			print('similar_treatments', similar_treatments) #.text
		if out is not None:
			alt_treatments = set()
			for sentence in out.split('\n'):
				for item in sentence.split(' '):
					tokens = nlp(item)
					for token in tokens:
						print('alt treatment token part of speech', token.pos_, token.text)
						if token.pos_ in nontrivial_parts_of_speech and token.pos_ not in ['ADJ', 'ADV']: # exclude adjectives like 'complete', 'clinical', 'major', etc and adverbs like 'only'
							lemmatized_alt_treatment = lemmatize_word(token.text)
							print('lemmatized_alt_treatment', lemmatized_alt_treatment)
							if lemmatized_alt_treatment not in ''.join(terms_to_exclude) and lemmatized_alt_treatment not in ''.join(known_treatments):
								alt_treatments.add(token.text)
			if len(alt_treatments) > 0:
				print('known_treatment', known_treatment, 'alt_treatments', alt_treatments)
				all_similar_treatments.append(known_treatment + ' ~ ' + ','.join([item for item in alt_treatments]))
	return all_similar_treatments

# *************************************************************************************************** #




# ********************************************* GET DATA ********************************************* # 

def get_right_term_for_wiki(word):
	# to do: add check for similar articles by using synonym search from custom corpus
	# also add check for more common word from lemmatizer for disambiguation
	medical_terms_to_check = ['pathogen', 'microb', 'chemical', 'compound', 'medic', 'disease', 'bio', 'treatment', 'health', 'therap']
	# results = wikipedia.search(word) # search doesnt disambiguate
	try:
		summary = wikipedia.summary(word)
		all_categories = ','.join(wikipedia.page(word).categories)
		print('categories', word, all_categories)	
		if len([item for item in medical_terms_to_check if item in all_categories or summary]) > 0:
			return word
	except wikipedia.DisambiguationError as e:
		print('e options', e.options)
		for suggestion in e.options:
			suggested_term_found = get_right_term_for_wiki(suggestion)
			print('suggested_term_found', suggested_term_found, suggestion)
			if suggested_term_found:
				return suggested_term_found			
	return False

def get_abstracts_from_pubmed_api(search_text, result_limit, email):
	pubmed = PubMed(tool="Finding possible treatments for a condition", email=email)
	results = pubmed.query(search_text, max_results=result_limit)
	abstracts = [result.abstract for result in results]
	keywords = [result.keywords for result in results]
	abstracts = [[' '.join(abstract[0].lower().split('\n')), ''] for abstract in abstracts] # add a blank line for the corpus reader
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
	abstracts = [[' '.join(abstract.lower().split('\n')), ''] for abstract in abstracts if abstract != []] # add a blank line for the corpus reader
	return abstracts, keywords

# **************************************************************************************************** # 




# **************************************** GET ENTITIES ********************************************** #

def extract_entities_from_abstract(abstracts):
	lemmatized_entities = set()
	used_entities = set()
	unused_entities = set()
	for abstract in abstracts:
		# filter abstract using scispacy entity detector, to create the most filtered list using entity recognition
		if abstract != []:
			doc = nlp(abstract[0].lower().strip()) # sentences = list(doc.sents)
			for entity in doc.ents:
				entity_text = entity.text.replace('  ', ' ').replace('\t', ' ')
				just_nonletters = ''.join([c for c in entity_text if c not in 'abcdefghijklmnopqrstuvwxyz'])
				if len(just_nonletters) < len(entity_text): # this isnt just numbers/punctuation, it has letters
					# make sure its a noun (verbs can be nouns in the spacy lib)
					lemmatized_entity = lemmatize_word(entity_text)
					if lemmatized_entity not in lemmatized_entities:
						# this is a new word, so add it to entities
						lemmatized_entities.add(lemmatized_entity)
						for token in nlp(entity_text):
							if token.pos_ in ['NOUN', 'PROPN', 'VERB']: # spacy tags some nouns as verbs
								# make sure it doesnt have any terms_to_exclude
								if len([term for term in terms_to_exclude if lemmatize_word(term) in token.text]) == 0:
									used_entities.add(entity_text)
							else:
								unused_entities.add(entity_text)
					else:
						unused_entities.add(f"lemmatized: {entity_text}")
	print('used_entities', used_entities)
	print('unused_entities', unused_entities)
	return used_entities, unused_entities

# **************************************************************************************************** #




# ************************************ VARIABLES ***************************************** #

known_treatments = ['eugenol', 'sitosterol', 'choline', 'fluconazole']
condition = 'fungal cryptococcus'
terms_to_exclude = condition.split(' ') if condition is not None and condition != '' else ['fung']

# **************************************************************************************** #



trivial_parts_of_speech = ['AUX', 'DET', 'ADP', 'PART', 'PUNCT', 'CCONJ', 'PRON'] # AUX = is, DET = the, ADP = of, PART = to, CCONJ = both, ADJ = clinical, only, major, new, PRON = the, which 
nontrivial_parts_of_speech = ['PROPN', 'NOUN', 'VERB', 'ADV', 'ADJ'] # PROPN = 'Citicoline', NOUN = CDP, choline, VERB = phosphatidylcholine, interacting, increase, is, ADV = especially, ADJ = generic, endogenous, able, central, nervous, cellular, especially

script_start_time = time.time()

# create filename from variables and create directories
filename = ''.join([c for c in condition if c in 'abcdefghijklmnopqrstuvwxyz'])[0:10]
saved_pubmed_download = f"pubmed-{filename}-set.txt"
print('\nusing file', saved_pubmed_download)
output_dir = f"{filename}_output"
corpus_dir = os.getcwd() + f"/{filename}_corpus"
for new_dir in [output_dir, corpus_dir]:
	if not os.path.exists(new_dir):
		os.mkdir(new_dir)

# to do: consolidate keywords and used_entities as possible_treatments and add a check of wikipedia to identify pathogens, compounds, processes
print('\nformatting & storing abstract and keyword lists, to identify possible treatments in keywords')
# format abstracts/keywords as a list from the downloaded pubmed file or the pubmed api
#abstracts, keywords = get_abstracts_from_pubmed_api(condition, 500, 'jonijezewski@outlook.com')
abstracts, keywords = get_abstracts_from_pubmed_download(saved_pubmed_download)
open(f"{output_dir}/keywords_{filename}.txt", 'w').write('\n'.join([item for item in keywords]))
open(f"{corpus_dir}/abstracts_{filename}.txt", 'w').write('\n'.join([abstract[0] for abstract in abstracts]))

print('\nfinding similar treatments based on sentence structure and word usage')
# find similar treatments based on similar sentence structure and word usages
all_similar_treatments = find_similar_words_using_custom_abstract_corpus(corpus_dir, abstracts, known_treatments, nontrivial_parts_of_speech)
open(f"{output_dir}/similar_treatments_to_known_treatments_{filename}.txt", 'w').write('\n'.join(all_similar_treatments))

print('\nextracting medical entities from abstracts to identify possible treatments')
# get entities (included and excluded from treatment list based on terms_to_exclude) and abstracts
used_entities, unused_entities = extract_entities_from_abstract(abstracts)
open(f"{output_dir}/unused_entities_{filename}.txt", 'w').write('\n'.join([item for item in unused_entities]))
open(f"{output_dir}/used_entities_{filename}.txt", 'w').write('\n'.join([item for item in used_entities]))

print('\nscript time', time.time() - script_start_time)