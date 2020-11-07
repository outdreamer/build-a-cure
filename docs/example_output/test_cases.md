# Test cases


## Disclaimer

	https://github.com/outdreamer/build-a-cure/blob/master/docs/example_output/disclaimer.md


## Conditions

	- Identify the processes & bio markers related to the condition as you go through search results so you can do secondary searches
		- target metric to inhibit/increase
		- cooperative metrics: synergistic compounds that enhance the effect of drugs without debilitating side effects
			- search for these & the stressors that deactivate/activate them
				Example: MUC1 - bacteria exposed to a split tail activates it
		- antagonistic metrics: any compounds that can neutralize the drug & the supplements/foods that contain them
			- get these inhibitors by looking up existing treatment pharmacokinetics/dynamics & interactions
				- search for inhibit, induce, substrate
				- check for synergistic effects & any effects that prevent the drug from being metabolized, which may be required to activate it
				- once you find a treatment, you need to check it against context provided by user to filter the list of treatments or style it differently
		- metrics further up the causal stack 
			- if you decrease hunger, diabetes doesnt happen, which is also a treatment (fasting)

### I. diabetes 

	- treatments should include: 
		- amylase & glucosidase inhibitors (caffeoyl, galloyl, and prenyl groups)
		- berberine
		- carb blockers like white kidney bean extract
		- insulin
		- fasting
		- sweet defeat (sugar taste blockers)
		- as well as any compounds that can target the processes/receptors involved (ghrelin, metabolism, dopamine, GLUT-4 receptor) 

	- treatment strategies should include:
		- inhibit glucose absorption 
		- insulin-mimicking activity
		- enhanced glucose uptake
		- regulation of insulin signaling pathways
		- translocation of GLUT-4 receptor 
		- activation of the PPARγ

### II. fungal meningitis 

	- treatments should include:
		- carvacrol, thymol, eugenol
		- ecgc
		- inhibitors of CYP51 (CYP2C9, CYP2C19, CYP3A4)
		- alternate routes to cyp51 outputs: 
			- depletion of ergosterol and ergosta-7-enol
			- accumulation of eburicol, obtusifolione, and lanosterol/obtusifoliol
		- azole drugs
		- imidazoles
		- sertraline
		- insight path for serotonin-imidazole:
			- serotonin, which play an important role in higher animals, are similar to alkaloids in their structure and biosynthesis and are sometimes called alkaloids
			- amino acids are precursors to some alkaloids
			- some amino acids have synergistic effects to kill the pathogen (histidine, carnosine, lysine)
			- alkaloid-related substances as serotonin, dopamine and histamine are important neurotransmitters so may impact meningitis
			- alkaloids have imidazole ring 
			- imidazoles are a subset of azoles that have fewer side effects

		- should pull drugs & drug types (like statin/alkylamine/sterol enzyme/terpene) from studies mentioning alternative strategies like: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC89924/

	- treatment strategies should include:
		- convert ergosterol to vitamin d
		- bind to ergosterol to break fungal cell membrane
		- any other substances that can bind with or permeate the fungal cell membrane or process ergosterol into something harmless
		- inhibit other links in chain allowing ergosterol to be constructed/protected:
			 "inhibitors of 3-hydroxy-3-methyglutaryl coenzyme A reductase, squalene synthase, squalene epoxidase, squalene epoxide-lanosterol cyclase, lanosterol demethylase, Δ8 to Δ7 isomerase, and S-adenosylmethionine:sterol methyltransferase"

	- insights should include:
		- inhibits [cytochrome p450] enzyme [14α-demethylase] in fungus but not mammals
		- inhibiting [cytochrome p450] enzyme [14α-demethylase] prevents production of ergosterol from lanosterol & accumulation of [14α-methyl] sterols
		- ergosterol is a required input of the fungal cell membrane
		- breaking cell components [membranes] is a way to kill an organism
		- once you break the membrane, your system can handle the components of the cell
		- required inputs (enzymes) to inputs (ergosterol) of object components [cell membranes] are a key target to break those components
			(this insight should already exist in your insight db without those specifics)
		- some natural processes break cell membranes

		- Entry of anti-infectives into the central nervous system (CNS) depends on:
		  - the compartment studied, 
		  - molecular size, 
		  - electric charge, 
		  - lipophilicity, 
		  - plasma protein binding, 
		  - affinity to active transport systems at the blood-brain/blood-cerebrospinal fluid (CSF) barrier, 
		  - host factors such as meningeal inflammation and CSF flow.

		- The ideal compound to treat CNS infections 
		  - is of small molecular size, 
		  - is moderately lipophilic, 
		  - has a low level of plasma protein binding, 
		  - has a volume of distribution of around 1 liter/kg
		  - is not a strong ligand of an efflux pump at the blood-brain or blood-CSF barrier

	- standard system analysis questions should include:
		- what are the limits of your system handling broken fungal cells?
		- does combination therapy work (convert ergosterol to vitamin d & prevent ergosterol production) without system damage?

	- drug attributes should include:
		- fungistatic
		- fungicidal (cryptococcus)
		- soluble in water & alcohol
		- stressor for kidneys
		- 90% excreted in urine & sweat, 10% metabolized

