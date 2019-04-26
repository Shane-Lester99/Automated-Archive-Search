

from plumbum import local, cli
import sys
import glob
import time
sys.path.append(local.path(__file__).dirname.up())
from tf_matrix import makeTfMatrix
from idf_matrix import makeIdfMatrix
from compute_semantic_similarity import multTfIdf
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

class SemanticSimilarity: 

    def printMenu(self):
        print('Command List:\n'
              'text: will show all words to perform analysis on\n'
              'retrievetop,<n>,<word>: will output the top n (only up to 5) most similar words desc\n'
              'help: display this help menu\n')

    def showAllText(self, rdd):
        items = rdd.collect()
        for i in items:
            print(i[0])

    def retrieveTopN(self, num):
        pass

    def __init__(self, filePath, command, num = None):
        sc = initApp('local','Semantic Similarity')
#        files = ['../test/medium_file.txt', '../test/small_file.txt', '../test/demo.txt']
        if local.path(filePath).suffix != '.txt':
            raise ValueError('{0} is not a text file. Exiting'.format(filePath))
        print('Initializing calculation. Please wait')
        time.sleep(2)
        baseDataStructure = makeWordToDocDataStructure(sc, filePath)
        tfMatrix =  makeTfMatrix(sc, filePath, baseDataStructure) 
        #AprintRdd(tfMatrix)
        idfMatrix = makeIdfMatrix(sc, filePath, baseDataStructure)
        mult = multTfIdf(sc, tfMatrix, idfMatrix)
        #printRdd(mult)
        whitespace(4)
        
        if command == 'help':
            whitespace(4)
            self.printMenu()
            whitespace(4)
        elif command == 'text':
            whitespace(4)
            self.showAllText(mult)
            whitespace(4)
        elif re.search('retrievetop*', command):
            print('TTTTTTTTTTTTTTTTT')
             
        else: 
            whitespace(4)
            print('Invalid command\n')
            self.printMenu()
            whitespace(4)


#    printRdd(baseDataStructure)


if __name__=='__main__':
    if len(sys.argv) != 3:
        raise ValueError('Please enter a file path and command. Exiting.')
    SemanticSimilarity(sys.argv[1], sys.argv[2])
