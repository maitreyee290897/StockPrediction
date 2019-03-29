# -*- coding: utf-8 -*-
import spacy
from spacy.symbols import nsubj, VERB, dobj, NOUN, advmod, neg, nsubjpass, amod,AUX

possible_prefixes_verb = [nsubj, nsubjpass, neg, advmod]
possible_suffixes_verb = [dobj]
possible_prefixes_noun = [amod, neg]
possible_suffixes_noun = []

nlp = spacy.load('en_core_web_sm', disable=['ner', 'textcat'])

GARBAGE_LIST = [("\r", " "), ("\n", " "), ("\t", " "), ("&#39;", "'"), ("&quot;", '\" '), ("&nbsp;", ' ')]

"""
removes stopwords and punctuations
"""


def remove_stopwords(line):
    doc = nlp(line)
    output = []
    for token in doc:
        if token.is_stop == False and token.is_punct == False and token.is_currency == False and token.is_digit == False:
            output.append(token)
    # print(output)
    return output


"""
makes bigrams
"""


def make_bigrams(line):
    doc = nlp(line)
    output = []
    for word in doc:
        if word.pos == VERB:
            for child in word.children:
                if child.dep in possible_prefixes_verb:
                    output.append((child.lemma_, word.lemma_))
                elif child.dep in possible_suffixes_verb:
                    output.append((word.lemma_, child.lemma_))
        elif word.pos == NOUN:
            for child in word.children:
                if child.dep in possible_prefixes_noun:
                    output.append((child.lemma_, word.lemma_))
    # print(output)
    return output


"""
makes unigrams
"""


def make_unigrams(line):
    doc = nlp(line)
    output = []
    for np in doc.noun_chunks:
        output.append(np.root.text)
    for word in doc:
        if word.pos == VERB and word.pos != AUX:
            output.append(word.lemma_)
    # print(output)
    return output


# split up a paragraph into sentences
# using regular expressions
def split_para_into_sentences(paragraph):
    # '''
    # break a paragraph into sentences
    #     and return a list
    # '''
    import re
    # to split by multile characters

    #   regular expressions are easiest (and fastest)
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList
