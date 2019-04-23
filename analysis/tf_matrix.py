from convenience import *


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



# Input a text file -> output the tFmatrix
def makeTfMatrix(sc, textFile, baseDataStructure):
    newRdd = loadToConvenienceRdd(sc, textFile)
    documentSplit = newRdd.map(lambda x: (normalizedWords(x[0]), x[1])).filter(lambda x: x[0] != []) 


    amountOfWordsPerDoc = documentSplit.map(lambda x: (x[1], len(x[0]))
    


    # Data structure of {doc_id -> amount of words}
    amountOfWordsPerDoc = dict(documentSplit.map(lambda x: (x[1], len(x[0]))).collect())
# 
    def createTf(wordDict):
        for (k, v) in wordDict.items():
            wordDict[k] = v / amountOfWordsPerDoc[k]
        return wordDict
#
#    
#
##    # tF Matrix
    tfMatrix = baseDataStructure.map(lambda x: (x[0], createTf(x[1])))
    return tfMatrix
#


