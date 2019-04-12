#from plumbum import (cli, local)
#from datetime import datetime
#from collections import OrderedDict
#import pandas as pd
#import yaml
#from collections import OrderedDict
#import os
#import sys
import operator
from pyspark import SparkConf, SparkContext
#import collections
import re

#sys.path.append(os.path.join(local.path(__file__).dirname, 'db'))


#class Collaborator(cli.Application):
#    PROGNAME = "Semantic Similarity"
#    VERSION = "1.0"
#    DESCRIPTION = "This is a command line tool to perform a semantic analysis on many documents."

def whitespace(num):
    for i in range(0, num, 1):
        print()

def normalizedWords(text):
    newList = re.compile(r'\W+', re.UNICODE).split(text.lower())
    newList = list(filter(lambda x: x != '', newList))
    return newList

conf = SparkConf().setMaster("local").setAppName("Semantic Similarity")

sc = SparkContext(conf=conf)

# Gives us [(line, doc_index)]
lines = sc.textFile("../test/medium_file.txt").zipWithIndex()
# Gives us [(word, doc_index)]
documentSplit = lines.map(lambda x: (normalizedWords(x[0]), x[1])).filter(lambda x: x[0] != [])
wordSplit = documentSplit.map(lambda x: [(i, x[1]) for i in x[0]]).reduce(lambda x,y: x+y)
wordSplit = sc.parallelize(wordSplit)
# Gives us list of [(word, [doc_index])]. Duplicates indicate multiple times in doc
groupByWord = wordSplit.groupByKey().map(lambda x: (x[0], list(x[1])))


def transformListToDict(array):
    new_dict = {}
    for i in array:
        if i in new_dict.keys():
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict


# Transform into dictionary instead of list, with amounts
dictByWord = groupByWord.map(lambda x: (x[0], transformListToDict(x[1])))

# Data structure of {doc_id -> amount of words}
amountOfWordsPerDoc = dict(documentSplit.map(lambda x: (x[1], len(x[0]))).collect())

def createTf(wordDict):
    for (k, v) in wordDict.items():
        wordDict[k] = v / amountOfWordsPerDoc[k]
    return wordDict


# tF Matrix
tfMatrix = dictByWord.map(lambda x: (x[0], createTf(x[1])))


whitespace(4)
print(dictByWord.collect())
print(amountOfWordsPerDoc)
print(tfMatrix.collect())
whitespace(4)

#words = lines.flatMap(normalizedWords).countByValue()
#wordCount = collections.OrderedDict(sorted(words.items(), key=lambda x: x[1], reverse=True))


#whitespace(4)
#for word, count in wordCount.items():
#    cleanWord = word.encode('ascii', 'ignore')
#    if (cleanWord):
#        print(cleanWord, count)
#whitespace(4)
