
import spacy
from sqlalchemy import false
import wikipedia
nlp = spacy.load('en_core_web_sm')


sentence = input("Enter your value: ")
phrase=" "



def get_info_phrase(doc):
    for token in doc:
        print(str(token)+" => "+ str(token.dep_))
        if ( 
            "pobj" in token.dep_ or  
            "attr" in token.dep_ or 
            "dobj" in token.dep_ or
            "subj" in token.dep_ or
            "compound" in token.dep_ or
            "advmod" in token.dep_ or
            "amod" in token.dep_ or 
            "acomp" in token.dep_ 

            ):
                if( str(token)!='who' and  
                    str(token)!='where' and
                    str(token)!='when' and 
                    str(token)!='why' and 
                    str(token)!='which' and
                    str(token)!='what'):
                    global phrase
                    phrase = phrase + str(token) + " "
            
    return[]


   


try:                       
    doc = nlp(sentence)
    print("#####################")
    oblique_phrase = get_info_phrase(doc)   
    print("RESULT: " + str(phrase))
    print("#####################")   
    print(wikipedia.search(phrase))
    print("----------------------------------------------")
    print(wikipedia.summary(phrase , auto_suggest=False))
        
except wikipedia.exceptions.PageError:
    new_search=wikipedia.search(phrase)[0]
    print(wikipedia.summary(new_search))
