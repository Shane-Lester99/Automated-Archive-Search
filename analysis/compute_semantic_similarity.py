import math


def passNow(pair):
    return pair

#def passAndMark(pair):
#    return (pair[0], [pair[1], True])

#def merge(x, y):
#    top = x if isinstance(x[1], dict) else y 
#    bottom = x if top is not x else y
#    return 

def merge(x, y):
    newDict = {}
    for (k, v) in x.items():
        newDict[k] = x[k] * y[k]
    return newDict


# multiply tf * idf 
def multTfIdf(sc, tf, idf): 
    shared = tf.map(lambda x: passNow(x)) 
    shared += idf.map(lambda x: passNow(x))
    mult = shared.reduceByKey(lambda x, y: merge(x, y))
    return mult


# compute semantic similarity on matrix
def computeSemanticSimilarity(item1, item2, termNum):
    top, b1, b2 = 0, 0, 0
    for i in range(termNum):
        try:
            item1[i]
        except KeyError:
            item1[i] = 0
        try:
            item2[i]
        except KeyError:
            item2[i] = 0
        top += item1[i] * item2[i]
        b1 += item1[i] * item1[i]
        b2 += item2[i] * item2[i]
    print(top, math.sqrt(b1), math.sqrt(b2))
    return top / (math.sqrt(b1) * math.sqrt(b2)) 


