# -*- coding: utf-8 -*-
import spacy

def remove_stopwords_punctuations(line):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(line)
    output=[]
    for token in doc:
        if token.is_stop == False and token.is_punct == False and token.is_currency == False and token.is_digit == False:
            output.append(token)
    print(output)
    return output

