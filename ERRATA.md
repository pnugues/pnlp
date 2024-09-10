# Python for Natural Language Processing — _Penelope_
## List of errata

### Chapter 3
page 77, line 12: Replace `'(.{0,20}Hector(?=.{0,20}))'` with `'.{0,20}Hector(?=.{0,20})'`

### Chapter 6
page 144, line 12: Replace 0.370 with 4.370

page 149, Table 6.5, last column: Replace 0.01889 with 0.01902

### Chapter 8
page 198, first line: Replace *tol* with *to*

### Chapter 9
pages 250-251, the vectorization code could be shorter with the replacement of the
CountVectorizer and TfidfTransformer sequence with TfidfVectorizer, see here: 
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