### III. cancer

	- relevant processes/attributes/systems:
		- communication, stressor distribution, & boundaries
		- immune system 
		- system & process error types

	- treatments should include:
		- anthrax for bladder cancer, salicylic acid (aspirin), AHCC, probiotics
		- stressors & handlers (change demand request & supply response matching)
		- known cancer drugs
		- hormone-reduction methods
		- ameliorative pathogen & microbe communities
		- metabolism (especially in blood sugar control & other fuels for cancer, as well as culling misfolded proteins), dietary enzymes
		- structural damage prevention (bind to toxins so theyre treated as fuel or not digested, tuning immune system to assume pathogens are hostile by default, tagging each new example encountered until its proven non-toxic using bio components as containers to form filters to allow testing, tuning immune system to gather & use the set of pathogen sub-components that will protect against all deadly pathogens)
		- immune system triggers
		- anti-inflammation triggers & similar triggers preventing excess unnecessary work of bio system like excess digestion
		- adjacent pathogens that can provide similar immunity
		- combinations/subsets & other structures of pathogens that can provide similar or equivalent immunity (wind blowing pieces of pathogens to form natural vaccine)
		- cell communication to prevent cancer from gathering (exercise, blood flow, oxygen absorption, deep breathing)
		- cell regeneration to cull compromised cells (exercise, cell proliferation/apoptosis triggers)
		- regulatory process triggers
		- neutralizing compounds to toxic chemicals (pollution, plastics, additives)

	- treatment strategies should include:
	  	- promote circulation in the organ (like caffeoquinone acid in the liver) to increasee cell communication, or push them to a place with greater blood flow or cell communication
	  	- identity set of stressors to activate helpful cell division
	  	- need a way to detect tumors using existing bio metrics
	  	- isolate tumors with a compound that they will interpret as the boundary of the host so they dont replicate further
	  	- make a list of anti-inflammatories & fit them to the stressor model
	  	- determine which organisms can borrow genes & look for link to cancer
	  	- determine the ratio of stress that optimizes learning without killing the host; ideally the solution would use the extra cell division potential to make useful cells
	  	- make a list of the common types of error the immune system makes (h pylori, cancer) & figure out if adjusting immune system function is the best layer to attack from
		- teach system to 'forget' previous misconfigurations with cell regeneration
		- teach system to function on various resource subsets with resource deprivation (fuel change, oxygen deprivation, environmental stress, nutrient-source variety)
		- stressor routing (apply cell stress to nearby or systemic components, like with massage to induce blood flow, weights to induce tissue repair)
		- reduce hormones that produce stressor-handler demand

