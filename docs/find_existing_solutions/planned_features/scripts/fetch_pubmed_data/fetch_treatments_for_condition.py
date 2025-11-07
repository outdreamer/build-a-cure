import nltk
import argparse, json, os, subprocess
import Bio.Entrez as Entrez
from Bio.Entrez import efetch, read
from geniatagger import GeniaTagger
from nltk.corpus import PlaintextCorpusReader
import spacy
import wikipedia 

scipy_nlp = spacy.load('en_core_web_sm')

# pip3 install pip -U
# pip3 install setuptools -U
# pip3 install spacy
# python3 -m spacy download en

# genia_corpus = PlaintextCorpusReader('~/Downloads/craft-v0.9/genia-xml', '.*')

# genia corpus downloads - http://www.geniaproject.org/genia-corpus/coreference

# use geniatagger from cli: ./geniatagger < input_textfile > output_textfile

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

def find_treatments_for_condition(condition, email):

	results = search(condition, email)
	print('search results found', len(results))

	if results:

		results_keys = ['Count', 'RetMax', 'RetStart', 'IdList', 'TranslationSet', 'TranslationStack', 'QueryTranslation']
		print('getting abstracts for each item in id_list', results['IdList'])

		for pmid in results['IdList']:

			abstract = fetch_abstract(pmid)

			if abstract is not None:

				entities, found_terms = get_entities(abstract)
				print('found entities for pmid', pmid, len(entities), entities)
				for entity, found_term in found_terms.items():
					print('found term for entity', entity, found_term)

				all_found_terms[entity] = found_term

				#bio_entities = parse_with_geniatagger(abstract)
				#print('found bio entities', bio_entities)
				#all_bio_entities_found.update([item.lower() for item in bio_entities])

				all_entities_found.update([item.lower() for item in entities])

	return all_entities_found

def search(query, email):
	Entrez.email = email
	handle = Entrez.esearch(db='pubmed', sort='relevance', retmax='20', retmode='xml', term=query)
	return Entrez.read(handle)

def fetch_abstract(pmid):
	sentences = set()
	val_key_sets = {}
	handle = efetch(db='pubmed', id=pmid, retmode='xml')
	xml_data = read(handle)
	if xml_data:
		#print('xml_data', type(xml_data), xml_data.keys()) # dict_keys(['PubmedBookArticle', 'PubmedArticle'])
		for article_type, articles in xml_data.items():
			#print('\n\nxml article_type', article_type, 'article', len(articles))
			for article in articles:
				#print('\narticle keys', article.keys()) # dict_keys(['MedlineCitation', 'PubmedData'])
				for key, val in article.items():
					#print('\narticle', type(key), key, type(val), val.keys()) 
					val_keys = ['GeneralNote', 'CitationSubset', 'SpaceFlightMission', 'OtherID', 'KeywordList', 'OtherAbstract', 'PMID', 'DateCompleted', 'DateRevised', 'Article', 'MedlineJournalInfo', 'ChemicalList', 'MeshHeadingList']
					val_key_sets[key] = [item for item in val.keys()]
					for item, value in val.items():
						if type(value) == str:
							val_key_sets[item] = [m for m in value.keys()]
							#value_keys['Article'] = [ArticleDate,ELocationID,Language,Journal,ArticleTitle,Pagination,Abstract,AuthorList,GrantList,PublicationTypeList]
						if item == 'Article':
							for i, j in value.items():
								if i == 'Abstract':
									for line in j['AbstractText']:
										sentences.add(str(line))

	#for key, item in val_key_sets.items():
		#print('val key sets', key, item)
		#val key sets ReferenceList,History,PublicationStatus,ArticleIdList
		#val key sets OtherAbstract,CitationSubset,SpaceFlightMission,OtherID,GeneralNote,KeywordList,PMID,DateCompleted,DateRevised,Article,MedlineJournalInfo,MeshHeadingList

	if len(sentences) > 0:
		return '\n'.join([sentence for sentence in sentences])
	return None

