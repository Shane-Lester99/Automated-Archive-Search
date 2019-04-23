
import sys
import os
from plumbum import local
sys.path.append(local.path(__file__).dirname.up())
#sys.path.append(os.path.join(local.path(__file__).dirname.up(), 'analysis'))
#from pyspark import SparkConf, SparkContext

#from analysis.tf_matrix import makeTfMatrix
from create_analysis import initApp
from convenience import makeWordToDocDataStructure, whitespace
#from tf_matrix import makeTfMatrix 
dataLink = os.path.join(local.path(__file__).dirname, '..','test', 'small_file.txt')
#dataLink = './small_file.txt'

sc = initApp('local', 'test')

def testConvDataStructure():
#    print()
#    print()
#    print(sc)
#    print(whitespace)
#print(makeWordToDocDataStructure)
#    print(makeWordToDocDataStructure(sc, dataLink))
    convDataStructure = makeWordToDocDataStructure(sc, dataLink)
    print('Test for makeWordToDocDataStructure')
    print('\n\n\n\n', 'Test for makeWordToDocStructure', '\n', convDataStructure.collect() == [ 
            ('i',  {0: 2, 1: 1}), 
            ('like', {0:1}),
            ('data',  {0:1, 1:1}),
            ('science', {0:1}),
            ('and', {0:1}),
            ('hate', {1:1}),
            ('want', {2:1}),
            ('a', {2:1})], '\n\n\n\n')

#def testTfMatrix():
#    tfMatrixSmall = makeTfMatrix(sc, dataLink, makeWordToDocDataStructure(sc, dataLink))
#    print('\n\n\n\n', 'Test for tf matrix',   
#     tfMatrixSmall.collect() == [('i', {0: 0.3333333333333333, 1: 0.3333333333333333}), ('like', {0: 0.16666666666666666}), ('data', {0: 0.16666666666666666, 1: 0.3333333333333333}), ('science', {0: 0.16666666666666666}), ('and', {0: 0.16666666666666666}), ('hate', {1: 0.3333333333333333}), ('want', {2: 0.5}), ('a', {2: 0.5})],
#     '\n\n\n\n')
if __name__ == '__main__':
    testConvDataStructure()
    #testTfMatrix()