### IV. Liver function

	- apple cider vinegar
	- d-mannose
	- bethanechol can stimulate the nerves of the bladder, making them more responsive to stimulus
	- prelief is a dietary supplement that works as an acid blocker for the bladder

	- eat:
	  - fruit & vegetables with vitamin c & get enough vitamin d
	  - vegetables (broccoli, squash, kale, green beans, potatoes, lettuce, soy, celery, garlic)
	  - lean proteins (turkey, chicken, fish, eggs)
	  - low-acid fruit (certain berries, pears, apricots, papaya, watermelon)
	  - high-fiber foods (wholegrain bread)
	  - almonds, cashews, peanuts

	- avoid:
	  - alcoholic/caffeinated beverages (carbonated drinks, chocolate, coffee & tea)
	  - high-acid foods (citrus fruits, apples, bananas, figs, cantaloupes, 
	      grapes, guava, peaches, prunes, plums, strawberries, pineapples,
	      cranberries (unless youre trying to clear an infection), 
	      tomatoes, onions, rye bread, fava beans, lentils, lima beans, nuts
	    )
	  - acidic condiments (vinegar, spicy seasoning, mayonnaise, soy sauce)
	  - weird or high-salt meat (corned beef, chicken liver, pickled herring)
	  - dairy (except probiotic yogurt if it doesnt bother you)
	  - excessive salt
	  - any sugar other than from low-acid fruit

	- other compounds to help liver & kidneys:
	  - milk thistle
	  - turmeric
	  - bitter leafy greens such as dandelion, chicory and arugula also may promote liver function by reducing congestion because they stimulate bile flow
	  - diuretics (celery, parsley, dandelion root, cucumber, asparagus, eggplant, watercress, artichokes and watermelon)
	  - sulfur detoxifies medication substances, pesticides & other environmental toxins
	    foods rich in sulfur include onions, garlic & cruciferous vegetables (broccoli, cauliflower, cabbage & brussels sprouts)
	    the primary medicinal compound in garlic is called allicin, a strong antimicrobial that also deters infections
	  - antioxidants eliminate free radicals, which reduce tissue damage & allow the organs & blood vessels to properly heal
	    vitamins C & E, beta-carotene & flavonoids are powerful antioxidants found in citrus fruits, berries, dark-colored grapes, apples, tomatoes, carrots, broccoli, spinach & asparagus
	  - vitamin C also helps to dissolve calcium buildup in the kidneys
	  - b. rotunda fingerroot has the potential to successfully treat liver cirrhosis in humans & diuresis (excess urine), dysentery and abdominal pain 

	- essential oils for liver:
		- rosemary: cleans the blood & flushes harmful toxins from the liver, stimulates bile production & flow which aids digestion, treats liver problems (cirrhosis & jaundice)
		- german chamomile: stimulates liver & gall bladder which helps digestion & cleans the blood
		- peppermint: stimulates bile flow from liver & gall bladder & helps digestion
		- juniper: helps digestion, helps liver eliminate waste products
		- fennel: helps digestion, has an antiseptic & protective effect on the liver

### V. Kidney function

	https://github.com/outdreamer/build-a-cure/blob/master/docs/example_output/kidney_function.md

### VI. Heart function

- heart supplements:
  	- arginine in moderation
  	- calcium in moderation
  	- coq10
  	- carnitine
  	- magnesium
  	- green tea in moderation
  	- Angiotensin_II_receptor_blocker selectively block the activation of AT1 receptors, preventing the binding of angiotensin II compared to ACE inhibitors.[4] 
	    - Angiotensin_II_receptor_blocker
	      - Angiotensin_II_receptor_blocker main uses are in the treatment of hypertension (high blood pressure), diabetic nephropathy (kidney damage due to diabetes) and congestive heart failure. 
	      - may worsen kidney functions such as reducing glomerular filtration rate associated with a rise of serum creatinine
    - ace inhibitor
      - ACEi have been shown to decrease erythropoietin production, help kidney function
      - Suppression of angiotensin II leads to a decrease in aldosterone level
      - ACE inhibitors can cause retention of potassium
      - ACE inhibitors, but not for other RAAS blockers, is an increase in bradykinin level
      - ACE inhibitor usually have a modest reduction in glomerular filtration rate (GFR)
        - Reduced GFR is especially a problem if the patient is concomitantly taking an NSAID and a diuretic.
          When the three drugs are taken together, the risk of developing renal failure is significantly increased.[20]
    - angiotensin: a peptide hormone that causes vasoconstriction and an increase in blood pressure. 
      It is part of the renin–angiotensin system, which regulates blood pressure. 
      Angiotensin also stimulates the release of aldosterone from the adrenal cortex to promote sodium retention by the kidneys
  	- beta blockers (reduce heart rate)
  	- diuretic (fluid retention)
  	- aldosterone antagonist
	- creatine, taurine, D-ribose
	- triptolide enhanced calcium restoration, curcumin inhibited ERK & p-STAT3 pathways, ginkolide B inhibited Ras/MAPK pathway, and steviol activated AMPK, which inhibited CFTR channel and mTOR pathway


