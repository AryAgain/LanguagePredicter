"""
file: train.py
description: Train data based on Decision Tree or Ada Boost
language: python3
author: Aryan Singh, as2886@rit.edu
"""

import re
import feature_list
import sys
import decisiontree as dt
import adab
import pickle


def getfilevalues(filename):
    f = open(filename)
    values = f.readlines()
    sentence_array = []

    # clean the data removing punctuations
    for line in values:
        t1 = line.split("|")
        temp_val = [re.sub(r'[^\w\s]', '',t1[1].strip()).lower(),
                    t1[0]]
        sentence_array.append(temp_val)
    #print(sentence_array)
    return sentence_array


def main():
    examples = sys.argv[1]
    hypothesisOut = sys.argv[2]
    learning_type = sys.argv[3]
    sentence_array = getfilevalues(examples)

    check_feature = feature_list.feature_count
    # convert the data into 2d boolean list based on number of feature lists
    data_list = []
    for sentence in sentence_array:
        temp = []
        for feature in check_feature:
            temp.append(feature(sentence[0]))
        temp.append(sentence[1])
        data_list.append(temp)

    if(learning_type == "dt"):
        rootnode = dt.tree_builder(data_list)
        pickle.dump(rootnode, open(hypothesisOut, 'wb'))
        print("Data trained through Decision Tree...")
    elif(learning_type == "ada"):
        adaroot = adab.ada_boost(data_list)
        pickle.dump(adaroot, open(hypothesisOut, 'wb'))
        print("Data Trained through Ada Boost...")
    else:
        print("Enter \"dt\" or \"ada\" in learning-type")



if __name__ == '__main__':
    main()