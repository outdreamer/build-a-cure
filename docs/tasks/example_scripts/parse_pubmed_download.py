'''

PURPOSE: this script helps find possible treatments for a condition, 
by compiling a list of nouns mentioned in research studies for a given search like 'meningitis treatment', 
as these nouns could be possible treatments studied recently

1. run a search on pubmed for the condition (like 'meningitis treatment') so you're at a url with your search terms in it 
    - example: https://pubmed.ncbi.nlm.nih.gov/?term=meningitis%20treatment
2. then click the Save button, select 'All results' and 'Pubmed format'
3. move the downloaded file to the same directory as the script
4. run the script: python3 parse_pubmed_download.py

NOTE: I think Pubmed includes Ayurvedic and Chinese medicine substances in a lot of the studies published there so I think it's a good general reference, 
although it is incomplete, as there are studies hosted on other sites that I haven't found on Pubmed

NOTE ON WHAT TO CHANGE:
- changing the 'condition' variable to match your search is useful to exclude that term from the possible treatment list created by the keywords and nouns in the summary
- also update "terms_to_exclude" with a list of any other terms like ['biology', 'exclude-this'] you want to remove from the list of nouns that could be possible treatments studied
- this will also retrieve plenty of irrelevant nouns as well like names of places where data was gathered, so maybe add 'treatment' to your search to only focus on treatment articles

'''

import spacy

nlp = spacy.load('en_core_web_sm')

keywords_found_in_treatment_articles = set()
compounds_pathogens_found_in_treatments = set()

condition = 'multiple sclerosis'
filename = ''.join([c for c in condition if c in 'abcdefghijklmnopqrstuvwxyz'])[0:10]
terms_to_exclude = [condition.split(' ')]
saved_pubmed_download = f"pubmed-{filename}-set.txt"
print('using file', saved_pubmed_download)
found_abstract = False
abstracts = []
nouns_from_abstracts = set()

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

for abstract in abstracts:
	tokens = nlp(line)
	for token in tokens:
		if token.pos_ in ['NOUN', 'PROPN', 'VERB']:
			if len([item for item in terms_to_exclude if item in token.text]) == 0:
			    nouns_from_abstracts.add(token.text.strip())

print('nouns_from_abstracts', nouns_from_abstracts)
print('keywords_found_in_treatment_articles', keywords_found_in_treatment_articles)