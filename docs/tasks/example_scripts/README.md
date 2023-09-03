
NAME: Possible Treatment Finder


PURPOSE: 

This script helps find possible treatments for a condition, 
by compiling a list of nouns mentioned in research studies for a given search like 'meningitis treatment', 
as these nouns could be possible treatments studied recently

1. run a search on pubmed for the condition (like 'meningitis treatment') so you're at a url with your search terms in it 
	- example: https://pubmed.ncbi.nlm.nih.gov/?term=meningitis%20treatment
2. then click the Save button, select 'All results' and 'Pubmed format'
3. move the downloaded file to the same directory as the script
4. change the variables 'condition' and 'known_treatments' and 'terms_to_exclude' to values that you want to check for or exclude from possible_treatments
    - changing 'condition' to reflect the search you used will exclude it from the list of possible treatments found
    - changing 'known_treatments' to reflect substances that you want to find similar substances to can sometimes find similar treatments based on sentence context (usage of the word).
    - changing 'terms_to_exclude' to remove any words from list of treatments found, otherwise it will use the condition words to remove the condition from treatments found.
        terms_to_exclude = ['biology', 'exclude-this'] 
5. A. run the script:
Example run like 'python3 parse_pubmed_download.py condition known_treatments terms_to_exclude'
``` python3 parse_pubmed_download.py -c 'fungal treatment' -k 'sitosterol, fluconazole, citicoline, eugenol' -t 'biology' ```
I recommend not including a 'term to exclude' at all until youve viewed the output and know what you want to exclude, otherwise you could easily end up excluding treatments.

5. B. run the script like this if you want to store the errors and other messages it creates in a file rather than just showing them in the terminal window:
``` python3 parse_pubmed_download.py -c 'fungal treatment' -k 'sitosterol, fluconazole, citicoline, eugenol' -t 'biology' > output.txt ```
You'll have to change the name of the output.txt file each time to save the output from different scripts.


INSTALLATION: 

- install primary libraries
	pip3 install nltk scispacy spacy PyDictionary
- install the scispacy entity recognition model (which can identify a compound/organism/antibody/etc)
	pip3 install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.0/en_core_sci_sm-0.2.0.tar.gz
- use spacy validate to check for updates & update en_core_web_sm accordingly
	- python3 -m spacy validate
	- python -m spacy download en_core_sci_sm

- install errors like 'package not found' 
	- run "pip3 install packagename" of the package that is not installed, when you run the python3 parse_pubmed_download.py command and it says you didnt install some package.


NOTES:

- the script can take up to seveeral hours to run on 10,000 search results bc of all the processing I added recently.


EXAMPLE OUTPUT AND ERRORS

- for 'cancer treatment' Pubmed search results, this script included 'selenium', 'limonene', 'saffron', 'linalool', 'astragalus', 'lactoferrin', 'fucose', 'lysine', 'withaferin', 'dendritic cell vaccines', 'checkpoint inhibitors', 'VSV (an oncolytic virus)' in its results, their interaction with cancer being useful to know about

	- other anti-tumor substances identified in research (having various mechanisms of action like inhibiting vimentin, inducing apoptosis, suppressing growth factors, suppressing pro-inflammatory interleukins, upregulating interleukin-12, lowering inflammation, lowering LDL cholesterol, etc)
	    - dendritic cell vaccines, checkpoint inhibitors, VSV (an oncolytic virus), linalool, fucose, lysine, ashwagandha/Withaferin or ginsenosides (a similar compound), atorvastatin, melatonin, cilantro, ginger, coffee, green tea, lactobacillus, bacillus subtilis, milk thistle, chicory, turmeric, astragalus, pterostilbene/resveratrol, boswellia, selenium, ahcc (shiitake mushroom), mushrooms (reishi, maitake, turkey tail), mangosteen, quercetin, broccoli (indole-3-carbinol, sulfuraphane, DIM), beta-glucans (oat, mushrooms, seaweed), flaxseed, chamomile, guggulsterone, propolis/bee pollen

	- as a side note, after testing various substances, the following substances were useful at reducing brain pressure/pain (not sure which ones worked):
	    - low carb, low protein, mostly vegan diet (vegetables like avocados/artichokes/broccoli, nuts like walnuts, berries like blueberries (avoid sugar at first if youre going to try glucose starvation), olive oil, mushrooms like reishi, shiitake, maitake, turkey tail), ashwagandha, atorvastatin, citicoline, melatonin, cilantro, ginger, coffee, green tea, lactobacillus (various strains), bacillus subtilis, milk thistle, selenium, omega-3 (fish oil), antioxidants (like vitamin C powder)
	    - various agglutinins have immune system effects (peanut/wheat germ agglutinins have an unclear association, abrus agglutinins may be helpful in reducing cancer)
	    - similarly, other substances that apparently help with DNA repair (other than milk thistle) include the following: Uncaria tomentosa, alpha-lipoic acid, coq10, sulforaphane, selenium, carotenoids, fisetin, grapeseed

	- also avoid the following when treating cancer: 
		- pesticides, methylfolate/nicotinamide supplements, paint fumes (which can contain silica dust/formaldehyde/cristobalite/other VOCs which can cause MS/cancer), unnecessary acetylaldehyde (found in pollutants and some foods like coffee/fruit, but which is not as harmful when it comes from some foods), sugar/processed foods, amino acids that tumors like such as arginine (also avoid sitosterol, NAC/glutathione, aluminium hydroxide, aluminium phosphate, and calcium phosphate which inhibit anti-tumor interleukins like interleukin-12), sun burn, ozone/pollution (I would use a Sundstrom silica dust respirator mask to filter out pollution while driving and while walking outside or while within a few miles of superfund sites/chemtrails/airports)
		- also infrared light therapy (LLLT, near/far infrared) is contraindicated for cancer but could be useful for fungal infections in the brain

    - tyrosine might also be implicated, which is a precursor to T3, which can influence cancer - given that T3 analogues like T2AA can inhibit PCNA's activity, tyrosine could be useful, but it might have the opposite effect, so Id avoid supplementing with that just in case

    - how else could these substances have been found? the following pages, which are results from a search like "citicoline" "withaferin" "lactoferrin" "uncaria" "atorvastatin", had some of these substances (neuroprotective drugs, triggers of positive neural processes, articles about anxiolytic substances, citations/usages of an article about a key inflammatory variable):
    	- https://www.science.gov/topicpages/a/acid-induced+microglial+activation
    	- https://www.science.gov/topicpages/p/potential+neuroprotective+drugs.html
    	- https://www.jci.org/articles/view/11830/citations
    - substances not tried: 
    	- I didnt try substances like various algaes which might be useful in treating cancer, or other anti-cancer substances not listed here

