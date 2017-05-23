# -*- coding: utf-8 -*-

import bayes

listOPosts, listClasses = bayes.loadDataSet()
vocabList = bayes.createVocabList(listOPosts)
print vocabList
print bayes.setOfWords2Vec(vocabList, listOPosts[0])