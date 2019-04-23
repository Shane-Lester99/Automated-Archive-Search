

from plumbum import local, cli
import sys
sys.path.append(local.path(__file__).dirname.up())
#from tf_matrix import makeTfMatrix
#from idf_matrix import makeIdfMatrix
from pyspark import SparkConf, SparkContext
from convenience import *

def whitespace(num):
    for i in range(0, num, 1):
        print()

def printRdd(rdd):
    whitespace(4)
    print(rdd.collect())
    whitespace(4)

def initApp(master, name):
    # NOTE: master == 'local', name = 'Semantic Simiarity'
    conf = SparkConf().setMaster(master).setAppName(name)
    return SparkContext(conf=conf)

if __name__ == '__main__':
    sc = initApp('local','Semantic Similarity')
    files = ['../test/medium_file.txt', '../test/small_file.txt']
    baseDataStructure = makeWordToDocDataStructure(sc, files[1])
    #tfMatrix =  makeTfMatrix(sc, files[1], baseDataStructure) 
    #AprintRdd(tfMatrix)
    #idfMatrix = makeIdfMatrix(sc, files[1])
    #`printRdd(tfMatrix)
    printRdd(baseDataStructure)

