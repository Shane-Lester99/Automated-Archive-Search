# Semantic Similarity

## What is this application?

Semantic Similarity is a natural language processing application meant to automate the process of finding the top k most similar terms in large text documents given a query term. For example, if we analyze the top 5 words most similar to ‘ice cream’ within the context of a children’s novel about summer we might retrieve the words cold, delicious, creamy, summer,  and happy. Say we ran that same analysis across hundreds of children’s books (which is possible, because Spark supports horizontal scalability out of the box), we could get a nice view of what words are associated with ice cream across many children books.

A couple of real world use cases for this application are::

Automating the analysis of customer reviews:

- A company could use this application to see what words are typically associated with their products from large text surveys

- This could limit the need for companies to hire cheap labor to review surveys and automate tedious jobs

Voter analytics:

- A campaign manager could see common terms associated with their candidate to inform decision making

- For example, if the word slimy keeps popping up across social media but ‘hard working’ pops up in certain newspapers, it might give insight to campaign managers on making decisions

- This could be done across social media data, news articles, and any and all raw text data to quickly and objectively see what words are associated with their candidate, political party, or message

Qualitative sentiment analysis: 

- A research professor can use this application to see the context of a word in a given set of documents. 
This could be used by a history professor wanting to know terms associated with a particular person of interest across multiple time periods

## Technologies Used

This application is implemented using python and spark via the pyspark API. Natural language processing is a computationally intensive operation so this application utilizes sparks parallelization of data processing to efficiently analyze large text documents and extract insight fast. Python is fast to implement because of its lack of verbosity, so it was chosen for rapid prototyping and ease of use given the pyspark api.
 
## Setup

First navigate to root directory

Create a virtual environment (and activate it)

`pip install -r requirements.txt`

Navigate to directory analysis to use commands below

## Commands
This will output all the words which are valid for that text file for an analysis:

`spark-submit create_analysis.py ../test/medium_file.txt text` 

This will analyze the top 10 highest scores for word feelings. The number can be anywhere from 1-25:

`spark-submit create_analysis.py ../test/medium_file.txt retrievetop,10,feelings`

Will display help menu:

`spark-submit create_analysis.py ../test/medium_file.txt help` 

This will run tests on small files to validate correctness of computations. This entire program was built with test driven development in mind, assuring the validity of the analytics

`spark-submit test-analytics` 

## Test files

These files are packaged with this application for testing and development purposes: 

`demo.txt  small_demo.txt  medium_file.txt  small_demo.txt  small_file.txt bible.txt small_bible.txt`

`Small_file.txt` is used for testing purposes of computations. This application has automated testing to guarantee the validity of the computations. This file needs to be used for these automated tests. It is a very small file with only 7 words. It takes a few seconds to perform analytics on.

`medium_file.txt` is a slightly larger file of about 16 lines. It was used while developing for rapid development purposes. It takes a few seconds to perform analytics on.

`small_demo.txt` has 2000 lines. It is about a quarter of the size of the official demo file. It was used during development for speedier testing then the full size demo file. It takes a few seconds to perform analytics on.

`demo.txt` has 8000 lines and is the official standard for the application. It takes a few minutes to perform the analysis.

`Bible.txt` has about 100,000 lines and is an example of a real text document this application can analyze. It took about 10 minutes to perform the analysis.

Also note that these metrics are performed on a macbook pro with these specs:

```
MacBook Pro (15-inch, 2018)
Processor: 2.6 GHz Intel Core i7
Memory: 16 GB 2400 MHz DDR4

Running on an Ubuntu VM 18.04.1

Running on localhost default configuration for Spark.
```

## Example top 25 analysis for bible.txt and demo.txt

When this program was run on a king james bible from project gutenberg this was the resulting output and performance metrics. Note that it was run on one laptop so it couldn’t reap the benefits of hardware level parallelism

Top 25 Words similar to ‘feared’ in the bible:

input:
```
spark-submit create_analysis.py ../test/bible.txt retrievetop,25,feared
```

