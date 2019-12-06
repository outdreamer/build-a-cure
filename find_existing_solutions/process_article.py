from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

'''
- types follow patterns:
    1. <adjective> <noun>
    Ex: 'chaperone protein' (subtype = 'chaperone', type = 'protein')

- roles follow patterns:
    1. <adverb> || <verb> <noun>
    Ex: 'emulsifying protein' (role = 'emulsifier')

    2. <noun> of <noun>
    Ex: 'components of immune system' (role = 'component', system = 'immune system')

    3. <verb> || <noun> role
    Ex: functional role (role => 'function')

    4. functions/works/operates/interacts/acts as (a) <verb> || <noun>
    Ex: acts as an intermediary (role => 'intermediary')

- roles are intrinsically related to functions, intents, strategies, & mechanisms

# the word with the highest count that is a noun is likely to be a focal object of the article
'''

def convert_patterns(lang_patterns):
    patterns = []
    for p in lang_patterns:
        pattern = []
        for alt_phrases in p.split('--'):
            pos_list = alt_phrases.split(' ')
            all_pos = [True for pos_item in pos_list if pos_item in language_pos_map.keys()]
            if len(all_pos) == len(pos_list):
                ''' this is a set of alternative parts of speech '''
                final_list= ['[']
                for item in pos_list:
                    final_list.append(language_pos_map[item].replace('[','').replace(']',''))
                final_list.append(']')
                pattern.append(''.join(final_list))
        for i, w in enumerate(p.split(' ')):
            if w in language_pos_map.values():
                pattern.append(language_pos_map[w])
            else:
                pattern.append(w)
        patterns.append(' '.join(pattern))
    if len(patterns) > 0:
        return patterns
    return False

def get_pos(word):
    noun_string = '<noun>'
    verb_string = '<verb>'
    if len(word) > 0:
        stem = stemmer.stem(word)
        tagged = pos_tag(word_tokenize(word))
        tagged_stem = pos_tag(word_tokenize(stem))
        pos = [item[1] for item in tagged if item[0].lower() == word]
        stem_pos = [item[1] for item in tagged_stem if item[0].lower() == stem]
        if (len(pos) > 0 and pos[0] in noun_pos):
            return noun_string
        elif (len(pos) > 0 and pos[0] in verb_pos):
            return verb_string
        elif len(stem_pos) > 0:
            if stem_pos[0] in noun_pos:
                return noun_string
            elif stem_pos[0] in verb_pos:
                return verb_string
        else:
            noun_synsets = Word(word).get_synsets(pos=NOUN)
            verb_synsets = Word(word).get_synsets(pos=VERB)
            if len(noun_synsets) > 0:
                return noun_string
            elif len(verb_synsets) > 0:
                return verb_string
            else:
                noun_stem_synsets = Word(stem).get_synsets(pos=NOUN)
                verb_stem_synsets = Word(stem).get_synsets(pos=VERB)
                if len(noun_stem_synsets) > 0:
                    return noun_string
                elif len(verb_stem_synsets) > 0:
                    return verb_string
        #print('unknown word', word, pos, stem_pos, noun_synsets, verb_synsets)
    return False

def convert_to_pattern_format(line):
    new_line = []
    for word in line.split(' '):
        pos = get_pos(word)
        val = pos if pos and word not in pattern_words else word
        new_line.append(val)
    line = ' '.join(new_line)
    return line

def find_pattern(original, line, pattern):
    found_phrases = []
    original_split = original.split(' ')
    # phrases = TextBlob(line).noun_phrases
    if pattern in line:
        ''' replace pattern with pos so each pos in pattern is only taking up one item in line.split(' ') '''
        line_split = line.split(pattern)
        print('line_split', line_split, pattern)
        for i, phrase in enumerate(line_split):
            words = phrase.split(' ')
            if i < (len(line_split) - 1):
                new_pattern = []
                for j in range(0, len(pattern.split(' '))):
                    pattern_index = len(words) + j - 1
                    if pattern_index < len(original_split):
                        new_pattern.append(original_split[pattern_index])
                found_phrases.append(' '.join(new_pattern))            
    if len(found_phrases) > 0:
        return found_phrases, pattern
    return False, False

