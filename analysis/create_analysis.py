

from plumbum import local, cli
import sys
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
    _textFilePath = None 
    
#    cli.SwitchAttr('--file-path',
#                                    mandatory=True,
#                                    argtype=cli.ExistingFile,
#                                    help='File to do analysis on')
    def __init__(self, filePath):
        self._textFilePath = filePath
        sc = initApp('local','Semantic Similarity')
#        files = ['../test/medium_file.txt', '../test/small_file.txt', '../test/demo.txt']
        if local.path(self._textFilePath).suffix != '.txt':
            raise ValueError('{0} is not a text file. Exiting'.format(self._textFilePath))
        baseDataStructure = makeWordToDocDataStructure(sc, self._textFilePath)
        tfMatrix =  makeTfMatrix(sc, self._textFilePath, baseDataStructure) 
        #AprintRdd(tfMatrix)
        idfMatrix = makeIdfMatrix(sc, self._textFilePath, baseDataStructure)
        mult = multTfIdf(sc, tfMatrix, idfMatrix)
        printRdd(mult)
#    printRdd(baseDataStructure)


if __name__=='__main__':
    if len(sys.argv) != 2:
        raise ValueError('Must have 1 file path argument. Exiting.')
    SemanticSimilarity(sys.argv[1])
