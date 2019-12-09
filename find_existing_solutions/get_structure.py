from nltk import word_tokenize, pos_tag
from textblob import TextBlob, Word
from textblob.wordnet import VERB, NOUN, ADJ, ADV
from textblob.wordnet import Synset

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

from utils import *
from get_vars import get_vars

''' important note for pattern definitions in get_vars:
    - always put the extended pattern first
    - if you put '<noun>' before "<noun> <noun>',
        you'll miss phrases like 'compound acid' returning matches like:
             ['compound acid']
        and will instead get matches for the '<noun>' pattern:
            ['compound', 'acid']
        so make sure thats what you want before ignoring this rule
        
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

def find_pattern(original, line, pattern):
    found_phrases = []
    original_split = original.split(' ')
    if pattern in line:
        ''' replace pattern with pos so each pos in pattern is only taking up one item in line.split(' ') '''
        line_split = line.split(pattern)
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

def get_pattern_stack(line, all_vars):
    line = line.replace('\n','').replace('.', '')
    original = line
    pattern_stack = {}
    pos_line = convert_to_pattern_format(line)
    for pattern in all_vars['patterns']:
        found, adjusted_pattern = find_pattern(original, pos_line, pattern)
        if found:
            if adjusted_pattern not in pattern_stack:
                pattern_stack[adjusted_pattern] = found
            else:
                pattern_stack[adjusted_pattern].extend(found)
    return pattern_stack

def convert_to_pattern_format(line):
    new_line = []
    for word in line.split(' '):
        pos = get_pos(word)
        val = pos if pos else word # to do: restrict by pattern_words
        new_line.append(val)
    line = ' '.join(new_line)
    return line

def get_pos(word):
    noun_pos = ['NN', 'NNP', 'NNS', 'JJ', 'JJR']
    verb_pos = ['VB', 'VBP', 'VBD', 'VBG', 'VBN', 'VBZ']
    exclude = ['DT', 'WRB', 'TO', 'CC', 'IN']
    noun_string = 'noun'
    verb_string = 'verb'
    if len(word) > 0:
        pos = [item[1] for item in pos_tag(word_tokenize(word)) if item[0].lower() == word]
        if (len(pos) > 0 and pos[0] in noun_pos):
            return noun_string
        elif (len(pos) > 0 and pos[0] in verb_pos):
            return verb_string
        else:
            noun_synsets = Word(word).get_synsets(pos=NOUN)
            if len(noun_synsets) > 0:
                return noun_string
            verb_synsets = Word(word).get_synsets(pos=VERB)
            if len(verb_synsets) > 0:
                return verb_string
            else:
                stem = stemmer.stem(word)
                stem_pos = [item[1] for item in pos_tag(word_tokenize(stem)) if item[0].lower() == stem]
                if len(stem_pos) > 0:
                    if stem_pos[0] in noun_pos:
                        return noun_string
                    elif stem_pos[0] in verb_pos:
                        return verb_string
                noun_stem_synsets = Word(stem).get_synsets(pos=NOUN)
                if len(noun_stem_synsets) > 0:
                    return noun_string
                verb_stem_synsets = Word(stem).get_synsets(pos=VERB)
                if len(verb_stem_synsets) > 0:
                    return verb_string
        if len(pos) > 0:
            if pos[0] not in exclude:
                print('get_pos: unknown word', word, pos)
    return False

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
                    d_next = '-'.join([last_item, next_item]) #C. elegans => C-elegans
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

def get_counts(article_words, processed_data, tagged, line, row):
    object_pos = ['NNP', 'NNS', 'JJR']
    for item in tagged:
        w = item[0].lower()
        if item[1] in object_pos:
            if len(w) > 0 and w not in stop:
                w_upper = w.upper()
                w_name = ''.join([w[0].upper(), w[1:]])
                upper_count = article_words.count(w_upper) # find acronyms, ignoring punctuated acronym
                count = processed_data.count(w)
                ## and w not in verbs and w not in nouns and w_name not in ' '.join(names):
                if item[0] == w_name and w_name != article_words[0] and w_name not in ' '.join(row['names']): # exclude first word in sentence
                    if upper_count > 0 and upper_count <= count:
                        if upper_count not in row['counts']:
                            row['counts'][upper_count] = set()
                        row['counts'][upper_count].add(w_upper)
                    else:
                        if count > 0:
                            if count not in row['counts']:
                                row['counts'][count] = set()
                            row['counts'][count].add(w)
    if len(row['counts']) > 0:
        common_words = get_most_common_words(row['counts'], 3) # get top 3 tiers of common words
        if common_words:
            row['common_words'] = row['common_words'].union(common_words)
    return row

def get_names(article_words, line, row):
    line = line.replace("'",'')
    tagged = pos_tag(word_tokenize(line))
    for p in row['phrases']:
        if len(p) > 0:
            new_name = []
            phrase_words = p.split(' ')
            for name in phrase_words:
                pos = [item[1] for item in tagged if item[0].lower() == name]
                if len(pos) > 0:
                    pos_item = pos[0]
                    if name not in stop:
                        if pos_item == 'NNP':
                            name = ''.join([name[0].upper(), name[1:]]) if '.' not in name and '/' not in name else name.upper()
                            new_name.append(name)  
                        elif pos_item == 'NNS':
                            name = ''.join([name[0].upper(), name[1:]])
                            if name in '\n'.join(article_words):
                                new_name.append(name)
            if len(new_name) > 0:                                         
                final_name = ' '.join(new_name)
                if len(new_name) == len(phrase_words) and final_name != line[0:len(final_name)] and final_name.lower() not in row['nouns'] and final_name.lower() not in row['verbs']:
                    row['names'].add(final_name) # find names and store separately
    return row

def get_clauses(line, row, all_vars):
    '''
    to do: 
    - add logic for other phrase types than 'noun-noun', like verb_phrases
    - clauses are relationships between subject and objects in line
    - the response object should be a list of the acting subject, verb, & object:
        row['clauses'] = ['chemical', 'caused', 'reaction'], ['experiment', 'was', 'successful']]

    active: x  || did  ||  this and then y  ||  did  ||  z
    passive: this  ||  was done  ||  by x and then z  ||  was done  ||  by y

    '''
    line = rearrange_sentence(line)
    active = get_active(line)
    sentence_pieces = [] # break up sentence by verbs
    sentence_piece = []
    for w in line.split(' '):
        if w not in row['verbs']:
            sentence_piece.append(w)
        else:
            sentence_pieces.append(' '.join(sentence_piece))
            sentence_pieces.append(w) # add the verb separately
            sentence_piece = []
    for j, s in enumerate(sentence_pieces):
        s_split = s.split(' ') if type(s) == str else s
        for i, word in enumerate(s_split):
            if word in row['verbs']:
                prev_object = False if i < 1 else get_object_by_position(i, s_split, 'prev', row['nouns'], row['phrases'])
                prev_object = sentence_pieces[j - 1] if prev_object is False and j > 0 else prev_object
                next_object = False if i == (len(sentence_pieces) - 1) else get_object_by_position(i, s_split, 'next', row['nouns'], row['phrases'])
                next_object = sentence_pieces[j + 1] if next_object is False and j < (len(sentence_pieces) - 1) else next_object
                if active:
                    if prev_object:
                        row['subjects'].add(prev_object)
                        if next_object:
                            row['clauses'].add(' '.join([prev_object, word, next_object]))
                else:
                    active_s = change_to_infinitive(word)
                    active_s = 'was' if active_s == 'be' else active_s # to do: handle other cases where infinitive is linguistically awkward bc clauses will be re-used later
                    if next_object:
                        row['subjects'].add(next_object)
                        if prev_object:
                            row['clauses'].add(' '.join([next_object, active_s, prev_object]))
    return row 

def get_pos_in_line(line, row):
    pattern_format_line = convert_to_pattern_format(line)
    split_line = line.split(' ')
    print('pattern_format_line', pattern_format_line)
    for index, p in enumerate(pattern_format_line.split(' ')):
        if len(p) > 0:
            word = split_line[index]
            if p == 'verb':
                row['verbs'].add(word)
                row['functions'].add(word)
                # relationships = treatments, intents, functions, insights, strategies, mechanisms, patterns, systems
            elif p == 'noun':
                ''' check if the noun stem is a verb, if so add it to verbs
                    # using verb_versions adds a lot of nouns like worm & rat to the verbs list
                    verb_suffixes = ['e', 'd', 'ed'] 
                    verb_versions = [pos_tag(word_tokenize(''.join([p, v]))) for v in verb_suffixes]
                '''
                row['nouns'].add(word)
                row['components'].add(word) 
                # compounds, symptoms, treatments, metrics, conditions, stressors, types, variables
            else:
                row['taken_out'].add('_'.join([split_line[index], p]))
    return row

def get_similarity_to_title(string, title):
    string_split = string.split(' ')
    title_split = title.split(' ')
    both = set()
    similarity = {}
    for s in string_split:
        if s in title_split:
            both.add(s)
    if len(both) > 0:
        key = (len(both) / len(title))
        similarity[string] = key
        return similarity
    return False

def get_most_common_words(counts, top_index):
    '''
    given counts which is structured like:
    counts = {
        0: ['words', 'that', 'appeared', 'once'],
        1: ['items', 'shown', 'twice']
    }
    '''
    count_keys = counts.keys()
    if len(counts.keys()) > 0:
        sorted_keys = reversed(sorted(count_keys))
        max_key = max(counts.keys())
        retrieved_index = 0
        max_words = []
        for k in sorted_keys:
            max_words.extend(counts[k])
            retrieved_index += 1
            if retrieved_index == top_index:
                return max_words
        if len(max_words) > 0:
            return max_words
    return False

def get_structural_metadata(line, title, article_words, article_string, index, row, metadata_keys, all_vars):
    line = replace_contractions(line, all_vars)
    line = remove_standard_punctuation(line)
    # line = line.replace(',','')
    similarity = get_similarity_to_title(line, title)
    if similarity:
        for line, score in similarity.items():
            if line not in row['title_similarities']:
                row['title_similarities'][line] = score
    pattern_stack = get_pattern_stack(line, all_vars)
    if pattern_stack:
        for key, val in pattern_stack.items():
            if key not in row['pattern_stack']:
                row['pattern_stack'][key] = val
            else:
                row['pattern_stack'][key].extend(val)
    row = get_pos_in_line(line, row)
    phrases = TextBlob(line).noun_phrases
    if len(phrases) > 0:
        row['phrases'] = phrases
    row = get_names(article_string, line, row)
    # line = remove_names(line, row['names'])
    row = get_clauses(line, row, all_vars)
    tagged = pos_tag(word_tokenize(line))
    processed_data = article_string.replace("'",'').replace(',','')
    row = get_counts(article_words, processed_data, tagged, line, row)
    for key in row:
        if key in index:
            if type(index[key]) == set:
                index[key] = index[key].union(row[key])
            elif type(index[key]) == dict:
                for k, v in row[key].items():
                    if k in index[key]:
                        index[key][k] = index[key][k].union(v)
                    else:
                        index[key][k] = set(v)
    return index, row

def replace_mappings(lines):
    article = '\n'.join(lines)
    article_words = article.split(' ')
    replacement_map = all_vars['supported_core']['replacement']
    for k, v in replacement_map.items():
        for word_to_replace in v:
            if word_to_replace in article_words:
                    article = article.replace(word_to_replace, k)
    return article.split('\n')

def get_active(line):
    ''' check for verb tenses normally used in passive sentences 
    VBD: Verb, past tense #thought, did, gave
    VBG: Verb, gerund or present participle #thinking, doing, giving
    VBN: Verb, past participle #had thought, had done, had given
    VBP: Verb, non-3rd person singular present 
    VBZ: Verb, 3rd person singular present
    # had been done = past perfect

    test cases:
    pattern = "A were subjected to B induced by C of D"
    pattern_with_pos = "A were subjected to B induced by C of D"
    - "Rats were subjected to liver damage induced by intra-peritoneal injection of thioacetamide" => 
        "intra-peritoneal thioacetamide injection induced liver damage in rats"
        noun_phrases for this would be "intra-peritoneal thioacetamide injection", "liver damage" and "rats"
    - "chalcone isolated from Boesenbergia rotunda rhizomes" => "Boesenbergia rotunda rhizomes isolate chalcone"

    keep in mind:
        if you standardize "injection of thioacetamide" to "thioacetamide injection", 
        your other pattern configuration wont work, so either 
        add more patterns, change the pattern, or apply pattern function before this one

    '''
    passive_patterns = [
        '[was had has] [been done] past_participle [to by]',
        '[noun verb] of [noun verb]'
    ]
    formatted_line = convert_to_pattern_format(line)
    passive = 0
    for p in passive_patterns:
        keywords_found = [True for x in passive_keywords if x in line]
        found = find_pattern(line, formatted_line, p)
        if found:
            passive += 1
        passive += len(keywords_found)
    if passive > 2:
        return False
    return True

def replace_contractions(line, all_vars):
    contractions = all_vars['supported_core']['replacement']['contraction']
    line = line.replace("'",'')
    new_line = []
    for w in line.split(' '):
        if w in contractions:
            new_line.append(contractions[w])
        else:
            new_line.append(w)
    line = ' '.join(new_line)
    return line

def get_phrase_with_word(word, phrases, line):
    phrase_string = ' '.join(phrases)
    if word in phrase_string:
        for phrase in phrases:
            '''
            p_pos = line.find(phrase)
            word_pos = line.find(word)
            if word_pos >= p_pos:
            '''
            for i, phrase_word in enumerate(phrase.split(' ')):
                if phrase_word == word and i == 0:
                    ''' this is the first word in a phrase so get the whole phrase '''
                    return phrase
    return False

def get_object_by_position(index, sentence_pieces, position, check_list, phrases):
    relevant_piece = sentence_pieces[index - 1] if position == 'prev' else sentence_pieces[index + 1] if index < (len(sentence_pieces) - 1) else ''
    if relevant_piece != '':
        sequenced_words = relevant_piece.split(' ') if position == 'next' else relevant_piece.split(' ').reverse()
        for w in sequenced_words:
            found = get_phrase_with_word(w, phrases, line)
            if found:
                return found
            elif w in check_list: # check that its in the noun list passed in before returning it as an object
                return w
    return False

'''
structural metadata example output:

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
names {'Caenorhabditis', 'Medical Center', 'Advances', 'Er', 'Vanderbilt', 'Alzheimers', 'PI3K/AKT', 'Michigan', 'M.D', 'Trap-alpha'}
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

'''
all_vars = get_vars()
article_string = read('article.txt')
if article_string:
    article_string = concatenate_species(article_string)
    article_words = article_string.split('\n')
    title = article_words[0]
    for line in article_words:
        if len(line.strip()) > 0:
            empty_index = get_empty_def(metadata, all_vars['supported_params'])
            metadata = get_structural_metadata(line, title, article_words, article_string, empty_index, empty_index, 'all')
            for key in metadata:
                print(key, metadata[key])
'''