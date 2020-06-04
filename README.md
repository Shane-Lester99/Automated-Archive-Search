# Automated Archive Search

Automated Archive Search is a natural language processing data pipeline to find and score the top k most similar terms to a search word by semantic similarity in a  collection of large text documents. It is excellent for searching massive archives at rapid speeds because of its use of PySpark's automated distributed processing and uses the famous web algorithm "term frequency - inverse document frequency" for massive text processing.

Some uses where Automated Archive Search  could do the trick:

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

## Example

Top 25 words similar to "feared" for a classic King James Bible

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
```

## System architecture and how to use

Please review "arcitecture.md" to learn the libraries, frameworks, data structures, and algorithms in Automated Archive Search and "how_to_use.md" to understand how to setup and give commands to this application.

## Current State Of Project

All the core logic has been implemented. It is currently a command line application. A lightweight interface would make this application much more accessible and would be fast and easy for a frontend developer to implement.

The last major update was in May 2019.