output:
```

    1) Word `feared` has a score of 1.0
    2) Word `divorce` has a score of 0.11269939811535641
    3) Word `eschewed` has a score of 0.09536102917453235
    4) Word `gods` has a score of 0.07103067740999565
    5) Word `newly` has a score of 0.06743043039024002
    6) Word `above` has a score of 0.060488736700924
    7) Word `midwives` has a score of 0.053679567436164234
    8) Word `behave` has a score of 0.05262032953187906
    9) Word `obeyed` has a score of 0.04798671866923051
    10) Word `presents` has a score of 0.04160381689523638
    11) Word `they` has a score of 0.03741342330854565
    12) Word `napkin` has a score of 0.03739689731679032
    13) Word `greatly` has a score of 0.03568226945036983
    14) Word `130` has a score of 0.03213687080536157
    15) Word `forgiveness` has a score of 0.031510745503789045
    16) Word `regarded` has a score of 0.030010984847613643
    17) Word `killedst` has a score of 0.02965317326644465
    18) Word `perceived` has a score of 0.02791116990718123
    19) Word `romans` has a score of 0.02736019673776634
    20) Word `was` has a score of 0.027029877274198914
    21) Word `still` has a score of 0.026950575454853274
    22) Word `treacherous` has a score of 0.02596950546331977
    23) Word `alms` has a score of 0.024555450100066756
    24) Word `because` has a score of 0.024540874074099422
    25) Word `egyptian` has a score of 0.022543066142793004

Program started at 2019-04-28 14:49:23.994704 and ended at 2019-04-28 15:01:48.135662

```
Here is another analysis with input from demo.txt, which was the original standard to meet when testing:
```
spark-submit create_analysis.py ../test/demo.txt retrievetop,25,pp44
```

```
Top 25 Words similar to pp44:

    1) Word `rte` has a score of 1.0
    2) Word `pp44` has a score of 1.0
    3) Word `pp42` has a score of 1.0
    4) Word `doc8341` has a score of 1.0
    5) Word `accompanied` has a score of 1.0
    6) Word `shc` has a score of 0.4954672823108429
    7) Word `disease_aa_disease` has a score of 0.414517191603598
    8) Word `sos` has a score of 0.3518141388602821
    9) Word `tubular` has a score of 0.21082076709157876
    10) Word `phosphoprotein` has a score of 0.17569469432343596
    11) Word `tubule` has a score of 0.16923048382576003
    12) Word `aa` has a score of 0.16262539553614674
    13) Word `tyrphostin` has a score of 0.1604753802393448
    14) Word `grb2` has a score of 0.1552365016486987
    15) Word `ng` has a score of 0.15338488067678935
    16) Word `chem_arachidonic_acid_chem` has a score of 0.14655397419403224
    17) Word `mapk` has a score of 0.13993823895646318
    18) Word `renal` has a score of 0.1360244281694116
    19) Word `association` has a score of 0.1228218403053491
    20) Word `rabbit` has a score of 0.12000847634451235
    21) Word `ag1478` has a score of 0.11993777181325778
    22) Word `egf` has a score of 0.11125021657335084
    23) Word `phorbol` has a score of 0.10977470972268176
    24) Word `ml` has a score of 0.10628194075157006
    25) Word `chem_tyrosine_chem` has a score of 0.1053419412943896




Program started at 2019-04-28 15:55:58.974964 and ended at 2019-04-28 15:57:46.642936
```


## Improvements

I would have liked to make it so the program is interactive. That means that the computations of idf * tf would only have to be done at startup and then we could cache the solutions  of (word, s(idf, tf)) as we make them so if we want to retrieve them again it would be very fast
An extension to the above is I would have liked to use a technology like redis to persist a lot of these calculations associated with a user
I would just like to, in general, learn more about sparks architecture so I can improve the efficiency of each algorithm and understand the terminal output 
Better modularization and function naming. The functions are named poorly and there is repeated code. The codebase could use a refactoring. 
The king james bible didn’t have much more of a word count then the demo.txt file, yet it took 5 times as long. The only difference I can think of between the two files is the amount of whitespace. There is 100000 lines vs 8000 lines with a similar word count. This shows me that there is inefficiency involved in dealing with whitespace. This should be dealt with first before implementing new features.
Some kind of GUI to improve UX

## Mapreduce Algorithms:

The entire program was written with the constraint of map and reduce functions. CombineByKey was also used when a combiner was needed.


To begin, we will define a small text file to run through the algorithms defined in the program.

```
Here is the file:
small.txt
I like data science and I, 
I hate data
want A
```

First we want to take this data structure and turn it into a data structure similar to 

```
col,d1,d2,d3
I,2,1,0 
like,1,0,0
data,1,1,0
science,0,1,0
and,0,1,0
hate.0,1,0
want 0,0,1
a0,0,1
```

