# -*- coding: utf-8 -*-

from sklearn.ensemble import ExtraTreesClassifier
from feature_selection.unigram_feature import find_X,find_Y
from feature_selection.bigram_feature import find_X1,find_Y1

def unigram_bagged_decision_tree(): 
    X = find_X()
    y= find_Y()
    model = ExtraTreesClassifier()
    model.fit(X, y)
    print(model.feature_importances_)
    #(150, 2)

def bigram_bagged_decision_tree(): 
    X = find_X1()
    y= find_Y1()
    model = ExtraTreesClassifier()
    model.fit(X, y)
    print(model.feature_importances_)
    #(150, 2)

#bigram_bagged_decision_tree(); 
