from nltk.stem.snowball import SnowballStemmer
from itertools import combinations

stemmer = SnowballStemmer("english")

''' related to this workflow, identify 'iterated interface structures' that fulfill high-level functions like 'determine' or 'organize'
    - identifying errors like 'incompleteness/inaccuracy' in a useful structure like a 'network of determining variables' which are useful to identify 'optimization opportunities' with 'identifiable optimizations' ('determining variables' have enough structure to be identifiable and for their optimizations and interaction optimizations to be identifiable')
        - for example, identifying an 'interaction network of determining variables' is useful to identify their structures like 'switching/coordination interaction functions, their variants and variables, their equivalents/opposites, and the systems that support the most determining variables' (which can be determined by the most variables that are the most powerful as in 'creating extreme changes from trivial inputs', supporting the most variation)
        - determining variables can take many forms like:
             'whichever agent arrives at a position first with more resources than a threshold value' or a 'function that, when applied in a specific pattern/position, determines what other functions can be used' a 'repeatable unit that, when iterated, determines the rest of the system' or a 'variable that, when present, overrides all other variable sets' or a 'variable that simplifies a structure enough to be the only relevant variable to identify so its used in all future calculations' or a 'limiting variable that determines when other variables stop/end' or a 'variable that changes all other variables' (which are specific cases that can vary, as theyre 'incomplete specifications of determining variables', since a 'variable that changes all other variables' might not be a determining variable in a case like 'if there are other more determining variables')
        - relatedly, there are only so many interface structures like 'sub-problems described by interface structure combinations' that are necessary to describe a sufficiently specific implementation of high-level functions like 'describe/determine/differentiate/organize/standardize', so generating these and filtering them by grouping them into this relatively trivial set is useful/trivial
'''
 
intents = ['determine'] #'organize', 'describe']
interface_structures = {
    'structure': ['variable', 'limit', 'network', 'index', 'cycle', 'degree', 'subset', 'base', 'position', 'size', 'scale', 'distance', 'direction', 'interim', 'embedding', 'sequence', 'directness', 'starting point', 'end point', 'average', 'range', 'ratio', 'threshold'],
    'interface': ['cause', 'concept', 'standard', 'interface', 'format', 'independence'],
    'concept': ['power', 'balance', 'energy', 'type'],
    'workflow': ['iterate all possibilities', 'change a base solution'],
    'errors': ['barrier', 'gap', 'hidden', 'missing/lack', 'excess','incomplete', 'compared to other structures/functions', 'compared to other solutions', 'compared to intents', 'compared to solution metrics', 'compared to errors'],
    'core_interaction_functions': ['filter', 'reduce', 'connect', 'apply', 'generate', 'identify', 'iterate', 'interfere', 'overlap', 'intersect', 'interact', 'reverse', 'recurse', 'simple', 'complex', 'abstract', 'specific', 'maintain'],
    'system': ['state', 'mode', 'phase', 'condition', 'context'],
    'change': ['similarity', 'adjacency', 'symmetry', 'difference', 'change', 'alternate'],
    'meaning': ['useful', 'relevant', 'valid', 'meaningful', 'use', 'meaning', 'definition', 'example'],
    'potential': ['possibility', 'probability', 'entropy'],
    'function': ['input', 'output', 'volatility', 'accuracy'],
    'problem/solution': ['error', 'optimization', 'solution', 'optimality', 'cost', 'benefit', 'solution metric', 'useful metric'],
}
all_interface_structures = [v for k, vals in interface_structures.items() for v in vals]
connections = ['to', 'of', 'for', 'as', 'in', 'on']
changes = ['ify', 'ification', 'ly']
max_iterations = 5
filtered_structures = {k: [] for k in intents}
iterated_interface_structures = set()
abstract_definitions_to_filter_implementations_with = {
    'determine': ['when this variable is applied, the rest of the adjacent variables change'],
}

def generate_iterated_interface_structures():
    for i in range(2, max_iterations):
        # generate all possible sets of interface structures having count i
        # to do: filter to use only cross-interface structures
        # to do: filter to be valid and use only cross-interface structures or include a concept/function
        iterated_interface_structures.update([' '.join(c) for c in combinations(all_interface_structures, i)])
    return iterated_interface_structures

def filter_intent(intent):
    structures_found = []
    definitions = abstract_definitions_to_filter_implementations_with[intent]
    for item in iterated_interface_structures:
        for definition in definitions:
            if similar(item, definition):
                structures_found.append(item)
    return structures_found

