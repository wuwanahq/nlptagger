# NLP Libraries and variables
lib = "keybert" # library to be used (wordcloud / gensim / keybert).
spacy_model = "./en_core_web_lg" # spacy pretrained model.
max_words = 5 # max words to be returned by wordcloud. Gensims is limited to 3 by default.

remove_words = "./data/words_to_remove.txt" # path to file of words to be removed.        
replace_words = "./data/words_to_replace.txt" # path to file of words to be replaced.
empha_words = "./data/words_to_emphasize.txt" # path to file of words to be emphasized.
empha_multi = 5 # number of times to repeat/emphasize words

# MySQL Database and Tables
desc_field = "description" # field from company table where description text is.
weight_field = "NLPInfoTag" # Field in company table where weights will be stored.
languages = ["es","fr","zh-cn"] # list of languages to be translated, in addition to english. Order is followed.
