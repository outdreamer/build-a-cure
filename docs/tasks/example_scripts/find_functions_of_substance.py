import argparse
import time
import json
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

import wikipedia

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

def lemmatize_word(word):
    lemmatized = lemmatizer.lemmatize(word)
    lemmatized_without_letters = [c for c in lemmatized.lower() if c not in 'abcdefghijklmnopqrstuvwxyz']
    if len(lemmatized_without_letters) < len(lemmatized):
        return lemmatized
    return False # not likely to be found in entities where this function is used

def is_medical_term(phrase, original_call):
    try:
        if phrase in already_identified_medical_terms:
            return True
        if phrase in already_identified_not_medical_terms:
            return False
        page = wikipedia.page(phrase)
        categories = [item.lower() for item in page.categories]
        references = ','.join(page.references)
        chemical_found = True if len([item for item in categories if 'chemical' in item]) > 0 else False
        if len([source for source in medical_sources if source in references]) > 0:
            chemical_found = True
        return chemical_found
    except wikipedia.DisambiguationError as e:
        print('e options', e.options)
        if original_call is True:
            for option in e.options:
                chemical_found = is_medical_term(option, False)
                if chemical_found is True:
                    return True
    except Exception as e:
        #print('search exception', phrase, e)
        # assume its a medical term if there is no entry for it
        return True
    return False

def get_wiki_info(phrase, original_call, include_links):
    print('get_wiki_info searching phrase in wiki', phrase)
    try:
        related_substances_variants = set([item for item in wikipedia.search(phrase)]) # search doesnt disambiguate
        summary = wikipedia.summary(phrase)
        page = wikipedia.page(phrase)
        categories = [item.lower() for item in page.categories]
        references = ','.join(page.references)
        links_not_medical_terms = ['articles', 'cs1 ', 'image', 'wiki', 'info', 'journal', 'identifier', 'chebi', 'chembl', 'chemspider', 'chemical', '(anatomy)', 'ineffective', '(data page)']
        links_medical_terms = ['(drug)', 'substance', '(biochemistry)', '(flavonol)', 'inhibitor', 'modulator', 'agonist', 'acid', 'pubchem cid', 'metabolite']
        possible_functions_from_categories = [item for item in categories if len([term for term in links_not_medical_terms if term in item]) == 0]
        print('possible_functions_from_categories', possible_functions_from_categories)
        print('summary', summary)
        # to do: handle false negatives like AC-186, KN-04, MRL-37, NF-110, RO-3, mrs-1754, Uridine and false positives like Standard state True
        if include_links is True:
            for link in page.links:
                link = link.lower()
                if len([item for item in links_medical_terms if item in link]) > 0:
                    medical_term = True
                elif len([term for term in links_not_medical_terms if term in link]) == 0:
                    link_without_parenthesis = link.split('(')[0].strip()
                    medical_term = is_medical_term(link, False)
                    print('is_medical_term searching phrase in wiki', link, medical_term)
                if medical_term is True:
                    already_identified_medical_terms.add(link)
                else:
                    already_identified_not_medical_terms.add(link)
                if medical_term is True:
                    #to do: filter functional nouns like 'apoptosis' from links 
                    #verb_noun = [token for token in nlp(link) if token.pos_ in ['PROPN', 'NOUN']]
                    related_substances_variants.add(link)
        chemical_found = True if len([item for item in categories if 'chemical' in item]) > 0 else False
        if len([source for source in medical_sources if source in references]) > 0:
            chemical_found = True
        return related_substances_variants, possible_functions_from_categories, chemical_found
        '''possible_functions_from_categories ['aromatase inhibitors', 'cyp2c8 inhibitors', 'cyp3a4 inhibitors', 'experimental medical treatments', 
        'flavonoid antioxidants', 'gper agonists', 'phytoestrogens', 'quercetin', 'selective erβ agonists', 'xanthine oxidase inhibitors']
        categories ['Aromatase inhibitors', 
        'Articles containing unverified chemical infoboxes', 'Articles with BNF identifiers', 'Articles with BNFdata identifiers', 'Articles with FAST identifiers', 'Articles with GND identifiers', 'Articles with J9U identifiers', 
        'Articles with LCCN identifiers', 'Articles with SUDOC identifiers', 'Articles with short description', 
        'CS1 errors: periodical ignored', 'CS1 maint: DOI inactive as of August 2023', 
        'CYP2C8 inhibitors', 'CYP3A4 inhibitors', 
        'Chembox image size set', 'Chemical articles with multiple CAS registry numbers', 'Chemical articles with multiple compound IDs', 
        'Commons category link from Wikidata', 
        'ECHA InfoCard ID from Wikidata', 
        'Experimental medical treatments', 
        'Flavonoid antioxidants', 'GPER agonists', 
        'Multiple chemicals in an infobox that need indexing', 
        'Phytoestrogens', 'Quercetin', 'Selective ERβ agonists', 
        'Short description is different from Wikidata', 'Xanthine oxidase inhibitors']
        '''
    except wikipedia.DisambiguationError as e:
        #pass
        print('e options', e.options)
        if original_call is True:
            for option in e.options:
                variants, functions, chemical_found = get_wiki_info(phrase=option, original_call=False, include_links=include_links)
                if chemical_found is True:
                    return variants, functions, chemical_found
    except Exception as e:
        print('search exception', phrase, e)
        # assume its a medical term if there is no entry for it
        return True, True, True
    return False, False, False

