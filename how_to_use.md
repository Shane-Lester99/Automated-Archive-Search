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