def check_summary_and_categories(term):

	summary = None
	try:
		summary = wikipedia.summary(term, sentences=3) #auto_suggest=False 
		print('summary', term, summary)

	except wikipedia.exceptions.DisambiguationError as e:
		for option in e.options:
			if term not in option.lower():
				return check_summary_and_categories(option)
		return e.options
	except wikipedia.exceptions.PageError as e:
		print('page not found', e)

	if summary is not None:
		for bio_keyword in bio_keywords:
			if bio_keyword in summary:
				return term

	page_object = None
	try:
		page_object = wikipedia.page(term)
	except wikipedia.exceptions.PageError as e:
		print('page not found', e)

	if page_object is not None:

		print('title', page_object.original_title, 'categories', page_object.categories, 'sections', page_object.sections)
		
		for section in page_object.sections:
			for bio_keyword in bio_keywords:
				if bio_keyword in section.lower():
					return term

		for category in page_object.categories:
			for bio_keyword in bio_keywords:
				if bio_keyword in category.lower():
					return term
	return False

def find_bio_term(index, options, tried_options):

	print('\nfind bio term from options', options[index], options)

	found_term = check_summary_and_categories(options[index])

	if type(found_term) == str:
		return options[index], tried_options

	elif type(found_term) == list:

		additional_options = found_term
		for i, additional_option in enumerate(additional_options):
			if additional_option not in tried_options:
				tried_options.add(additional_option)
				found_term, tried_options = find_bio_term(i, additional_options, tried_options)
				if found_term is not False:
					return found_term, tried_options

	search_result_options = wikipedia.search(options[index], results=5)
	for i, search_result_option in enumerate(search_result_options):

		search_result_option = ''.join([c for c in search_result_option if c in 'abcdefghijklmnopqrstuvwxyz0123456789 '])
		if search_result_option not in tried_options:
			tried_options.add(search_result_option)
			found_term, tried_options = find_bio_term(i, search_result_options, tried_options)
			if found_term is not False:
				return found_term, tried_options

	return False, tried_options

def get_entities(text):
	entities = set()
	entity_terms = {}
	doc = scipy_nlp(text)
	if doc.ents:
		for entity in doc.ents:
			entity_text = entity.text
			nonnumeric_text = entity_text
			for string in ['year', 'month', 'day', 'years', 'months', 'days']:
				nonnumeric_text = nonnumeric_text.replace(string, '')
			just_string = ''.join([c for c in nonnumeric_text.strip() if c not in '0123456789.,%/ '])
			if len(just_string) > 0:
				found_term, tried_options = find_bio_term(0, [just_string], set())
				print('found term for entity', found_term, entity)
				print('tried_options', tried_options)
				entity_terms[just_string] = found_term
				entities.add(entity_text)
	return entities, entity_terms

bio_keywords = ['health', 'scien', 'medical', 'medic', 'bio', 'chem', 'treatment', 'drug', 'illness', 'anatom']

all_found_terms = {}
if os.path.exists('all_found_terms.json'):
	with open('all_found_terms.json', 'r') as f:
		all_found_terms = json.load(f)

all_entities_found = set()
all_bio_entities_found = set()

#geniatagger = GeniaTagger('./geniatagger/geniatagger')
#geniatagger_path = './geniatagger'
#geniatagger = subprocess.Popen(geniatagger_path, cwd='/'.join(geniatagger_path.split('/')[0:-1]), stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#tags = geniatagger.parse('sample bio text medicine')
#print('tags', tags)

parser = argparse.ArgumentParser(description='find treatments for a condition')
parser.add_argument('-c', '--condition', required=True, help='find treatments tried for the specified condition')
args = parser.parse_args()
print('args', args)
email = 'jonijezewski@outlook.com'

if args.condition != '':

	all_entities_found = find_treatments_for_condition(args.condition, email)
	print('entities found', len(all_entities_found))

	with open('all_entities_found.json', 'w') as f:
		json.dump(list(all_entities_found), f, indent=3)
	with open('all_bio_entities_found.json', 'w') as f:
		json.dump(list(all_bio_entities_found), f, indent=3)
	with open('all_found_terms.json', 'w') as f:
		json.dump(all_found_terms, f, indent=3)