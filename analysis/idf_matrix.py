#from plumbum import (cli, local)
#from datetime import datetime
#from collections import OrderedDict
#import pandas as pd
#import yaml
#from collections import OrderedDict
#import os
#import sys
import operator
from pyspark import SparkConf, SparkContext
#import collections
import re
from convenience import *


# Input a text file -> output the tFmatrix
def makeIdfMatrix(sc, textFile):
    wordToDoc = makeWordToDocDataStructure(sc, textFile)
    return wordToDoc