def get_pattern_stack(line):
    line = line.replace('\n','').replace('.', '')
    original = line
    pattern_stack = {}
    pos_line = convert_to_pattern_format(line)
    for pattern in patterns:
        found, adjusted_pattern = find_pattern(original, pos_line, pattern)
        if found:
            if adjusted_pattern not in pattern_stack:
                pattern_stack[adjusted_pattern] = found
            else:
                pattern_stack[adjusted_pattern].extend(found)
    return pattern_stack

def concatenate_species(data):
    data_lines = data.split('.')
    new_lines = []
    next_item = None
    for i, d in enumerate(data_lines):
        d_split = d.split(' ')
        last_item = d_split.pop()
        if len(last_item) == 1:
            if (i + 1) < len(d):
                prev_item = d_split[-1]
                if len(prev_item) > 1:
                    next_item = data_lines[i+1].strip().split(' ')[0]
                    d_next = '.'.join([last_item, next_item])
                    d_split.append(d_next)
                    new_lines.append(' '.join(d_split))
        else:
            next_item = None
            new_lines.append(' '.join(d_split))
        if next_item is not None:
            next_item_len = len(next_item)
            if next_item == d[0:next_item_len]:
                d = ' '.join(d[next_item_len:].split(' '))
                new_lines.append(d)
    data = '.'.join(new_lines)
    return data