- for 'fungal treatment' Pubmed search results, this script included 'eugenol' and 'atorvastatin' and 'citicoline' and 'ginseng' which are active against that condition (but left out 'withaferin' which is an antifungal and is similar to 'ginsenoside').
- on the other side, there were thousands of nouns to sift through, so this tool could use some filtering.
- also, harmful substances were included in the search results (amphotericin is very harmful and can be deadly in the amounts required to fight a fungal infection)
- also, ineffective substances were included in the search results (miltefosine is ineffective for some people with fungal infections).
- similarly, some treatments will be missing, as only 10,000 results can be downloaded at a time - for example, the search results for 'fungal cryptococcus' did not include sitosterol or Undecylenic acid, both being known treatments.
- I think Pubmed includes Ayurvedic and Chinese medicine substances in a lot of the studies published there so I think it's a good general reference, although it is incomplete, as there are studies hosted on other sites that I haven't found on Pubmed
- this script will also retrieve plenty of irrelevant nouns as well like names of places where data was gathered, so maybe add 'treatment' or 'therapeutic' or 'therapy' to your search to only focus on treatment articles
- a good way to think of this tool is a 'way to find all the variables associated with a condition (including related conditions, symptoms/complications, related bio-system components like cell types involved, possible causes), 
  some of which are possible treatments which have been recently studied'
- you can filter your Pubmed search by recent results to make sure youre only finding the most recent treatments


OUTPUT FILES:

- keywords will be stored in (search_term)_output/keywords_(search_term).txt
- abstracts will be stored in (search_term)_corpus/abstracts_(search_term).txt
- similar treatments (based on either known_treatments or possible_treatments) will be stored in (search_term)_output/similar_treatments_to_known/possible_treatments_(search_term).txt
- Not possible treatments (like entities with an existing word root already added) will be stored in (search_term)_output/not_possible_treatments_(search_term).txt
- Possible entities will be stored in (search_term)_output/possible_treatments_(search_term).txt


TO DO LIST:

- add 'integrated deduplicated search results' so that results that occur in multiple searches can be de-duplicated (to find generally useful compounds that can help multiple conditions, for those managing multiple conditions)
- add filters to remove irrelvant nouns like places and filter out anything that isnt a treatment (compound, process, pathogen)
- lemmatize common words
- use context checking for a similarity metric from nltk - https://www.nltk.org/book/ch05.html
- filter out variants of the same word
- add generation of similar searches, such as a general type search as in 'fungal treatment' or a similar but more common fungal species like 'candida treatment' instead of 'cryptococcus treatment' or pathogens that bind to cryptococcus like 'staphylococcus aureus'
- fix errors, such as medical terms excluded from current possible_treatments file
- reduce time of script