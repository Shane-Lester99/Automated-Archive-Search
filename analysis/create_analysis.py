
from datetime import datetime
from plumbum import local, cli
import sys
import random
import glob
import time
sys.path.append(local.path(__file__).dirname.up())
from tf_matrix import makeTfMatrix
from idf_matrix import makeIdfMatrix
from compute_semantic_similarity import multTfIdf, computeSemanticSimilarity
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

    startTime = None

    def printMenu(self):
        print('Command List:\n'
              'text: will show all words to perform analysis on\n'
              'retrievetop,<num>,<word>: will output the top n most similar words descending with num of 25\n'
              'help: display this help menu\n')

    def showAllText(self, rdd):
        items = rdd.collect()
        for i in items:
            print(i[0])

    def retrieveTopN(self, rdd, num, word):
        def findWord(pair1, pair2):    
            if pair1 and pair1[0] == word:
                return pair1
            elif pair2 and pair2[0] == word:
                return pair2
        def delWord(pair):
            return pair
                
        def createAnalysis(searchWord, pair, small):
            if small:
                num = 1
            else:
                num = random.randint(1, 5)
            return (num, (computeSemanticSimilarity(searchWord[1], pair[1]), pair[0]))
        def makeArray(a):
            return [a]
        def makePartition(a, b):
            return a + [b]
        def stop(a, b):
            return (a + b)
        newWord = rdd.reduce(lambda x, y: findWord(x,y))
        if not newWord:
            print('Word not found. Exiting')
            return
        whitespace(4)

        wordAmount = rdd.collect()
        wordAmount = len(wordAmount)
        smallAnalysis = True if wordAmount < 25 else False
        semanticAnalysis = rdd.map(lambda x: createAnalysis(newWord, x, smallAnalysis))

        #s = semanticAnalysis.combineByKey(makeArray, makePartition, stop)
        s = semanticAnalysis.groupByKey()
        if smallAnalysis:
            s = s.flatMap(lambda x: sorted(x[1], reverse = True)).collect()
            print('Warning. Data batch is very small (under 25 words). Consider analyzing larger document.')
        else:
            s = s.flatMap(lambda x:  (sorted(x[1], reverse = True)[0:5]))
            #s = s.reduceByKey(lambda x, y: sorted(x + y, reverse = True)[0:5])
            #s = s.combineByKey(makeArray
            #s1 = s.takeOrdered(5)
            
            s = sorted(s.collect(), reverse=True)
        if num > 25:
            print('Truncating to top 25 matches from {0}.'.format(num))
            num = 25
        print('\nTop {0} Words similar to {1}:\n'.format(num if wordAmount > num else wordAmount, word))
        i = 0
        counter = 1
        while i < num:
            if wordAmount == i:
                break
            score, w = s[i]
            print('    {0}) Word `{1}` has a score of {2}'.format(counter, w, score))
            i += 1
            counter += 1
        return 

    def __init__(self, filePath, command, num = None):
        self.startTime = datetime.now()
        sc = initApp('local','Semantic Similarity')
        if local.path(filePath).suffix != '.txt':
            raise ValueError('{0} is not a text file. Exiting'.format(filePath))
        print('Initializing calculation. Please wait')
        time.sleep(2)
        baseDataStructure = makeWordToDocDataStructure(sc, filePath)
        tfMatrix =  makeTfMatrix(sc, filePath, baseDataStructure) 
        idfMatrix = makeIdfMatrix(sc, filePath, baseDataStructure)
        mult = multTfIdf(sc, tfMatrix, idfMatrix) 
        if command == 'help':
            whitespace(4)
            self.printMenu()
            whitespace(4)
        elif command == 'text':
            whitespace(4)
            self.showAllText(mult)
            whitespace(4)
        elif re.search('retrievetop*', command):
            try:
               c, num, word = command.split(',')  
               num = int(num)
            except Exception as e:
                raise e
            word = word.lower()
            whitespace(4)
            self.retrieveTopN(mult,num, word)
            whitespace(4)
        else: 
            whitespace(4)
            print('Invalid command\n')
            self.printMenu()
            whitespace(4)
        print('Program started at {0} and ended at {1}'.format(self.startTime, datetime.now()))

#    printRdd(baseDataStructure)


if __name__=='__main__':
    if len(sys.argv) != 3:
        raise ValueError('Please enter a file path and command. Exiting.')
    SemanticSimilarity(sys.argv[1], sys.argv[2])
