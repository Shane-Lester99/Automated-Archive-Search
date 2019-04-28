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

    normalize = lambda x: (normalizedWords(x[0]), x[1])


    reverse = lambda x: [(i, x[1]) for i in x[0]]
    pair = normalize(pair)
    pair = reverse(pair)

def amountOfWordsMap(pair):
    normalize = lambda x: (normalizedWords(x[0]), x[1])
    reverse = lambda x: (x[1], len(x[0]))
    return reverse(normalize(pair))

def createTfValue(pair, dictCounts):
    newVal = dict([(k, pair[1][k] / dictCounts[k]) for (k,v) in pair[1].items()])
    return (pair[0], newVal)


# Input a text file -> output the tFmatrix
def makeTfMatrix(sc, textFile, baseDataStructure):
    newRdd = loadToConvenienceRdd(sc, textFile)
    inMemoryDataStructure = dict(newRdd.map(lambda x: amountOfWordsMap(x)).collect())
    rc = baseDataStructure.map(lambda x: createTfValue(x, inMemoryDataStructure))
    
    return rc 