The goal here is to lowercase all the text to normalize it and remove the punctuation. Also the goal is to count all the words from each document. The data structure aimed for here will be a list of key value pairs where each key is a word and the value is a dictionary where the key is document number and the value is count
 
We will build this data structure in step 1. It is needed as a basis to compute both the tf matrix and the idf matrix.

Step 1) Build the base matrix. Note that this algorithm is implemented in the file convenience.py 

Mapper:
Input: file path of document text file

Takes file and turns it into Data Structure [(line, line number)] with lower case words, no punctuation, and no empty values.

```
Output:
[[(i -> 0), 
(like -> 0) 
(data -> 0)
(science -> 0)
(and -> 0)
(i -> 0)],
[(i -> 1)
(hate -> 1)
(data -> 1)], [
(want -> 2)
(a -> 2)]
]
```

Reducer Input (above):

In the reducer we aim to remove all the internal arrays arrays

```
[(I -> 0), 
(Like -> 0) 
(Data -> 0)
(Science -> 0)
(And -> 0)
(I -> 0),
(I -> 1)
(Hate -> 1)
(Data -> 1)
(Want -> 2)
(A -> 2)]
]
```

Output of reducer:
We group all of the values in a list like:

```
I -> 0, 0, 1 
...
```

We skip the mapper and use a combiner to finish job. We also skip the reducer. So the mapper passes in a and returns a and there is no reducer needed. Combiner turns the list into a dictionary like below

Combiner:

Output:

```
I -> {1: 2, 2: 1}
Like -> {1:1}
Data ->  {1:1. 2:1}
Science -> {0;1} 
And -> {1:1}
Hate -> {2: 1}
Want -> {3:1}
A - > {3:1}
```

Code implementation:

```
 newRdd =  sc.textFile(textFile).zipWithIndex()
 dc = newRdd.map(lambda x: indexValues(x)).reduce(lambda x,y: x +y)
 dc = sc.parallelize(dc)
 dc = dc.combineByKey(toDict, addKey, stop)
```

Its implemented in file convience.py

This is similar to a record count mapreduce design pattern. We needed a numerical summarization of word count to document number.

2) Now we  will calculate the tf matrix. With input 

```
I -> {0: 2, 1: 1}
Like -> {0:1}
Data ->  {0:1. 1:1}
Science -> {0;1} 
And -> {0:1}
Hate -> {1: 1}
Want -> {2:1}
A - > {2:1}
```

We want output:

```
I -> {0: 2/6 , 1: 1/3}
Like -> {0:1/6}
Data ->  {0:1/6. 1:1/3}
Science -> {0;1/6} 
And -> {0:1/6}
Hate -> {1: 1/3}
Want -> {2:1/2}
A - > {2: 0.5}
```

Mapper input

```
I -> {0: 2, 1: 1}
Like -> {0:1}
Data ->  {0:1. 1:1}
Science -> {0;1} 
And -> {0:1}
Hate -> {1: 1}
Want -> {2:1}
A - > {2:1} 
```

And the raw input text file: 

```
I like data science and I, 
I hate data
want A
```

We turn the input file to this like before

```
[[(I -> 0), 
(Like -> 0) 
(Data -> 0)
(Science -> 0)
(And -> 0)
(I -> 0)],
[(I -> 1)
(Hate -> 1)
(Data -> 1)], [
(Want -> 2)
(A -> 2)]
]
```

But we reverse the values and count the words in each reversed list. This is done within mapper, no reduction needed. We also turn it into  a dictionary so we can use it in next calculation. Also note that this is a small data structure and will fit into memory. It will be at most the size of a words value which has been in every document, so it will always fit in memory as a dictionary

```
{0: 6, 1:3, 2:2}
```

We then define a mapper on the data structure (RDD)

```
I -> {0: 2, 1: 1}
Like -> {0:1}
Data ->  {0:1. 1:1}
Science -> {0;1} 
And -> {0:1}
Hate -> {1: 1}
Want -> {2:1}
A - > {2:1} 
```

In our mapper we match the keys to make the appropriate calculation and end up with the desired output

```
I -> {0: 2/6 , 1: 1/3}
Like -> {0:1/6}
Data ->  {0:1/6. 1:1/3}
Science -> {0;1/6} 
And -> {0:1/6}
Hate -> {1: 1/3}
Want -> {2:1/2}
A - > {2: 0.5}
```