def get_structural_metadata(line, data_words, data, metadata):
    '''
    to do: exclude places 'Michigan' & common nouns 'Medical Center'
    '''
    processed_data = data.lower().replace('"', '').replace("'",'').replace(',','').replace('(','').replace(')','').replace('[','').replace(']','')
    name_line = line.replace('"', '').replace("'",'').replace('(','').replace(')','').replace('[','').replace(']','')
    name_tagged = pos_tag(word_tokenize(name_line))
    line = line.replace('"', '').replace(',','').replace('(','').replace(')','').replace('[','').replace(']','')
    pattern_stack = get_pattern_stack(line)
    if len(pattern_stack.keys()) > 0:
        for key, val in pattern_stack.items():
            if key not in metadata['pattern_stack']:
                metadata['pattern_stack'][key] = val
            else:
                metadata['pattern_stack'][key].extend(val)
    tagged = pos_tag(word_tokenize(line))
    for p in TextBlob(name_line).noun_phrases:
        if len(p) > 0:
            new_name = []
            phrase_words = p.split(' ')
            for name in phrase_words:
                pos = [item[1] for item in tagged if item[0].lower() == name]
                if len(pos) > 0:
                    pos_item = pos[0]
                    stem = stemmer.stem(name)
                    stem_pos = [item[1] for item in pos_tag(word_tokenize(stem)) if stemmer.stem(item[0].lower()) == stem]
                    if len(stem_pos) > 0 and stem_pos != pos_item and stem not in stop and stem_pos in common_noun_pos:
                        metadata['nouns'].add(stem)
                    elif len(stem_pos) > 0 and stem_pos != pos_item and stem not in stop and stem_pos in verb_pos:
                        metadata['verbs'].add(stem)
                    elif name not in stop:
                        if pos_item in verb_pos:
                            metadata['verbs'].add(name)
                        elif pos_item in common_noun_pos:
                            ''' check if the noun stem is a verb, if so add it to verbs
                            # using verb_versions adds a lot of nouns like worm & rat to the verbs list
                            verb_suffixes = ['e', 'd', 'ed'] 
                            verb_versions = [pos_tag(word_tokenize(''.join([name, v]))) for v in verb_suffixes] # append verb affixes and check if its a verb
                            '''
                            metadata['nouns'].add(name)
                        elif pos_item == 'NNP':
                            name = ''.join([name[0].upper(), name[1:]]) if '.' not in name and '/' not in name else name.upper()
                            new_name.append(name)  
                        elif pos_item == 'NNS':
                            name = ''.join([name[0].upper(), name[1:]])
                            if name in data:
                                new_name.append(name)
                        else:
                            metadata['taken_out'].add('_'.join([name, pos_item[1]]))
            if len(new_name) > 0:                                         
                final_name = ' '.join(new_name)
                if len(new_name) == len(phrase_words) and final_name != data_words[0] and final_name.lower() not in metadata['nouns'] and final_name.lower() not in metadata['verbs']:
                    metadata['names'].add(final_name) # find names and store separately
                    line = line.replace(final_name, '')
    tagged = pos_tag(word_tokenize(line)) # line without names
    for item in tagged:
        if len(item) == 2:
            w = item[0].lower()
            if item[1] in leave_in_pos:
                if len(w) > 0 and w not in stop:
                    w_upper = w.upper()
                    w_name = ''.join([w[0].upper(), w[1:]])
                    upper_count = data_words.count(w_upper) # find acronyms, ignoring punctuated acronym
                    count = processed_data.count(w)
                    ## and w not in verbs and w not in nouns and w_name not in ' '.join(names):
                    if item[0] == w_name and w_name != data_words[0] and w_name not in ' '.join(metadata['names']): # exclude first word in sentence
                        if upper_count > 0 and upper_count <= count:
                            if upper_count not in metadata['counts']:
                                metadata['counts'][upper_count] = set()
                            metadata['counts'][upper_count].add(w_upper)
                        else:
                            if count > 0:
                                if count not in metadata['counts']:
                                    metadata['counts'][count] = set()
                                metadata['counts'][count].add(w)
    for p in TextBlob(line).noun_phrases:
        if len(p) > 0:
            phrase_words = p.split(' ')
            for n in phrase_words:
                new_p = set()
                p_name = '***'.join([n[0].upper(), n[1:]])
                for name in metadata['names']:
                    if name not in p_name:
                        new_p.add(n)
                p = ' '.join(new_p)
            if len(p.strip()) > 0:
                pos = [item[1] for item in tagged if item[0].lower() == phrase_words[0]]
                if pos not in verb_pos and p not in metadata['verbs'] and p not in metadata['nouns'] and p_name not in ' '.join(metadata['names']) and p not in stop:
                    p_upper = p.upper()
                    upper_count = data_words.count(p_upper) # find acronyms
                    phrase_count = processed_data.count(p)
                    p = p_upper if upper_count > 0 and len(p_upper) > 0 and upper_count < phrase_count else p
                    count = upper_count if upper_count > 0 and len(p_upper) > 0 and upper_count < phrase_count else phrase_count
                    if count not in metadata['phrases']:
                        metadata['phrases'][count] = set()
                    metadata['phrases'][count].add(p)
    return metadata

