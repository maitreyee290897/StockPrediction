# -*- coding: utf-8 -*-
import json
from feature_selection.unigram_feature import find_X_unigrams, find_Y_unigrams
from feature_selection.bigram_feature import find_X_bigrams, find_Y_bigrams
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from paths import CONFIG_PATH
from paths import PREPROCESSED_DATA_PATH
from feature_selection.tfidf_method import find_tfidf_unigrams
from feature_selection.tfidf_method import find_tfidf_bigrams
'''
 Add all Constants for this file here
'''
with open(CONFIG_PATH) as file:
    config = json.load(file)
PATH = config['project_path']
NUMBER_OF_ARTICLES = int(config['training-data-size'])

TEST_SIZE = 0.3
SEED_DECISION_TREE = 3
SEED_RFE = 3
SEED_CHI_SQUARE = 10
SEED_TF_IDF = 10
STEP_SIZE_RFE = 25
MIN_FEATURES_TAKEN_RFE = 50
MAX_FEATURES_TAKEN_RFE = 2500
FEATURES_STEP_RFE = 50
MIN_FEATURES_TAKEN_CHI_SQUARE = 25
MAX_FEATURES_TAKEN_CHI_SQUARE = 2800
FEATURES_STEP_CHI_SQUARE = 25
PLOT_Y_LOWER_LIMIT = 55
PLOT_Y_UPPER_LIMIT = 55

'''
load the json data from file
'''
with open(PREPROCESSED_DATA_PATH) as file:
    data = json.load(file)

#X = find_X_unigrams()
# X = find_X_bigrams()
X = find_tfidf_unigrams()
#X = find_tfidf_bigrams()

y = find_Y_unigrams()
# y = find_Y1_bigrams()

ilist = []
acc = []

# print(X.shape)
# print(X1.shape)

'''
Decision Tree
------------------------------------------------------------------------
'''


def decision_tree():
    model = ExtraTreesClassifier()
    model.fit(X, y)
    model = SelectFromModel(model, prefit=True)

    x_new = model.transform(X)
    x_train, x_test, y_train, y_test = train_test_split(x_new, y, test_size=TEST_SIZE, random_state=SEED_DECISION_TREE)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(x_train, y_train)
    y_pred = svclassifier.predict(x_test)
    print(confusion_matrix(y_test, y_pred))
    print(100 * accuracy_score(y_test, y_pred))


'''
Recursive Feature Elimination
------------------------------------------------------------------------
'''


def rfe():
    for i in range(MIN_FEATURES_TAKEN_RFE, MAX_FEATURES_TAKEN_RFE, FEATURES_STEP_RFE):
        ilist.append(i)
        svc = SVC(kernel="linear", C=1)
        features = i
        rfe = RFE(estimator=svc, n_features_to_select=features, step=STEP_SIZE_RFE)
        rfe.fit(X, y)
        x_new = rfe.transform(X)
        x_train, x_test, y_train, y_test = train_test_split(x_new, y, test_size=TEST_SIZE, random_state=SEED_RFE)
        svclassifier = SVC(kernel='linear')
        svclassifier.fit(x_train, y_train)
        y_pred = svclassifier.predict(x_test)
        acc.append(100 * accuracy_score(y_test, y_pred))

    plt.plot(ilist, acc, linewidth=1.0)
    plt.ylim(PLOT_Y_LOWER_LIMIT, PLOT_Y_UPPER_LIMIT)
    plt.xlabel('Number of selected features')
    plt.ylabel('Accuracy (in %)')
    plt.savefig('rfe_accuracy.png')
    plt.show()


'''
Chi Square
------------------------------------------------------------------------
'''


def chi_square():
    for i in range(MIN_FEATURES_TAKEN_CHI_SQUARE, MAX_FEATURES_TAKEN_CHI_SQUARE, FEATURES_STEP_CHI_SQUARE):
        ilist.append(i)
        x_new = SelectKBest(chi2, k=i).fit_transform(X, y)
        x_train, x_test, y_train, y_test = train_test_split(x_new, y, test_size=TEST_SIZE, random_state=SEED_CHI_SQUARE)
        svclassifier = SVC(kernel='linear')
        svclassifier.fit(x_train, y_train)
        y_pred = svclassifier.predict(x_test)
        acc.append(100 * accuracy_score(y_test, y_pred))

    plt.plot(ilist, acc, linewidth=1.0)
    plt.ylim(PLOT_Y_LOWER_LIMIT, PLOT_Y_UPPER_LIMIT)
    plt.xlabel('Number of selected features')
    plt.ylabel('Accuracy (in %)')
    plt.savefig('chi2_accuracy.png')
    plt.show()


'''
tf-idf
------------------------------------------------------------------------
'''


def tf_idf():
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=SEED_TF_IDF)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(x_train, y_train)
    y_pred = svclassifier.predict(x_test)
    accuracy = 100 * accuracy_score(y_test, y_pred)
    print(accuracy)
    return accuracy


# decision_tree()
# rfe()
# chi_square()
# tf_idf()
# print(classification_report(y_test,y_pred))