def get_abstracts_from_pubmed_download(saved_pubmed_download):
    found_abstract = False
    abstracts = []
    keywords = set()
    with open(saved_pubmed_download, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if 'OT  - ' in line:
                line = line.replace('OT  - ', '')
                for word in substance.split(' '):
                    if word not in line:
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
    abstracts = [[' '.join(abstract.lower().split('\n'))] for abstract in abstracts if abstract != []] # dont add a blank line for the corpus reader
    return abstracts, keywords

def find_related_substances(entity, substance, sentence):
    related_substances_variants_in_sentence = set()
    entity_text = entity.text.lower().strip()
    if entity_text != substance:
        medical_term = is_medical_term(entity_text, False)
        if medical_term is True:
            already_identified_medical_terms.add(entity_text)
        else:
            already_identified_not_medical_terms.add(entity_text)
        print('is_medical_term searching phrase in wiki', entity_text, medical_term)
        if medical_term is True:
            substance_words = substance.split(' ')
            entity_words = entity_text.split(' ')
            # compare with rest of sentence for context in finding related substances like aliases and components
            # check for an alias 'GH' in a phrase like 'growth hormone (GH)'
            if substance in sentence:
                if '(' in entity_text and ')' in entity_text:
                    related_substances_variants_in_sentence.add(entity_text.replace('(', '').replace(')', ''))
            # check for a component like 'metabolite', 'component', 'section'
            if len([component_word for component_word in component_words if component_word in sentence]) > 0:
                related_substances_variants_in_sentence.add(entity_text)
            # check for a variant like 'growth factor' (has a lemma or substring in common with this entity)
            # check for a related compound like 'growth hormone inhibitor' (has a modifier or other difference)
            for word in entity_words:
                for i, c in enumerate(word):
                    if i > 3 and word[0:i] in substance:
                        related_substances_variants_in_sentence.add(entity_text)
                        break
            for word in substance_words:
                for i, c in enumerate(word):
                    if i > 3 and word[0:i] in entity_text:
                        related_substances_variants_in_sentence.add(entity_text)
                        break
            #words_in_common = [word for word in entity_words if word in substance]
            #lemmatized_variant_words_found_in_substance = [word for word in entity_words if lemmatize_word(word) in substance]
            #lemmatized_substance_words_found_in_variant = [word for word in substance_words if lemmatize_word(word) in entity_text]
            #if len(words_in_common) / len(substance_words) > 0.5 or len(lemmatized_variant_words_found_in_substance) / len(entity_words) > 0.5 or len(lemmatized_substance_words_found_in_variant) / len(entity_words) > 0.5:
            #    related_substances_variants_in_sentence.add(entity_text)
    return related_substances_variants_in_sentence


substance = 'quercetin'
filtering_condition = 'cancer'
medical_sources = ['nih.gov', 'cdc.gov', 'who.int', 'nhs.uk', 'doi.org'] # pubmed contains nih.gov
medical_terms = ['disease', 'bio', 'species', 'mechanism', 'treatment', 'health', 'target', 'therap', 'bac', 'fung', 'vir', 'escher', 'pathogen', 'microb', 'chemical', 'compound', 'medic', 'substance', 'some', 'organism', 'organ', 'plas', 'immun', 'vitam', 'nutrient', 'inflamm']
medical_terms_to_check = [
    'sis', 'sus', 'oid', 'ose', 'ceph', 'aly', 'leu', 'ate', 'delt', 'yl', 'ster', 'amphi', 'dend',
    'meth', 'oxy', 'kary', 'cere', 'sia', 'eri', 'sept', 'ima', 'ora', 'benz', 'ase', 'ii', 'il', 'rin', 'amin', 'tion', 'ae', 'ius', 'cus', 'ia', 'mab', 'ica', 'lic', 
    'lis', 'ila', 'lin', 'lus', 'ean', 'cyt', 'arth', 'derm', 'trich', 'staph', 'ete', 'iso', 'ana', 'spor', 'gen', 'zym', 'san', 'era', 'rus', 'tum', 'eum', 'osa', 
    'geno', 'pheno', 'tis', 'ans', 'zol', 'nis', 'cia', 'alde', 'cin', 'sin', 'iva', 'ola', 'sil', 'ane', 'vin', 'ese', 'phy', 'gin', 'mis', 'iol', 'one', 'chol', 'ion',
    'ens', 'occ', 'glu', 'tol', 'nol', 'rol', 'element', 'vor', 'zol', 'cin', 'prot', 'bet', 'alph', 'ium', 'ella', 'ala', 'dia', 'itis', 'myc', 'ryp', 'fol', 'anth', 
    'aqu', 'tissue', 'lymph', 'trans', 'globul', 'trid', 'chy', 'aden', 'xyl', 'thy', 'ein', 'tin', 'ide', 'ine', 'methyl', 'lysis', 'acetyl', 'oxid',  'strain', 'avi', 
    'gamma', 'morph', 'syl', 'terp', 'oma', 'pyr', 'epi', 'phe', 'ris', 'glyc', 'ite', 'ize', 'flav', 'plat', 'aca', 'guan', 'xan', 'cyn', 'ima', 'ida', 'sys', 'ken', 
    'gene', 'cell', 'prot', 'enzyme', 'acid', 'base', 'non', 'mono', 'bi', 'tri', 'quat', 'pent', 'dna', 'rna', 'prop', 'eryth', 'euk', 'proto', 'eus', 'sum', 
    'sugar', 'alcohol', 'energy', 'metab', 'carbo', 'hydr', 'lipid', 'anti', 'anti', 'ria', 'fluro', 'chia', 'acti', 'eal', 'din', 'pha', 'poly', 'mer', 'chlo', 
    'um', 'oxi', 'kin', 'mico', 'aly', 'spl', 'rsi', 'nic', 'mos', 'neut', 'tox', 'oxo', 'idi', 'oe', 'mic', 'eu',
]
target_words = ['target', 'therap', 'treatment']
remove_words = ['mgkg', 'dose', 'assay', 'test', 'µ', '±', '=', '+', '%', '\\x']
component_words = ['metabolite', 'component', 'section', 'subset', 'piece', 'part', 'input', 'output', 'exudate', 'product']
function_words = ['suppress', 'exhibit', 'show', 'capacity', 'promot', 'diminish', 'exacerb', 'magnif', 'affect', 'reveal', 'seen', 'includ', 'protect', 'promising', 'action', 'mechanism', 'used', 'dys', 'ability', 'effect', 'activ', 'anti', 'pro', 'reduc', 'induc', 'express', 'inhibit', 'trigger', 'agoni', 'change', 'modif', 'modul', 'initia', 'stress', 'increas', 'decreas', 'upreg', 'downreg', 'regulat', 'control', 'enhanc', 'target', 'mechan', 'act', 'propert', 'attribute', 'function']
already_identified_medical_terms = set()
already_identified_not_medical_terms = set()
if not os.path.exists(substance):
    os.mkdir(substance)
filename = ''.join([c for c in substance.lower() if c in 'abcdefghijklmnopqrstuvwxyz'])[0:10]
saved_pubmed_download = f"pubmed-{filename}-set.txt"
print('\nusing file', saved_pubmed_download)

# to do: create a list of aliases/alternate names of a substance as well as its components and variants, which can be treated like equivalent to the substance in finding the functions of a substance

# get info about substance from wiki
related_substances_variants, functions_found, chemical_found = get_wiki_info(phrase=substance, original_call=True, include_links=False)
functions_found_for_substance = functions_found
no_substance_found_sentences = []
not_included_sentences = []
related_sentences = []
substances_found = []
targets_found = []
# get abstracts/keywords from download
articles, keywords = get_abstracts_from_pubmed_download(saved_pubmed_download)
open(f"{substance}/keywords.txt", 'w').write('\n'.join([item for item in keywords]))
article_count = len(articles) # 100

# add keywords to related substance
#for keyword in keywords:
#    related_substances_variants.add(keyword)

'''
# find related substances in article sentences 
for article_list in articles:
    print('article', article_list)
    for article in article_list:
        for sentence in article.split('. '):
            sentence = sentence.lower()
            entities_in_sentence = [token for word in sentence.split(' ') for token in nlp(word) if token.pos_ in ['PROPN', 'NOUN']] #'VERB']]
            print('entities_in_sentence', entities_in_sentence, sentence)
            for entity in entities_in_sentence:
                related_substances_variants_in_sentence = find_related_substances(entity, substance, sentence)
                related_substances_variants.update(related_substances_variants_in_sentence)
'''

# use related terms to identify sentences that include the substance or a related term which can be filtered further to identify functionality of the substance or its related substances
for article_list in articles[0:article_count]:
    #print('article', article_list)
    for article in article_list:
        if filtering_condition in article:
            for sentence in article.split('. '):
                if len(sentence) > 3: # occasionally a sentence will be a letter with punctuation bc of scientific names

                    sentence = ' '.join([word for word in sentence.lower().replace('(', '').replace(')', '').split(' ') if len(word) > 1])
                    # to do: identify lists of functions
                    # identify lists of nouns as substances/targets
                    non_numerical_sentence = ''.join([c for c in sentence if c in 'abcdefghijklmnopqrstuvwxyz, -/'])

                    # treat noun_lists like possible functions, treatments, targets, symptoms/conditions
                    and_sentence = non_numerical_sentence.replace(' and ', ' ').replace(' or ', ' ')
                    lists = []
                    new_list = []
                    for i, word in enumerate(and_sentence.split(' ')):
                        noun = [token for token in nlp(word) if token.pos_ in ['PROPN', 'NOUN']]
                        if len(noun) > 0:
                            new_list.append(word)
                        else:
                            if len(new_list) > 0:
                                lists.append(new_list)
                                new_list = []
                    if len(new_list) > 0:
                        lists.append(new_list)
                    noun_lists = []
                    for list_item in lists:
                        phrase = ' '.join(list_item).strip()
                        if phrase.count(',') > 1 and len(list_item) > 2:
                            noun_lists.append(' '.join(list_item).replace(', ', ' '))
                    if len(noun_lists) > 0:
                        print('noun_lists', noun_lists)
                        for list_items_phrase in noun_lists:
                            if len([f for f in function_words if f in list_items_phrase]) > 0:
                                functions_found_for_substance.append(list_items_phrase)
                            elif len([t for t in target_words if t in list_items_phrase]) > 0:
                                targets_found.append(list_items_phrase)
                            else:
                                substance_found = False
                                for item in medical_terms_to_check:
                                    if item in sentence:
                                        substance_found = True
                                        break
                                if substance_found is True:
                                    substances_found.append(list_items_phrase)
                                else:
                                    no_substance_found_sentences.append(list_items_phrase)
                                substances_found.append(list_items_phrase)
                        
                    # treat clauses like individual sentences
                    replaced_sentence = non_numerical_sentence
                    clause_delimiters = ['but', 'while', 'which', 'instead', 'so', 'even', 'still', 'however', 'yet', 'because', 'since', 'as']
                    for clause_delimiter in clause_delimiters:
                        if ', ' + clause_delimiter in sentence:
                            replaced_sentence = sentence.replace(clause_delimiter, 'xxx')
                    clauses = replaced_sentence.split('xxx')
                    for clause in clauses:
                        if len([f for f in function_words if f in sentence]) > 0:
                            functions_found_for_substance.append(sentence)
                        elif len([t for t in target_words if t in sentence]) > 0:
                            targets_found.append(sentence)
                        elif len([w for w in remove_words if w in sentence]) > 0: # remove sentences about dosing and tests
                            not_included_sentences.append(sentence)
                        elif len([i for i in related_substances_variants if i in sentence]) > 0: # or substance in sentence:
                            related_sentences.append(sentence)
                        else:
                            substance_found = False
                            for item in medical_terms_to_check:
                                if item in sentence:
                                    substance_found = True
                                    break
                            if substance_found is True:
                                functions_found_for_substance.append(sentence)
                            else:
                                no_substance_found_sentences.append(sentence)

# print and save
print('substances_found', len(substances_found), [i for i in substances_found][0:10])
open(f"{substance}/substances_found.txt", 'w').write('\n'.join(list(set([i for i in substances_found]))))
print('targets_found', len(targets_found), [i for i in targets_found][0:10])
open(f"{substance}/targets_found.txt", 'w').write('\n'.join(list(set([i for i in targets_found]))))
print('functions_found_for_substance', len(functions_found_for_substance), [i for i in functions_found_for_substance][0:10])
open(f"{substance}/functions_found.txt", 'w').write('\n'.join(list(set([i for i in functions_found_for_substance]))))
print('related_sentences', len(related_sentences), [i for i in related_sentences][0:10])
open(f"{substance}/related_sentences.txt", 'w').write('\n'.join(list(set([i for i in related_sentences]))))
print('not_included_sentences', len(not_included_sentences), [i for i in not_included_sentences][0:10])
open(f"{substance}/not_included_sentences.txt", 'w').write('\n'.join(list(set([i for i in not_included_sentences]))))
print('related_substances_variants', len(related_substances_variants), [i for i in related_substances_variants][0:10])
open(f"{substance}/related_substances_variants_found.txt", 'w').write('\n'.join([i for i in related_substances_variants]))
print('no_substance_found_sentences', len(no_substance_found_sentences), [i for i in no_substance_found_sentences][0:10])
open(f"{substance}/no_substance_found_sentences.txt", 'w').write('\n'.join([i for i in no_substance_found_sentences]))