## Functions


I. stimulate bladder
  - oregano oil
  - cinnamon oil
  - basil oil
  - tea tree oil
  - clary sage
  - rosemary oil


2. bladder anti-spasmodic
  - marjoram
  - chamomile
  - basil
  - cypress
  - grapefruit
  - peppermint
  - eucalyptus


3. assist liver/digestion
  - rosemary treats liver problems including cirrhosis & jaundice
  - german chamomile stimulates the liver & gall bladder which cleans the blood
  - peppermint stimulates bile flow from the liver & gall bladder
  - juniper
  - fennel has an antiseptic, protective effect on the liver 
  - cypress, lemon and thyme oils help clear the liver


4. regulate blood sugar
	- cinnamon
	- berberine
	- Several flavonoids inhibit glucose absorption by inhibiting intestinal α-amylase and α-glucosidase
		  https://www.ncbi.nlm.nih.gov/pubmed/28729836
		  https://www.sepalika.com/type-2-diabetes/14-amazing-herbs-that-lower-blood-sugar/
		  - prebiotics, tryptophan, green-plant membranes, resveratrol
		  - ginger
		  - holy basil, olive leaf, chaga
		  - substitutions of caffeoyl, galloyl, and prenyl groups
		  - ketone esters

5. antifungal

	- compounds
		- Propidium iodide rapidly penetrated the majority of the yeast cells when the cells were treated with concentrations just over the MICs, 
		  meaning that the fungicidal effect resulted from an extensive lesion of the cell membrane
			- Clove oil and eugenol also caused a considerable reduction in the quantity of ergosterol, a specific fungal cell membrane component
			- Natamycin is able to inhibit growth of fungi by specifically binding to ergosterol present in fungal cell membranes. The molecule interacts irreversibly with the sterol forming a sandwich-like structure embedded in the hydrophobic core of the membrane; between the two lipid layers. This causes membrane fragmentation and indirectly affects the functions ergosterol takes part in, such as endocytosis and exocytosis, vacuole fusion, morphogenesis, and amino acid and glucose transport across the membrane
		- Amphotericin B, an antifungal drug, targets ergosterol. It binds physically to ergosterol within the membrane, thus creating a polar pore in fungal membranes. This causes ions (predominantly potassium and hydrons) and other molecules to leak out, which will kill the cell.
			- quercetin & rutin helped activity of & lessened side effects of amphotericin
		- Fluconazole, miconazole, itraconazole, clotrimazole, and myclobutanil work in a different way, inhibiting synthesis of ergosterol from lanosterol by interfering with 14α-demethylase
		- Candicidin
		- Filipin – 35 carbons, binds to cholesterol (toxic)
		- Hamycin
		- Natamycin – 33 carbons, binds well to ergosterol
		- Nystatin
		- Rimocidin
		- berberine, caprylic acid, and undecylenic acid
		- garlic
			- In garlic supplements, vinyldithiins are only found in garlic oil macerates that are made by incubation of crushed garlic in oil
			- When a garlic clove is crushed, the enzyme alliinase is released forming allicin from the cysteine sulfoxide alliin. Allicin breaks down into additional organosulfur compounds. 
			- In the presence of oil or organic solvents, among the compounds formed are the isomeric vinyldithiins and ajoene
			- allinase, allicin, ajoene, vinyldithiin, thiosulfinate
			- ajoene is formed from a compound named allicin and an enzyme named allinase. When garlic is chopped or crushed, allicin and allinase come together to form the powerful antimicrobial agent ajoene.
		- betulinic: rosemary
		- ursolic: rosemary, thyme, holy basil, peppermint, apple peels
		- oleanolic: olive oil, garlic
		- amino and guanidinium derivatives of betulinic, ursolic, and oleanolic acids
		- new triterpene acid derivatives exhibited excellent antifungal activity against Cryptococcus neoformans, 
		  with MICs values being as low as 0.25 μg/ml (0.4 μM), and were approximately 65 times as active as fluconazole
		- oregano, winter savory
		- pine, thyme, eucalyptus
		- green tea
		- clove, cinnamon, thyme, garlic, ginger, tea, coffee (Cafestol), pepper, walnuts/pecans (ellagic acid), DHEA, saffron, resveratrol
		- lysozyme
		- cinnamic and benzoic acids
		- Origanum vulgare (oregano), Pinus sylvestris (pine), and Thymus vulgaris (thyme red) EOs, and their components (α-pinene, carvacrol, thymol) 
		- Apigenin - parsley, celery, celeriac, and chamomile tea
		- polymyxin antibiotics (polymyxin B and colistin)
		- miltefosine
		- Scapania verrucosa
		- Thapsia villosa
		- Hirtellina lobelii
		- 5-fluorocytosine
		- Mebendazole, fenbendazole, flubendazole
		- Caspofungin
		- L-histidine supplements is important is the treatment of chronic kidney failure
		- aryl-alkyl-lysines
		- triclosan
		- quercetin, rutin
		- chlorpromazine
		- terpenes, Aldehydes, & ketones are the toxic compound in essential oils
		- essential oils (extremely toxic, always look for alternatives before using these, use as little as possible if absolutely necessary & dilute heavily with water, using as few other supplements/nutrients as possible at the same time)
		  - ylang ylang
		  - citronella/lemongrass, palmarosa, rose (geraniol) + aegle, geranium, patchouli, Eucalyptus, peppermint, Cinnamon
		  - Among phenolic compounds, thymol and carvacrol are most fungitoxic. 
		  - Terpenoids, citral, geraniol, and citronellol show best activities.
		  - finger root (Boesenbergia rotunda) 
		  	- Pinocembrin is in fingerroot (cerebral ischemia, intracerebral hemorrhage, neurodegenerative diseases)
		  - limonene
		  - thyme (Thymus camphoratus and Thymus carnosus): thymol, p-cymene, myrcene, borneol, & linalool
		    - geraniol (LC50, 0.47 mg/ml) was the most toxic compound, 
		    followed by thymol (1.08 mg/ml), 
		    carvacrol (1.23 mg/ml) and 
		    terpinen-4-ol (2.61 mg/ml)
		    p-cymene significantly inhibited propagation
		- chlorpromazine (Thorazine, Largactil, Hibernal, and Megaphen): increases valproic acid levels, which can be derived from valerian (valerian suppressed cyp3a4)

	- mechanism

		- The most common fungi to cause brain infections include filament-forming fungi like Aspergillus, Mucor and Rhizopus and yeast-type fungi such as Candida and Cryptococcus. 
		  Less common causes of fungal brain infections include Trichosporon, Blastomyces, Histoplasma, Coccidioides, Paracoccidioides and Penicillium marneffei.

		- Drug treatment of fungal brain infections is complicated by the fact that many common antifungal drugs do not easily cross the blood-brain barrier. 
		  Some successes in treating fungal brain infections has been reported with the use of Amphotericin B, and some of the azole drugs such as Voriconazole and Posconazole. 
		  The newer Echinocandin drugs such as Caspofungin and Micafungin are very effective in treating brain infections caused by such fungi as Aspergillus and Candida, 
		  however they do not have good activity against some other fungi such as Cryptococcus, Mucor or Rhizopus.
		  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4507162/

		- Polyene antifungals
			- A polyene is a molecule with multiple conjugated double bonds. 
			- A polyene antifungal is a macrocyclic polyene with a heavily hydroxylated region on the ring opposite the conjugated system. 
			- This makes polyene antifungals amphiphilic. 
			- The polyene antimycotics bind with sterols in the fungal cell membrane, principally ergosterol. 
			- This changes the transition temperature (Tg) of the cell membrane, thereby placing the membrane in a less fluid, more crystalline state. 
			- In ordinary circumstances membrane sterols increase the packing of the phospholipid bilayer making the plasma membrane more dense.
			- As a result, the cell contents including monovalent ions (K+, Na+, H+, and Cl−), small organic molecules leak.
			- This is regarded one of the primary ways cell dies.
		- convert ergosterol to vitamin d
		- breaking fungal cell membranes by binding to ergosterol
		- change transition temperature of cell membrane in same way as polyene antifungal so that small organic molecules leak
		- Several anti-infectives (e.g., isoniazid, pyrazinamide, linezolid, metronidazole, fluconazole, and some fluoroquinolones) 
		  reach a CSF-to-serum ratio of the areas under the curves close to 1.0 and, therefore, are extremely valuable for the treatment of CNS infections
		- The polyene antimycotics bind with sterols in the fungal cell membrane, principally ergosterol
		- Azoles inhibit conversion of lanosterol to ergosterol by inhibition of lanosterol 14-alpha demethylase


