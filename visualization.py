# -*- coding: utf-8 -*-
import spacy
from spacy import displacy

"""
display on localhost:5000
"""

nlp = spacy.load('en_core_web_sm', disable=['ner', 'textcat'])

def display_dep(text):
    doc = nlp(text)
    sentence_spans = list(doc.sents)
    displacy.serve(sentence_spans, style='dep')
 
def display_ent(text):
    doc = nlp(text)
    displacy.serve(doc, style='ent')