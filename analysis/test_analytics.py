# This is used to test the validity of the computations of the tf matrix, idf matrix, the base
# data structure and the semantic similarity calculation. It uses ../test/small_file.txt to compute
# tests.
import math
import sys
import os
from plumbum import local
sys.path.append(local.path(__file__).dirname.up())
from create_analysis import initApp
from convenience import makeWordToDocDataStructure, whitespace
from tf_matrix import makeTfMatrix
from idf_matrix import makeIdfMatrix
from compute_semantic_similarity import multTfIdf, computeSemanticSimilarity
dataLink = os.path.join(local.path(__file__).dirname, '..','test', 'small_file.txt')


sc = initApp('local', 'test')


def testConvDataStructure():
    convDataStructure = makeWordToDocDataStructure(sc, dataLink)
    print('Test for makeWordToDocDataStructure')
    testVal =  [('i',  {0: 2, 1: 1}), 
            ('like', {0:1}),
            ('data',  {0:1, 1:1}),
            ('science', {0:1}),
            ('and', {0:1}),
            ('hate', {1:1}),
            ('want', {2:1}),
            ('a', {2:1})]
    success = testVal == convDataStructure.collect()
    if success:
        print('\n\n\n\n', 'Test for makeWordToDocStructure', '\n', success, '\n\n\n\n')
    else: 
        print('\n\n\n\n', 'Test for makeWordToDocStructure', '\n', success, '\nTest: ', 
                testVal, '\nData: ', convDataStructure.collect(), '\n\n\n\n')


def testTfMatrix():
    tfMatrixSmall = makeTfMatrix(sc, dataLink, makeWordToDocDataStructure(sc, dataLink))
    testVal = [('i', {0: 0.3333333333333333, 1: 0.3333333333333333}), 
            ('like', {0: 0.16666666666666666}), 
            ('data', {0: 0.16666666666666666, 1: 0.3333333333333333}), 
            ('science', {0: 0.16666666666666666}), 
            ('and', {0: 0.16666666666666666}), 
            ('hate', {1: 0.3333333333333333}), 
            ('want', {2: 0.5}), 
            ('a', {2: 0.5})]
    success =  tfMatrixSmall.collect() == testVal
    if success: 
        print('\n\n\n\n', 'Test for tf matrix', success, '\n\n\n\n')
    else:
        print('\n\n\n\n', 'Test for tf matrix', success, '\nTest: ', 
                testVal, '\nReal: ', tfMatrixSmall.collect(), '\n\n\n\n')


def testIdfMatrix():
    idfMatrixSmall = makeIdfMatrix(sc, dataLink, makeWordToDocDataStructure(sc, dataLink))
    testVal =  [('i', {0: math.log10(3/3), 1: math.log10(3/3) }), 
            ('like', {0: math.log10(3/1)}), 
            ('data', {0: math.log10(3/2), 1: math.log10(3/2) }), 
            ('science', {0: math.log10(3/1)}), 
            ('and', {0: math.log10(3/1)}), 
            ('hate', {1: math.log10(3/1)}), 
            ('want', {2: math.log10(3/1)}), 
            ('a', {2: math.log10(3/1)})]
    success = idfMatrixSmall.collect() == testVal
    if success:
        print('\n\n\n\n', 'Test for idf matrix', success,
         '\n\n\n\n')
    else:
        print('\n\n\n\n', 'Test for idf matrix', success,
                '\nTest: ', testVal, '\nReal: ', idfMatrixSmall.collect(),
         '\n\n\n\n')

        
def testMultMatrix():
    idfMatrixSmall = makeIdfMatrix(sc, dataLink, makeWordToDocDataStructure(sc, dataLink))
    tfMatrixSmall = makeTfMatrix(sc, dataLink, makeWordToDocDataStructure(sc, dataLink))
    mult = multTfIdf(sc, tfMatrixSmall, idfMatrixSmall)
    testVal =  [('i', {0: 0.3333333333333333 * math.log10(3/3), 1: 0.3333333333333333 * math.log10(3/3) }), 
            ('like', {0: 0.16666666666666666 * math.log10(3/1)}), 
            ('data', {0: 0.16666666666666666 * math.log10(3/2), 1: 0.3333333333333333 * math.log10(3/2) }), 
            ('science', {0:  0.16666666666666666 * math.log10(3/1)}), 
            ('and', {0: 0.16666666666666666 * math.log10(3/1)}), 
            ('hate', {1: 0.3333333333333333 * math.log10(3/1)}), 
            ('want', {2: 0.5 * math.log10(3/1)}), 
            ('a', {2: 0.5 * math.log10(3/1)})] 
    success = mult.collect().sort() == testVal.sort()
    if success:
        print('\n\n\n\n', 'Test for tf*idf matrix', success,
         '\n\n\n\n')
    else:
        print('\n\n\n\n', 'Test for tf*idf matrix', success,
                '\nTest: ', testVal.sort(), '\nReal: ', mult.collect().sort(),
         '\n\n\n\n')


def testSemSim():
    item1 = {0: 0.044, 1: 0.059}
    item2 = {0: 0.153, 2: 0.238}
    testVal = ((0.044*0.153+0.059*0.0+0.0*0.238) / 
            (math.sqrt(0.044*0.044+0.059*0.059+0.0*0.0) * 
                math.sqrt(0.153*0.153+0.0*0.0+0.238*0.238)))
    real = computeSemanticSimilarity(item1, item2)
    success = real == testVal
    if success:
        print('\n\n\n\n', 'Test for semantic similarity matrix', success, real,
         '\n\n\n\n')
    else:
        print('\n\n\n\n', 'Test for semantic similarity matrix', success,
                '\nTest: ', testVal, '\nReal: ', real,
         '\n\n\n\n')


if __name__ == '__main__':
    testConvDataStructure()
    testTfMatrix()
    testIdfMatrix()
    testMultMatrix()
    testSemSim()
