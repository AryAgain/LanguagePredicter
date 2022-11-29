"""
file: predict.py
description: Predicsts language based on Trained data
language: python3
author: Aryan Singh, as2886@rit.edu
"""
import pickle
import re
import feature_list
import sys


def getfilevalues(filename):
    f = open(filename)
    values = f.readlines()
    sentence_array = []
    check_feature = feature_list.feature_count
    # clean the data removing punctuations
    for line in values:
        temp_val = re.sub(r'[^\w\s]', '', line.strip()).lower()
        sentence_array.append(temp_val)
    data_list = []
    for sentence in sentence_array:
        temp = []
        for feature in check_feature:
            temp.append(feature(sentence))
        data_list.append(temp)
    return data_list

def main():
    node = pickle.load(open(sys.argv[1], 'rb'))
    test_values = getfilevalues(sys.argv[2])

    for data in test_values:
        tnode = checker(data, node)
        print(tnode)


def checker(sentence, node) -> list:
    """
    Checks a sentence converting it into boolean list format
    :param sentence: Testing data
    :type sentence: list
    :param node: Node which has prediction
    :type node: Adaboost or DecisionNode
    :return: List of possible classes
    :rtype: list
    """
    # if object is made from Ada Boost training:
    if isinstance(node, list):
        nl_total_weight = 0
        en_total_weight = 0
        for i in range(len(node)):
            if node[i][0].checker(sentence) == True:
                nl_total_weight += node[i][1]
            else:
                en_total_weight += node[i][1]
        if en_total_weight >= nl_total_weight:
            return 'nl'
        return 'en'
    # if object is made from Decision Tree training:
    else:
        # check if Leaf node
        if node.col_value == None and node.true_branch == None and node.false_branch == None:
            best_count = 0
            result = []
            for label in node.language_count_dict:
                if not node.language_count_dict[label] <= best_count:
                    result = []
                    result.append(label)
                    best_count = node.language_count_dict[label]
                elif not node.language_count_dict[label] > best_count or not node.language_count_dict[
                                                                                 label] < best_count:
                    result.append(label)
            return result[0]
        # Else recursion
        if node.col_value.match(sentence):
            return checker(sentence, node.true_branch)
        else:
            return checker(sentence, node.false_branch)


if __name__ == "__main__":
    main()

