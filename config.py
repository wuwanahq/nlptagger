###################################
####### CONFIG FILE ###############
###################################
max_words = 5 # max words to be returned by wordcloud. Gensims is limited to 3 by default.
lib = "keybert" # library to be used (keybert / wordcloud(one word) / gensim ).
desc_field = "description" # field from company table where description text is.
weight_field = "TagInfo" # Field in company table where weights will be stored.
remove_words = "./data/words_to_remove.txt" # path to file of words to be removed.        
replace_words = "./data/words_to_replace.txt" # path to file of words to be replaced.
empha_words = "./data/words_to_emphasize.txt" # path to file of words to be emphasized.
finaltags_toremove = "./data/finaltags_toremove.txt" # tags that never will appear.
finaltags_alwaysmain = "./data/finaltags_alwaysmain.txt" # these tags will always be main tags (in order of appeareance).
empha_multi = 2 # number of times to repeat/emphasize words.
languages = ["es","fr","zh-cn"] # list of languages to be translated, in addition to english. Order is followed.
spacy_model = "./en_core_web_lg" # spacy pretrained model.