6. lifespan extension/anti-aging

	- carnosine prevents aging by preventing glycation
	- excess methionine associated with short lifespan & cancer


7. prevent colitis
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2780078/
  - https://www.ncbi.nlm.nih.gov/pubmed/17217564 
	  - Lactobacillus reuteri
	  - Lactobacillus fermentum


8. increase blood flow to brain

  - increase electrolytes
  - increase stimulants
  - brain-clearing mechanisms (sleep)
  - increase cell activity
  - increase cell motion
    - brain cell types that can move:
      - glial: oligodendrocytes that migrate relative long distances to find their target axons onto which they wrap themselves to form the insulating myelin sheath
      - neurons: post-mitotic (fully differentiated, not-dividing) neurons


9. reduce hormones

	- reduce estrogen
	  - eat: red grapes, fiber, cauliflower, cabbage, b vitamins, mushrooms, melatonin, limonene, turmeric
	  - avoid: dairy, fat
	  - inhibit aromatase enzyme which enables conversion to estrogen
	    - nettle root, resveratrol, oleuropein in olives, quercetin, zinc, green tea, white mushroomow

	  - counteract phytoestrogen
	    - ibuprofen
	    - ranitidine

	    - Avoid using saw palmetto together with other herbal/health supplements that can also affect blood-clotting. 
	    	- This includes angelica (dong quai), capsicum, clove, danshen, garlic, ginger, ginkgo, horse chestnut, panax ginseng, poplar, red clover, turmeric, vitamin E, and willow.

	    - Extracts of certain mushrooms have been shown to inhibit aromatase when evaluated by enzyme assays, with white mushroom having shown the greatest ability to inhibit the enzyme

	    - alternative to saw palmetto (5-alpha reductase inhibitor, may block aromatase)

		    - aromatase inhibitors (damiana, white mushroom, nettle, resveratrol, garlic, quercetin, apigenin, citrus, chamomile, thyme, red clover, brussel sprouts, cauliflower, DIM (Diindolylmethane), Indole-3-Carbinol)
		      - decreased rate of bone maturation & growth, infertility, aggressive behavior, adrenal insufficiency, kidney failure, hair loss, and liver dysfunction
		      - patients with liver, kidney or adrenal abnormalities are at a higher risk of developing adverse events
		    - phytoestrogens in soy may block estrogen 
		    - polyphenols reduce estrogen
		    - green tea damages liver with more than a few cups


10. anti-inflammatory
	- melatonin
	- algae
	- vitamin d
	- eha/dha
	- turmeric/curcurmin
	- glutamine
	- probiotics
	- Folic acid, vitamin B 6, riboflavin and thiamin are particularly important to the proper functioning of t-cells and their quantity
