# Functions here are used to create idf matrix
import operator
from pyspark import SparkConf, SparkContext
import re
from convenience import *
import math


def norm(pair):
    newPair = (' '.join(normalizedWords(pair[0])), pair[1])
    count = lambda x: 1 if x[0] != '' else 0
    return count(newPair)


def create(pair, sizeOfSet):
    return (pair[0], {k: math.log10(sizeOfSet/sum(pair[1].values())) for k,v in pair[1].items()})


# Input a text file -> output the tFmatrix
def makeIdfMatrix(sc, textFile, baseDataStructure):
    newRdd = loadToConvenienceRdd(sc, textFile)
    sizeOfSet = newRdd.map(lambda x: norm(x)).reduce(lambda x, y: x+y) 
    idf = baseDataStructure.map(lambda x: create(x, sizeOfSet))
    return idf 
