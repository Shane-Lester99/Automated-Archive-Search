## Technology Used

This application is implemented using python and spark via the pyspark API. Natural language processing is a computationally intensive operation so this application utilizes sparks parallelization of data processing to efficiently analyze large text documents and extract insight fast. Python is fast to implement because of its lack of verbosity, so it was chosen for rapid prototyping and ease of use given the pyspark api.

## Algorithms:

The entire program was written with the constraint of map and reduce functions to make the modularity similar to MapReduce application. CombineByKey was also used when a combiner was needed.

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

## Improvements

I would have liked to make it so the program is interactive. That means that the computations of idf * tf would only have to be done at startup and then we could cache the solutions  of (word, s(idf, tf)) as we make them so if we want to retrieve them again it would be very fast
An extension to the above is I would have liked to use a technology like redis to persist a lot of these calculations associated with a user
I would just like to, in general, learn more about sparks architecture so I can improve the efficiency of each algorithm and understand the terminal output 
Better modularization and function naming. The functions are named poorly and there is repeated code. The codebase could use a refactoring. 
The king james bible didn’t have much more of a word count then the demo.txt file, yet it took 5 times as long. The only difference I can think of between the two files is the amount of whitespace. There is 100000 lines vs 8000 lines with a similar word count. This shows me that there is inefficiency involved in dealing with whitespace. This should be dealt with first before implementing new features.
Some kind of GUI to improve UX
