'''


PURPOSE: this script helps find possible treatments for a condition, 
by compiling a list of nouns mentioned in research studies for a given search like 'meningitis treatment', 
as these nouns could be possible treatments studied recently

1. run a search on pubmed for the condition (like 'meningitis treatment') so you're at a url with your search terms in it 
	- example: https://pubmed.ncbi.nlm.nih.gov/?term=meningitis%20treatment
2. then click the Save button, select 'All results' and 'Pubmed format'
3. move the downloaded file to the same directory as the script
4. run the script: python3 parse_pubmed_download.py


NOTE ON WHAT TO CHANGE:
- changing the 'condition' variable to match your search is useful to exclude that term from the possible treatment list created by the keywords and nouns in the summary
- also update "terms_to_exclude" with a list of any other terms like ['biology', 'exclude-this'] you want to remove from the list of nouns that could be possible treatments studied
- this will also retrieve plenty of irrelevant nouns as well like names of places where data was gathered, so maybe add 'treatment' to your search to only focus on treatment articles
- a good way to think of this tool is, as a 'way to find all the variables associated with a condition (including related conditions, symptoms/complications, related bio-system components like cell types involved, possible causes), 
  where some of the variables are possible treatments which have been recently studied'
- you can filter your Pubmed search by recent results to make sure youre only finding the most recent treatments


INSTALLATION: 

- install primary libraries
	pip3 install nltk scispacy spacy 
- install the scispacy entity recognition model (which can identify a compound/organism/antibody/etc)
	pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.0/en_core_sci_sm-0.2.0.tar.gz
- use spacy validate to check for updates & update en_core_web_sm accordingly
	- python3 -m spacy validate
	- python -m spacy download en_core_sci_sm

- install errors like 'package not found' 
	- run "pip3 install packagename" of the package that is not installed, when you run the python3 parse_pubmed_download.py command and it says you didnt install some package.


NOTES:
- the script can take up to half an hour to run on 10,000 search results


EXAMPLE OUTPUT:
- for 'cancer treatment' Pubmed search results, this script included 'lysine', 'dendritic cell vaccines', 'checkpoint inhibitors', 'VSV (an oncolytic virus)' in its results, their interaction with cancer being useful to know about
- for 'fungal treatment' Pubmed search results, this script included 'eugenol' and 'choline' which are active against that condition.
- on the other side, there were thousands of nouns to sift through, so this tool could use some filtering.
- also, harmful substances were included in the search results (amphotericin is very harmful and can be deadly in the amounts required to fight a fungal infection)
- also, ineffective substances were included in the search results (miltefosine is ineffective for some people with fungal infections).
- similarly, some treatments will be missing, as only 10,000 results can be downloaded at a time - for example, the search results for 'fungal cryptococcus' did not include sitosterol or Undecylenic acid, both being known treatments.
- I think Pubmed includes Ayurvedic and Chinese medicine substances in a lot of the studies published there so I think it's a good general reference, although it is incomplete, as there are studies hosted on other sites that I haven't found on Pubmed


OUTPUT:
- this script will store the found nouns in a file called "possible_treatment_nouns_{condition}".txt in the same directory that the script is in.


TO DO LIST:
- add 'integrated deduplicated search results' so that results that occur in multiple searches can be de-duplicated (to find generally useful compounds that can help multiple conditions, for those managing multiple conditions)
- add filters to remove irrelvant nouns like places and filter out anything that isnt a treatment (compound, process, pathogen)
- lemmatize common words
- use context checking for a similarity metric from nltk - https://www.nltk.org/book/ch05.html
- filter out variants of the same word
- add generation of similar searches, such as a general type search as in 'fungal treatment' or a similar but more common fungal species like 'candida treatment' instead of 'cryptococcus treatment' or pathogens that bind to cryptococcus like 'staphylococcus aureus'

'''

import io
from contextlib import redirect_stdout
import os
import spacy, en_core_web_sm
import nltk
from nltk.corpus import stopwords
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

import scispacy
import spacy
from spacy import displacy
from scispacy.abbreviation import AbbreviationDetector
from scispacy.umls_linking import UmlsEntityLinker

#sci_nlp = spacy.load('en_core_web_sm')
#sci_nlp = en_core_sci_sm.load()

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download("vader_lexicon")
#nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

nlp = spacy.load('en_core_web_sm')

all_abstract_words_and_keywords = []
keywords_found_in_treatment_articles = set()
compounds_pathogens_found_in_treatments = set()

known_treatments = ['eugenol', 'sitosterol', 'choline', 'fluconazole']
condition = 'fungal cryptococcus'

filename = ''.join([c for c in condition if c in 'abcdefghijklmnopqrstuvwxyz'])[0:10]
terms_to_exclude = condition.split(' ') if condition is not None and condition != '' else []
saved_pubmed_download = f"pubmed-{filename}-set.txt"
print('using file', saved_pubmed_download)
found_abstract = False
abstracts = []
all_text = None

