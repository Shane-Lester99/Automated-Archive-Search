import re


def whitespace(num):
    for i in range(0, num, 1):
        print()

def normalizedWords(text):
    newList = re.compile(r'\W+', re.UNICODE).split(text.lower())
    newList = list(filter(lambda x: x != '', newList))
    return newList

# Gives us textFile -> [(line, doc_index)]. Conveinence loader to load data into easy to use form
def loadToConvenienceRdd(sc, textFile):
    # Note: "../test/medium_file.txt" is text
    return  sc.textFile(textFile).zipWithIndex()

def transformListToDict(array):
    new_dict = {}
    for i in array:
        if i in new_dict.keys():
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict

def indexValues(pair):
    normalize = lambda x: (normalizedWords(x[0]), x[1]) 

    #pair =  list(filter(lambda x: x[0] != [], normalize(pair)))

    reverse = lambda x: [(i, x[1]) for i in x[0]]
    pair = normalize(pair)
#    return pair
    pair = reverse(pair)
    return pair

def toDict(a):
    return {a: 1}

def addKey(a, b):
    if b in a.keys():
        a[b] += 1
    else:
        a[b] = 1
    return a

def stop(a, b):
    a
    return a

def makeWordToDocDataStructure(sc, textFile):
    # One pass to map reduce. We map to normalize text (remove punc, filter out values, and transform
    # to reverse word and line numer
    newRdd =  sc.textFile(textFile).zipWithIndex() 
    dc = newRdd.map(lambda x: indexValues(x)).reduce(lambda x,y: x +y)    
    dc = sc.parallelize(dc)  
    dc = dc.combineByKey(toDict, addKey, stop)
    #.reduce(lambda x,y: x + y) 
    #dc = dc.reduceByKey(lambda x,y: :
    return dc
#    documentSplit = newRdd.map(lambda x: (normalizedWords(x[0]), x[1])).filter(lambda x: x[0] != [])
#    wordSplit = documentSplit.map(lambda x: [(i, x[1]) for i in x[0]]).reduce(lambda x,y: x+y)
#    wordSplit = sc.parallelize(wordSplit)
#    # One pass to map to get data structure
#    groupByWord = wordSplit.groupByKey().map(lambda x: (x[0], list(x[1])))
#    dictByWord = groupByWord.map(lambda x: (x[0], transformListToDict(x[1])))
#    return dictByWord
