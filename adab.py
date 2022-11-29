"""
file: adab.py
description: Train data based on AdaBoost
language: python3
author: Aryan Singh, as2886@rit.edu
"""

import math
import random
import decisiontree as dt


class AdaDepth:
    __slots__ = ['col_value']
    def __init__(self, col_value):
        self.col_value = col_value
    def checker(self, row):
        return self.col_value.match(row)

# Algo provided in the textbook is referred to code
def ada_boost(sentences):
    results = [sentences[index][-1] != 'en' for index in range(len(sentences))]
    w = [(1 / len(sentences)) for index in range(len(sentences))]
    h = [None for index in range(len(sentences[0]) - 1)]
    z = [0 for index in range(len(sentences[0]) - 1)]
    for index in range(len(sentences[0]) - 1):
        error = 0
        new_dataset, h[index] = learn(sentences, w)
        for inner_index in range(len(sentences)):
            if not new_dataset[inner_index][index] == results[inner_index]:
                error = error + w[inner_index]
        for inner_index in range(len(sentences)):
            if not new_dataset[inner_index][index] != results[inner_index]:
                w[inner_index] = w[inner_index] * (error / (1 - error))
        # Normalize the weights
        current_weights = []
        for index1 in range(len(w)):
            current_weights.append(w[index1] / sum(w))
        w = current_weights
        if error == 0:
            z[index] = float('inf')
        elif error == 1:
            z[index] = 0
        else:
            z[index] = math.log((1 - error) / error)
    return [(h[index], z[index]) for index in range(len(sentences[0]) - 1)]


def learn(sentences, weights):
    wl = []
    new_datas = []
    present_weight = 0
    for index in range(len(weights)):
        present_weight = present_weight + weights[index]
        wl.append(present_weight)
    for index in range(len(sentences)):
        rand_weight = random.uniform(0, 1)
        inner_index=0
        while not rand_weight <= wl[inner_index]:
            inner_index=inner_index+1
        new_datas.append(sentences[inner_index])
    featured_col, info_gain = dt.calculate_information_gain(new_datas)
    return new_datas, AdaDepth(featured_col)
