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
