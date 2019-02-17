# -*- coding: utf-8 -*-
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from feature_selection.unigram_feature import find_X,find_Y
from feature_selection.bigram_feature import find_X1,find_Y1


def unigram_recursive_feature_elimination() :
    X = find_X()
    y= find_Y()
    model = LogisticRegression()
    rfe = RFE(model, 3)
    fit = rfe.fit(X, y)
    print("Num Features: " + str(fit.n_features_))
    print("Selected Features: " + str(fit.support_))
    print("Feature Ranking: " + str(fit.ranking_))

def bigram_recursive_feature_elimination() :
    X = find_X1()
    y= find_Y1()
    model = LogisticRegression()
    rfe = RFE(model, 3)
    fit = rfe.fit(X, y)
    print("Num Features: " + str(fit.n_features_))
    print("Selected Features: " + str(fit.support_))
    print("Feature Ranking: " + str(fit.ranking_))

#bigram_recursive_feature_elimination();