"""
file: decisiontree.py
description: Train data based on Decision Tree
language: python3
author: Aryan Singh, as2886@rit.edu
"""

import feature_list
import math


class TreeNode:
    __slots__ = ['col_value', 'language_count_dict', 'true_branch', 'false_branch']

    def __init__(self, question, rows, true_branch, false_branch):
        self.col_value = question
        self.language_count_dict = language_instances_count(rows)
        self.true_branch = true_branch
        self.false_branch = false_branch


class PreferredCol:
    __slots__ = ['column', 'value']

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        """
        Match/check example with the question.
        :param example: a sentence
        :type example: list of data list
        :return: True if match. False otherwise.
        :rtype: bool
        """
        val = example[self.column]
        return val == self.value


def tree_builder(data_lines):
    """
    Build the decision tree recursively.
    :param data_lines: Training data
    :type data_lines: list
    :return: Node
    :rtype: TreeNode
    """
    # column with what preferred_feature that column asks and it's info gain 
    preferred_feature, info_gain = calculate_information_gain(data_lines)

    # If no info is gained just return a leaf node with remaining data_lines
    if info_gain == 0:
        return TreeNode(None, data_lines, None, None)

    # segregate true data_lines and false data_lines based on best gain column
    true_lines = []
    false_lines = []
    for line in data_lines:
        if preferred_feature.match(line):  # True
            true_lines.append(line)
        else:
            false_lines.append(line)

    false_branch = tree_builder(false_lines)
    true_branch = tree_builder(true_lines)
    main_node = TreeNode(preferred_feature, data_lines, true_branch, false_branch)
    return main_node


def calculate_information_gain(data_lines):
    """
    Get the best possible preferred_feature and best possible info gain for a particular set of data_lines.
    :param data_lines: data_lines on which to ask a preferred_feature.
    :type data_lines: list
    :returns best_column: Best preferred_feature that maximizes info gained
    :returns best_info_gain: Info gained on asking the best preferred_feature
    :rtype best_info_gain: float
    :rtype best_column: class
    """
    best_info_gain = 0
    best_column = None
    # calculate parent's entropy of the given data
    parent_entropy = entropy_calculation(data_lines)


    # calculate if column has only true/false or both to know the leaf
    for col in range(feature_list.FEATURE_COUNT):

        # find if a column has both True and False
        column_bools = []
        for line in data_lines:
            if(len(column_bools) == 0):
                column_bools.append(line[col])
            else:
                if(line[col] == True and column_bools[0] == False):
                    column_bools.append(True)
                    break
                elif(line[col] == False and column_bools[0] == True):
                    column_bools.append(False)
                    break

        for value in column_bools:
            preferred_feature = PreferredCol(col, value)
            featured_col = col
            featured_bool = value

            # Partionining data_lines depending on the preferred_feature
            true_rows = []
            false_rows = []
            for line in data_lines:
                #if line[featured_col] == featured_bool :
                if preferred_feature.match(line):
                    true_rows.append(line)
                else:
                    false_rows.append(line)
            # Avoid following cases
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate info gain of the current split
            prob_false = len(false_rows) / (len(false_rows) + len(true_rows))
            info_gain = parent_entropy - (
                        prob_false * entropy_calculation(false_rows) +
                        (1 - prob_false) * entropy_calculation(true_rows))

            if info_gain > best_info_gain:
                best_info_gain, best_column = info_gain, preferred_feature

    return best_column, best_info_gain


def entropy_calculation(data_lines):
    """
    Calculate entropy of given value
    :param data_lines: List of examples from training data
    :type data_lines: list
    :returns: The entropy value of provided data
    :rtype: float
    """
    total_rows = len(data_lines)
    # Calculate the instances of each language
    language_count = language_instances_count(data_lines)

    if len(language_count) == 2:
        en_probability = language_count['en'] / total_rows
        nl_probability = language_count['nl'] / total_rows
        entropy = -((en_probability * math.log(en_probability,2)) + (nl_probability * math.log(nl_probability,2)))
    else:
        entropy = 0.0
    return entropy



def language_instances_count(data_lines):
    """
    Gives the count of each language
    :param data_lines: List of list processed from training data
    :type data_lines: list of list
    :return: Dictionary with key as en/nl and it's corresponding count
    :rtype: dict
    """
    language_count = {}
    for line in data_lines:
        lng = line[-1]
        if lng == 'en' and lng not in language_count:
            language_count['en'] = 1
        elif lng == 'en':
            language_count['en'] += 1
        elif lng == 'nl' and lng not in language_count:
            language_count['nl'] = 1
        elif lng == 'nl':
            language_count['nl'] += 1
    return language_count

