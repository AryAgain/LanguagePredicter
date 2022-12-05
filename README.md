# LanguagePredicter
**Predicts which language the given input is in using ada boost and decision tree**


The basic idea of predicting which language is based on features each language has
most common among.
Various online articles were referred for it. Following are some reference which
mentions few of the important features and difference between english and dutch:
https://www.superprof.com/blog/dutch-english-grammar-differences/
https://autolingual.com/dutch-english-similarities/
Based on various web references, following features are selected which are coded in
separate file “feature_list.py”:
- Feature0: At least two words contains “ij”
- Feature1: At least one word contains either “de” or “het” very common in dutch
- Feature2: The sentence contains any of the most common dutch words
- Feature3: Average size of words are more than 4.5, as most dutch words are long
- Feature4: The sentence contains common dutch bigrams listed
- Feature5: The sentence at least one word as en
- Feature6: The sentence contains some of the common words in english

#### Ada Boost :
We make a collection of lots of different decision trees, each having height of 1 called
stump.
The stumps are made using information gain based on entropy, using which the best
column is selected and split done based on it
Weight and error is calculated and added to the final value.

The algorithm of adaboost is applied using the one provided in textbook, which when
tested on different sets of data provides and accuracy of 90%

#### Decision tree:
Decision tree is calculated based on the entropy and then information gain out of it. Best
feature column is selected based on which column has most information gain and then
the same algorithm is recursively apply on two sets: True values of first split and false
values of first split.
Same is done until the tree exhausts or we find a Decision tree for which the information
Gain is 0.
The data trained provided 95% accuracy

### How to run:
The code has various section. To train first tain.py is used with the following arguments:
train <examples> <hypothesisOut> <learning-type>
examples is a file containing labeled examples. For example.
hypothesisOut specifies the file name to write your model to.
learning-type specifies the type of learning algorithm you will run, it is either "dt"
or "ada". You should use (well-documented) constants in the code to control
additional learning parameters like max tree depth, number of stumps, etc.
example : train.py trainData3.dat out "dt”
The preditiction is done using:
predict <hypothesis> <file>
ex: predict.py out test.txt


