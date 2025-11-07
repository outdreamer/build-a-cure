import json, os
import nltk
from nltk import pos_tag, word_tokenize

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# identify interaction rules in repo
interaction_types = set()
interaction_rules = set()
directory = os.getcwd().replace('tasks', '')
print('dir', directory)
for root, directory, files in os.walk(directory):
	for f in files:
		if '.py' in f or '.md' in f or '.json' in f:
			full_path = os.getcwd() + '/' + f 
			print('full path', full_path)
			with open(f, 'r') as f:
				for line in f.readlines():
					tokens = nltk.word_tokenize(line)
					tags = nltk.pos_tag(tokens)
					interaction_rule = {}
					for tag in tags:
						print('tag', tag)
						if tag[0] in ['V', 'VB', 'VBP', 'VBN', 'VBG']:
							interaction_rule['verb'] = tag[1]
							interaction_types.add(tag[0])
						elif tag[0] in ['NN', 'N', 'NNP', 'NNS', 'JJ']:
							interaction_rule['objects'].append(tag[1])
					if interaction_rule:
						if interaction_rule['verb'] not in interaction_rules:
							interaction_rules[interaction_rule['verb']] = []
						interaction_rules[interaction_rule['verb']].append(','.join(interaction_rule['objects']))
						
with open('interaction_rules.json', 'w') as f:
	json.dump(f, interaction_rules, indent=3)