'''
counts {
     1: {'science', 'beyond'},
     2: {'university'},
     11: {'insulin'},
     5: {'said'}
}
phrases {
     3: {'elegans', 'pi3k/akt', 'likely', 'm.d'},
     1: {'pathways', 'systems', 'broader', 'variants', 'processing', 'synthesis', 'imbalances', 'besides', 'strategies', 'drugs', 'therapies'},
     2: {'ways', 'molecules', 'components', 'worms'},
     7: {'cells'},
     4: {'diseases', 'proteins'}
}
verbs {'responses', 'maintaining', 'fold', 'contributes', 'understanding', 'exists', 'deleting', 'corresponding', 'screen'}
nouns {
    'researcher', 'total', 'sclerosis', 'proper', 'stress', 'parent', 'abnormal', 'phenotype', 'disease', 'human', 'chaperone', 'convenient', 'protein', 'professor', 'pancreatic', 'rat', 'genetic', 'amyotrophic', 
    'percent', 'insulin', 'reticulum', 'biogenesis', 'content', 'new', 'role', 'homeostasis', 'mammalian', 'health', 'contribution', 'Trap-alpha', 'model', 'associate', 'worm', 'pathway', 'research', 'expression', 
    'cancer', 'beta', 'endoplasmic', 'cell', 'response', 'gene', 'insulin-like', 'system', 'cellular', 'oncology', 'nematode', 'lateral', 'growth', 'factor', 'anti-tumor', 'unexpected', 'neurodegenerative', 'reduction', 
    'approach', 'culture', 'primordial', 'common', 'perspective'
}
names {'Caenorhabditis', 'Medical Center', 'Advances', 'Er', 'Hu', 'Peter Arvan', 'Vanderbilt', 'Alzheimers', 'PI3K/AKT', 'Michigan', 'M.D', 'Patrick Hu', 'Trap-alpha', 'Ming Liu'}
taken_out [
    'therapies_N', 'drugs_N', 'strategies_N', 'pathways_N', 'components_N', 'elegans_N', 'worms_N', 'systems_N', 'variants_N', 'cells_N', 'cells_N', 'molecules_N', 'cells_N', 'proteins_N', 'proteins_N', 
    'were_R', 'likely_B', 'imbalances_N', 'diseases_N', 'molecules_N', 'besides_N', 'broader_J', 'ways_N'
]
pattern stack [
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['understanding of type']}, 
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['professor of medicine']}, 
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['University of Michigan']}, 
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['molecules of insulin']}, 
    {'[NN || NNP || NNS || JJ || JJR] of [NN || NNP || NNS || JJ || JJR]': ['expression of chaperone']}
]
'''

pattern_categories = {
    'types': [
        '<adjective> <noun>'
    ],
    'roles': [
        '<adverb> || <verb> <noun>',
        '<noun> of <noun>',
        '<verb> || <noun> role',
        'functions/works/operates/interacts/acts as (a) <verb> || <noun>'
    ],
    'noun': [
        'the <noun>'
    ]
}

''' important note: always put the extended pattern first
    if you put '<noun>' before "<noun> <noun>',
        you'll miss phrases like 'compound acid' returning matches like:
             ['compound acid']
        and will instead get matches for the '<noun>' pattern:
            ['compound', 'acid']
        so make sure thats what you want before ignoring this rule
'''

''' () indicates an optional item, --a b c-- indicates a set of alternatives '''
language_patterns = [
    '<adjective> <noun>',
    '--<adverb> <verb>-- <noun>',
    '<noun> of <noun> <noun>',
    '<noun> of <noun>',
    '--<verb> <noun>-- role',
    '--functions works operates interacts acts-- as (a) --<verb> <noun>--'
]
language_pos_map = {
    '<adjective>': '[ADJ]',
    '<noun>': '[NN||NNP||NNS||JJ||JJR]',
    '<adverb>': '[ADV]',
    '<verb>': '[VB||VBP||VBD||VBG||VBN||VBZ]'
}

patterns = convert_patterns(language_patterns)
print('patterns', patterns)
pattern_words = ['of', 'acts', 'as']
leave_in_pos = ['NNP', 'NNS', 'JJR'] # JJR example: 'broader'
common_noun_pos = ['JJ', 'NN']
noun_pos = ['NN', 'NNP', 'NNS', 'JJ', 'JJR']
verb_pos = ['VB', 'VBP', 'VBD', 'VBG', 'VBN', 'VBZ']
stemmer = SnowballStemmer("english")  
stop = set(stopwords.words('english'))
metadata = {
    'counts': {},
    'phrases': {},
    'pattern_stack': {},
    'taken_out': set(),
    'patterns': [],
    'names': set(),
    'verbs': set(),
    'nouns': set()
}
data = None
with open('article.txt', 'r') as f:
    data = f.read()
    f.close()
if data:
    data = concatenate_species(data)
    data_words = data.split('\n')
    for line in data_words:
        if len(line.strip()) > 0:
            metadata = get_structural_metadata(line, data_words, data, metadata)
    print('counts', metadata['counts'])
    print('phrases', metadata['phrases'])
    print('pattern stack', metadata['pattern_stack'])
    print('verbs', metadata['verbs'])
    print('nouns', metadata['nouns'])
    print('names', metadata['names'])
    print('taken_out', metadata['taken_out'])
