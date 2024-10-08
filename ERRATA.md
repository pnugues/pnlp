# Python for Natural Language Processing — _Penelope_
## List of errata

### Chapter 3
page 77, line 12: Replace `'(.{0,20}Hector(?=.{0,20}))'` with `'.{0,20}Hector(?=.{0,20})'`

### Chapter 4
page 99, line 17: Replace *these paramaters* with *these parameters*

### Chapter 6
page 144, line 12: Replace 0.370 with 4.370

page 149, Table 6.5, last column: Replace 0.01889 with 0.01902

### Chapter 8
page 198, first line: Replace *tol* with *to*

### Chapter 9
pages 250-251, the vectorization code could be shorter with the replacement of the
CountVectorizer and TfidfTransformer sequence with TfidfVectorizer, see here: 
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

### Chapter 10
Sect. 10.9.2, pages 279-282. The programs could be a bit simplified. See the new version of the notebook, `10_01_ngrams.ipynb`

### Chapter 11
Sect. 11.5.1, page 295, replace:

`words = re.findall('\p{L}+', text)`

with 

`words = re.findall(r'\p{L}+', text)`

### Chapter 13
page 356, five lines from the bottom, replace:

`re.findall(s_regex + '|\p{L}+', word[::-1])`

with

`re.findall(s_regex + r'|\p{L}+', word[::-1])`

page 356, two lines from the bottom, replace:

`     '|\p{L}+', 'celebration'[::-1])[::-1]))`

with

`     r'|\p{L}+', 'celebration'[::-1])[::-1]))`

page 375, replace:

`>>> unigram.encode('therefore')`

with

`>>> unigram.encode('there')`