```
I like data science and I, 
I hate data
want A
```

This is the code to implement:

```
newRdd = loadToConvenienceRdd(sc, textFile)
inMemoryDataStructure = dict(newRdd.map(lambda x: amountOfWordsMap(x)).collect())
rc = baseDataStructure.map(lambda x: createTfValue(x, inMemoryDataStructure))
```

It is implemented in ```tf_matrix.py```

Note that this is similar to a ‘stripes’ mapreduce design pattern. We computed a word count stripe and we processed it across all other stripes in our mapper.

Step 3: Compute idf

What we want:
We use existing data structure from step 1 and the raw text data. 

```
I -> {0: 2, 1: 1}
Like -> {0:1}
Data ->  {0:1. 1:1}
Science -> {0;1} 
And -> {0:1}
Hate -> {1: 1}
Want -> {2:1}
A - > {2:1} 
```

We compute the amount of lines from the raw text, here it is 3 and we update the data structure. We also sum up the values to see how many words appeared across document.

```
I -> {0: 2, 1: 1}
Like -> {0:1}
Data ->  {0:1. 1:1}
Science -> {0;1} 
And -> {0:1}
Hate -> {1: 1}
Want -> {2:1}
A - > {2:1} 
```

->

```
I -> {0: 3/3, 1: 3/3}
Like -> {0:1/3}
Data ->  {0:2/3. 1:2/3}
...
```

We get this by using a mapper and reducer to get the amount of documents across. We first replace each document with 1 in the mapper and then sum them up in the reducer. This gives us the number of documents. This is done in a function called norm in the program. It uses a count mapreduce design pattern

Then a map is used on each value in the data structure from step 1 to perform sizeofset/ sum of all dict values placed in the function math.log10


This is how the function looks in code:
```
newRdd = loadToConvenienceRdd(sc, textFile)
sizeOfSet = newRdd.map(lambda x: norm(x)).reduce(lambda x, y: x+y)
idf = baseDataStructure.map(lambda x: create(x, sizeOfSet))
```

It is implemented in file idf_matrix.py

This algorithm uses a numerical aggregation mapreduce design pattern where it makes a computation across all documents and updates the data structure given that information.

Step 4: Compute tf * idf
Mapper: Input
We already have the two existing data structures, just output both of them to reducer and group by the keys so identical keys end up on similar nodes
Output: two existing data structures

Reducer: input is our two existing data structures post map (from step 2 and step 3).

```
tf = 
I -> {1: 2/6, 2: 1/4}
Like -> {1:1/6}
Data ->  {1:1/6. 2:1/4}
And -> {1:1/6}
Hate -> {2: 1/4}
Want -> {3:1/2}
A - > {3:1/2}


idf = 
I -> log(1)
Like -> log(3/1)
Data -> log(3/2)
And ->  log(3) 
Hate -> log(3) 
Want -> log(3) 
A - > log(3) 
```


Reducer: output
```
tf*idf = 
I -> {1: log(1)2/6, 2: log(1)1/4}
Like -> {1:log(3)1/6}
Data ->  {1: log(3/2)1/6. 2: log(3/2)1/4}
And -> {1: log(3)1/6}
Hate -> {2: log(3)1/4}
Want -> {3: log(3)1/2}
A - > {3: log(3)1/2}
```

All we do is reduce the two data structures by key and perform the analytics on

This is implemented in file compute_semantic_similarity.py

This algorithm was written with the join mapreduce design pattern in mind. 

Step 5: Compute similarities for each term and retrieve top N results.

For example, we use term with key Like (but remember we will repeat this term for all keys)

Mapper:
Performing the computation S(like, term) on each word, reverse the output with the name, and give it a new key that is a random number from 1- 5 

```
I -> {1: log(1)2/6, 2: log(1)1/4}
Data ->  {1: log(3/2)1/6. 2: log(3/2)1/4}
And -> {1: log(3)1/6}
Hate -> {2: log(3)1/4}
Want -> {3: log(3)1/2}
A - > {3: log(3)1/2}

to:
(1, (S(like, I), like))
...
```

We then used combiner to combine the random keys to create local lists. We then aggregated to the top N of each list as we sorted each list. After our combiner we flatmap the list, sort it, and have the top 25 results.

This algorithm is inspired by the top k design pattern in mapreduce which uses local top n lists and then groups the results, sorts them, and truncates to the top n desired results.

