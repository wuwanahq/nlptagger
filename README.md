# Wuwana's NLP Python script

The objective of this script is to apply NLP techniques in order to extract topics (tags) from a body of text. 

It is used for the project [wuwana2](https://github.com/wuwanahq/wuwana2) to automatically classify a company based on the text from their website and social media.

## Requirements 

- [Python 3.7](https://www.python.org/downloads/) or higher.
- A MySQL database

## Steps

1. Launch the following command to install all the libraries required:

```
pip install -r requirements.txt
```
2. Download a Spacy pretrained model in the desired folder:

```
python -m spacy download en_core_web_lg
```

> This model can be switched with some other english one from https://spacy.io/models/en

## Config files
### 1. General

Use the **config.py** to define general aspects of the script:

- **max_words** = 5 - *Max number of words/tags to be returned by default. Gensims is limited to 3 by default.*
- **lib** = "keybert" # library to be used (wordcloud / gensim / keybert).
- **desc_field** = "description" - *field from company table where description text is taken.*
- **weight_field** = "NLPInfoTag" - *Field in company table where weights will be stored.*
- **remove_words** = "./data/words_to_remove.txt" - *path to file of words to be removed.*   
- **replace_words** = "./data/words_to_replace.txt" - *replace_words: path to file of words to be replaced.*
- **empha_words** = "./data/words_to_emphasize.txt" - *path to file of words to be emphasized.
- **empha_multi** = 5 - *number of times to repeat/emphasize words.
- **languages** = ["es","fr","zh-cn"] - *list of languages to be translated, apart from english. Same order is followed in output.*
- **spacy_model** = "./en_core_web_lg" - *spacy pretrained model.*

### 2. Database

Use the **database_config.py** to connect to the MySQL database.

## How to run the script

Once defined properly the config file, we can launch the script from a command line this way:

```
python main.py --onlyid ID
```

Where **ID** the id of the company in the database we want to update. This command will launch the script which will take the text from **desc_field** column (in the company table) and extract the main topics (including weights).

Topics will be stored in the following table/fields:

- **Tag table:** This table holds tags ID and descriptions (translated according to languages in config file). The table is updated when a new tag is discovered.
- **Company table:** For the selected ID, four columns are updated: 
  - FirstTagID (main tag)
  - SecondTagID (second main tag)
  - OtherTags (rest of them)
  - NLPInfoTag (or other field selected in config file, with the weights returned by NLP algos)