# -*- coding: utf-8 -*-
"""
NLP WUWANA MAIN
@author: Oscar Fernández Vicente / ofvicente@gmail.com
jan/21
"""
import sys
import functions
import config
import database_config
import  pymysql
import argparse
import click

def main():

    #args    
    parser = argparse.ArgumentParser(description='WUWANA NLP SCRIPT')
    parser.add_argument("--onlyid")
    args = parser.parse_args()   

    # command line arguments control
    if(args.onlyid):
        if args.onlyid.lower() == 'false':
            sys.exit("no valid ID")
    else:
        sys.exit("--onlyid arg missing. Please, insert one company id")  
            
    if ((str(config.lib) != "gensim") & (str(config.lib) != "wordcloud") & (str(config.lib) != "keybert")):
        print("lib parameter in config.py should be gensim, wordcloud or keybert")
        sys.exit()        

    #db connection      
    db = pymysql.connect(host = database_config.server, user = database_config.user, password = database_config.password, database = database_config.database)

    ##MAIN##
        
    nlp_obj = functions.NLP_Wuwana(db, 
                languages = config.languages,
                spacy_model = config.spacy_model,
                max_words = config.max_words, 
                remove_words = config.remove_words,
                replace_words = config.replace_words,
                empha_words = config.empha_words,
                weight_field = config.weight_field,
                empha_multi = config.empha_multi,
                desc_field = config.desc_field )
    nlp_obj.process_query_companies(onlyid = args.onlyid, lib = config.lib.lower())



if __name__ == "__main__":
    main()
    
    



