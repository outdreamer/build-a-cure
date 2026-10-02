import nltk 

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

nltk.download('wordnet')

from nltk.corpus import wordnet

def get_synonyms(sentence):
	synonyms = []
	for word in sentence.split(' '):
		for syn in wordnet.synsets(word):
			for lemma in syn.lemmas():
				synonyms.append(lemma.name())
	return set(synonyms)

def get_nouns(sentence):
	noun1, noun2 = None, None
	switch_flag = False
	for word in sentence.split(' '):
		for token, tag in nltk.pos_tag(nltk.word_tokenize(word)):
			if tag in ['NN', 'NNS', 'NNP', 'NNPS'] and switch_flag is False:
				noun1 = word
			if tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
				switch_flag = True # switch on first verb
			if tag in ['NN', 'NNS', 'NNP', 'NNPS'] and switch_flag is True:
				noun2 = word
	return noun1, noun2