def similar(item, definition):
    # check if a generated item like 'similarity adjacency' could possibly fulfill the definition above for the 'determine' function
    # by checking for a similarity in interface structures like 'similar functions/variables/inputs/outputs'
    item_words = item.split(' ')
    definition_words = definition.split(' ')
    nouns = ['tion', 'ty', 'cy']
    item_verbs = [word for word in item_words if len([n for n in nouns if word[len(word)-len(n):] == n]) == 0]
    definition_verbs = [word for word in definition_words if len([n for n in nouns if word[len(word)-len(n):] == n]) == 0]
    item_nouns = [word for word in item_words if word not in item_verbs]
    definition_nouns = [word for word in definition_words if word not in definition_verbs]
    item_mid_index = round(len(item_words) / 2)
    definition_mid_index = round(len(definition_words) / 2)
    item_inputs = item_words[0:item_mid_index]
    definition_inputs = definition_words[0:definition_mid_index]
    item_outputs = item_words[item_mid_index:]
    definition_outputs = definition_words[definition_mid_index:]
    item_functions = item_verbs
    definition_functions = definition_verbs
    item_variables = item_nouns
    definition_variables = definition_nouns
    for item_list in [[item_inputs, definition_inputs], [item_outputs, definition_outputs], [item_functions, definition_functions], [item_variables, definition_variables]]:
        if len(item_list[0]) > 0 and len(item_list[1]) > 0:
            if more_similar_than_different(item_list[0], item_list[1]):
                return True
    return False

def similar_words_in_common(base_usage, compare_usage):
    common_words = [word for word in base_usage.split(' ') if word in compare_usage]
    if len(common_words) / len(base_usage.split(' ')) > 0.6:
        return True
    return False

def find_similar_roots(base, compare):
    base_roots = [stemmer.stem(word) for word in base.split(' ')]
    compare_roots = [stemmer.stem(word) for word in compare.split(' ')]
    common_roots = [root for root in base_roots if root in compare_roots]
    if len(common_roots) / len(base.split(' ')) > 0.6:
        return common_roots
    return []

def find_similar_nonroots(base, compare, roots):
    base_nonroots = []
    compare_nonroots = []
    for word in base.split(' '):
        word_root = stemmer.stem(word)
        if word_root is not None and word_root != word:
            word_without_root = word.replace(word_root, '').strip()
            if len(word_without_root) > 0:
                base_nonroots.append(word_without_root)
        else:
            base_nonroots.append(word)
    for word in compare.split(' '):
        word_root = stemmer.stem(word)
        if word_root is not None and word_root != word:
            word_without_root = word.replace(word_root, '').strip()
            if len(word_without_root) > 0:
                compare_nonroots.append(word_without_root)
        else:
            compare_nonroots.append(word)
    common_nonroots = [nonroot for nonroot in base_nonroots if nonroot in compare_nonroots]
    if len(common_nonroots) / len(base) > 0.6:
        return True
    return False

def more_similar_than_different(base_list, compare_list):
    base = ' '.join(base_list)
    compare = ' '.join(compare_list)
    same_interface = False 
    similar_relevant_subsets = False
    same_usages = []
    usages = {base: [], compare: []}
    for interface, examples in interface_structures.items():
        if base in examples and compare in examples:
            same_interface = True
    with open('examples_of_implementation_methods.md', 'r') as f:
        for i, line in enumerate(f.readlines()):
            if i < 1000:
                line_words = line.split(' ')
                for item in [base, compare]:
                    if item in line:
                        index = line.index(item)
                        usage = ' '.join(line[index - 5: index + 5])
                        new_usage = ' '.join([word for word in usage.split(' ') if word in line_words])
                        usages[item].append(new_usage)
                        if len(usages[item]) > 4 and len(usages[compare]) > 4:
                            break
    for base_usage in usages[base]:
        for compare_usage in usages[compare]:
            if similar_words_in_common(base_usage, compare_usage):
                same_usages.append('_'.join([base_usage, compare_usage]))
    similar_roots = find_similar_roots(base, compare)
    similar_structures = find_similar_nonroots(base, compare, similar_roots)
    if similar_roots or similar_structures:
        similar_relevant_subsets = True
    if len(same_usages) > 3 or same_interface or similar_words_in_common(base, compare):
        return True
    return False

# test cases
specific_structures_implementing_definitions = {
    'determine': ['powerful variables', 'variable-changing variable', 'multi-functional, multi-modal structures', 'causative variables', 'repeatable units that cover a structure']
}
generate_iterated_interface_structures()
# filter to implement intent
for intent in intents:
    filtered_structures[intent] = filter_intent(intent)
    print('filtered_structures', intent, filtered_structures[intent])

# to do: compared filtered_structures for each intent with the test values in specific_structures_implementing_definitions for that intent