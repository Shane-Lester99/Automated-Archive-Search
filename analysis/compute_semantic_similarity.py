import math


def passNow(pair):
    return pair

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
#def computeSemanticSimilarity(item1, item2):
#    termNum = max(max(item1.keys()), max(item2.keys())) + 1
#    top, b1, b2 = 0, 0, 0
#    for i in range(termNum):
#        try:
#            item1[i]
#        except KeyError:
#            item1[i] = 0
#        try:
#            item2[i]
#        except KeyError:
#            item2[i] = 0
#        top += item1[i] * item2[i]
#        b1 += item1[i] * item1[i]
#        b2 += item2[i] * item2[i]
#    try:
#        result = top / (math.sqrt(b1) * math.sqrt(b2)) 
#    except ZeroDivisionError as e:
#        result = 0
#    return result


def computeSemanticSimilarity(item1, item2):
    keys = set().union(item1.keys(), item2.keys())
    top, b1, b2 = 0, 0, 0
    for i in keys:
        try:
            top += item1[i] * item2[i]
        except Exception as e:
            top += 0
        try: 
            b1 += item1[i] * item1[i]
        except Exception as e:
            b1 += 0
        try:
            b2 += item2[i] * item2[i]
        except Exception as e:
            b2 += 0
    try:
        result = top / (math.sqrt(b1) * math.sqrt(b2)) 
    except ZeroDivisionError as e:
        result = 0
    return result 