with open(saved_pubmed_download, 'r') as f:
	for line in f.readlines():
		if 'OT  - ' in line:
			line = line.replace('OT  - ', '')
			for word in condition.split(' '):
				if word not in line:
					if len([item for item in terms_to_exclude if item in line]) == 0:
						keywords_found_in_treatment_articles.add(line.strip())
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

excluded_types = ['PERSON', 'ORGANIZATION']
all_entities = set()
unused_entities = set()
for abstract in abstracts:

	# filter abstract using scispacy entity detector, to create the most filtered list using entity recognition
	doc = nlp(abstract.lower().strip())
	sentences = list(doc.sents)
	entities = doc.ents
	for entity in entities:
		# make sure its a noun
		tokens = nlp(entity.text)
		for token in tokens:
			if token.pos_ in ['NOUN', 'PROPN', 'VERB']: # spacy tags some nouns as verbs
				# then make sure it doesnt have any terms_to_exclude
				if len([item for item in terms_to_exclude if item in token.text]) == 0:
					all_entities.add(entity)
			else:
				unused_entities.add(entity)

	# remove places, people, organizations and other non-treatment words
	''' # an attempt to use nltk to filter out useless entities
	filtered_abstract_sentences = []
	for sentence in abstract.lower().split('\n'):
		# make sure its not a stopword
		#if word not in stop_words:
		# make sure its a noun
		tokens = nlp(sentence)
		filtered_abstract_sentence = []
		for token in tokens:
			if token.pos_ in ['NOUN', 'PROPN', 'VERB']: # spacy tags some nouns as verbs
				# then make sure it doesnt have any terms_to_exclude
				if len([item for item in terms_to_exclude if item in token.text]) == 0:
					print('recognizing entities with nltk')
					tokenized = nltk.word_tokenize(sentence)
					pos_tagged = nltk.pos_tag(tokenized)
					chunks = nltk.ne_chunk(pos_tagged)
					for chunk in chunks:
						if hasattr(chunk, 'label'):
							print('chunk', chunk)
							print(chunk[0], chunk[1])
							# then make sure its not a person, organization, or other term types in excluded_types
							if chunk[0] not in excluded_types:
								filtered_abstract_sentence.append(chunk[1].split('/'))

					print('recognizing entities with spacy')
					spacy_token = nlp(sentence)
					for entity in spacy_token.ents:
						print('entity', entity.text, entity.label_)
						if entity.label_ not in excluded_types:
							filtered_abstract_sentence.append(entity.text)
		filtered_abstract_sentences.append(' '.join(filtered_abstract_sentence))
	'''
	all_abstract_words_and_keywords.extend([' '.join(abstract.lower().split('\n')), '']) # add a blank line for the corpus reader

print('keywords_found_in_treatment_articles', keywords_found_in_treatment_articles)
open(f"possible_treatment_nouns_{filename}.txt", 'w').write('\n'.join([item for item in keywords_found_in_treatment_articles]))

# attempt to create a custom corpus and identity similar words by context (such as identifying 'voraconazole' from 'fluconazole')
# create nltk corpus from all_abstract_words_and_keywords
corpus_dir = os.getcwd() + '/corpus/'
if not os.path.exists(corpus_dir):
	os.mkdir(corpus_dir)
corpus_filename = f"all_abstract_words_and_keywords_{filename}.txt"
with open(f"{corpus_dir}{corpus_filename}", 'w') as f:
	f.write('\n'.join(all_abstract_words_and_keywords))
new_corpus = PlaintextCorpusReader(corpus_dir, r'.*\.txt')
print('new corpus words', new_corpus.words())
all_text = nltk.Text(new_corpus.words())

# find substances with similar contexts (used in similar ways in the sentence) as 'eugenol', a known treatment
all_similar_treatments = []
for known_treatment in known_treatments:
	f = io.StringIO()
	with redirect_stdout(f):
		similar_treatments = all_text.similar(known_treatment)
	out = f.getvalue()
	print('similar_treatments', similar_treatments)
	print('out', out)
	print('similar_treatments', known_treatment, out)
	similar_treatments_text = similar_treatments.text
	if similar_treatments_text is not None and len(similar_treatments_text) > 0:
		new_item = known_treatment + '_is_similar_to_' + ','.join([item for item in out.split('\n')])
		if len(all_similar_treatments) == 0:
			all_similar_treatments = [new_item]
		else:
			all_similar_treatments.append(new_item)
open(f"similar_treatments_{filename}.txt", 'w').write('\n'.join(all_similar_treatments))

print('all_entities', all_entities)
open(f"all_entities_{filename}.txt", 'w').write('\n'.join([item for item in all_entities]))

print('unused_entities', unused_entities)