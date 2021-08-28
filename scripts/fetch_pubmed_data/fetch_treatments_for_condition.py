import nltk
import argparse, json, os, subprocess
from Bio.Entrez import efetch, read
from nltk.corpus import PlaintextCorpusReader
#import spacy
#genia_corpus = PlaintextCorpusReader('~/Downloads/craft-v0.9/genia-xml', '.*')
#print('genia_corpus', genia_corpus, type(genia_corpus))
#scipy_nlp = spacy.load("en_core_sci_sm")

# avoid this error with the 'make' command:

'''
/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1/algorithm:715:71: error: invalid operands to binary expression ('const Annotation' and 'const Annotation')
    bool operator()(const _T1& __x, const _T1& __y) const {return __x < __y;}
                                                                  ~~~ ^ ~~~
/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1/list:2310:13: note: in instantiation of member function 'std::__1::__less<Annotation, Annotation>::operator()' requested here
        if (__comp(*--__e2, *__f1))
            ^
/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1/list:2296:5: note: in instantiation of function template specialization 'std::__1::list<Annotation, std::__1::allocator<Annotation> >::__sort<std::__1::__less<Annotation> >' requested here
    __sort(begin(), end(), base::__sz(), __comp);
    ^
/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1/list:2287:5: note: in instantiation of function template specialization 'std::__1::list<Annotation, std::__1::allocator<Annotation> >::sort<std::__1::__less<Annotation> >' requested here
    sort(__less<value_type>());
    ^
namedentity.cpp:353:6: note: in instantiation of member function 'std::__1::list<Annotation, std::__1::allocator<Annotation> >::sort' requested here
  la.sort();
     ^
'''

# by commenting out this line in namedentity.cpp:
# la.sort();

# add parentheses around the print statements in geniatagger.py if youre using python3

# add this line in geniatagger.py:
# self._tagger.stdin.write(oneline + '\n')

# to this line:
# self._tagger.stdin.write((oneline + '\n').encode('utf-8'))

from geniatagger import GeniaTagger
geniatagger = GeniaTagger('./geniatagger/geniatagger')

email = 'jonijezewski@outlook.com'
#parser = English()

def find_treatments_for_condition(condition):

	results = search(condition)
	print('results found', len(results))

	if results:
		id_list = results['IdList']
		print('id_list', id_list)

		for pmid in id_list:
			abstract = fetch_abstract(pmid)
			if abstract is not None:

				entities = get_entities(abstract)
				print('found entities for pmid', pmid, len(entities))

				bio_entities = parse_with_geniatagger(abstract)
				print('found bio entities', bio_entities)
				all_bio_entities_found.update([item.lower() for item in bio_entities])

				all_entities_found.update([item.lower() for item in entities.keys()])

	return all_entities_found, all_bio_entities_found

def search(query):
	Entrez.email = email
	handle = Entrez.esearch(db='pubmed', sort='relevance', retmax='20', retmode='xml', term=query)
	results = Entrez.read(handle)
	return results

def fetch_abstract(pmid):
	handle = efetch(db='pubmed', id=pmid, retmode='xml')
	xml_data = read(handle)[0]
	print('xml_data', xml_data.keys())
	try:
		article = xml_data['MedlineCitation']['Article']
		abstract = article['Abstract']['AbstractText'][0]
		return abstract
	except IndexError:
		return None
	return None

def get_entities(text):
	entities = set()
	doc = scipy_nlp(text)
	sentences = list(doc.sents)
	if doc.ents:
		if len(doc.ents) > 0:
			print('doc.ents', set(doc.ents))
			entities = set(doc.ents)
	parsedEx = parser(text)
	for entity in list(parsedEx.ents):
		term = ' '.join(t.orth_ for t in entity)
		print('parser term', term)
	return entities

all_entities_found = set()
all_bio_entities_found = set()

#geniatagger_path = './geniatagger'
#geniatagger = subprocess.Popen(geniatagger_path, cwd='/'.join(geniatagger_path.split('/')[0:-1]), stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

tags = geniatagger.parse('sample bio text medicine')
print('tags', tags)

parser = argparse.ArgumentParser(description='find treatments for a condition')
parser.add_argument('-c', '--condition', required=True, help='find treatments tried for the specified condition')
args = parser.parse_args()
print('args', args)

if args.condition != '':
	entities, bio_entities = find_treatments_for_condition(condition)
	if entities:
		print('entities found', len(entities))
		with('entities.json', 'w') as f:
			json.dump(entities, f, indent=3)
	if bio_entities:
		print('bio_entities found', len(bio_entities))
		with('bio_entities.json', 'w') as f:
			json.dump(bio_entities, f, indent=3)