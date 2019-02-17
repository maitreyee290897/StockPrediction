# -*- coding: utf-8 -*-
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from feature_selection.unigram_feature import find_X,find_Y
from feature_selection.bigram_feature import find_X1,find_Y1

def unigram_chi_square() : 
    X = find_X()
    y= find_Y()
    X_new = SelectKBest(chi2, k=150).fit_transform(X, y)
    print(X_new)
    print(X_new.shape)
    #(150, 2)

def bigram_chi_square() : 
    X = find_X1()
    y= find_Y1()
    X_new = SelectKBest(chi2, k=150).fit_transform(X, y)
    print(X_new)
    print(X_new.shape)
    #(150, 2)
