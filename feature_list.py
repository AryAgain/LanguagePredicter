"""
file: feature_list.py
description: List of features selected to train data
language: python3
author: Aryan Singh, as2886@rit.edu
"""
FEATURE_COUNT = 7

def feature_0(sentence):
    value = False
    count = 0
    for word in sentence.split():
        if 'ij' in word:
            count += 1
    if count >= 2:
        value = True
    return value


def feature_1(sentence):
    value = False
    kw = ['de', 'het']
    for word in sentence.split():
        if word not in kw:
            value = True
    return value



def feature_2(sentence: list) -> bool:
    value = False
    common_nl_words = ['ik', 'je', 'het', 'de', 'dat', 'een', 'niet',\
            'en', 'wat', 'van', 'ze', 'op', 'te', 'hij', 'zijn', 'er' ,\
            'maar', 'naar' ,'dan' ,'jij' ,'zo' ,'weet' ,\
            'ja' ,'kan' ,'geen' ,'nog' ,'wel' ,'wil' ,'moet' ,'goed' ,'hem',\
            'hebben' ,'nee' ,'heeft', 'komen' , 'tot' , 'veel' ,\
            'worden' , 'onze' , 'mensen' , 'zeg' , 'leven' , 'zeggen' ,'weer',\
            'gewoon' , 'nodig' , 'wij' , 'twee' ,'waar' ,'nu' ,'hoe' ,'ga' ,'kom' ,'uit',\
            'haar' ,'doen' ,'ook' ,'mij', 'daar' , 'zou' , 'gaan' ,'bent' ,\
            'al' , 'jullie' , 'zal' , 'bij', 'zie' , 'allemaal' , 'gedaan' , 'oh' ,\
            'dank' , 'huis' , 'hé' , 'zij' , 'jaar' , 'vader', 'doet','zoals',\
            'jouw' , 'vrouw' , 'geld' , 'hun' , 'ons' , 'gaat' , 'hebt', 'meer',\
            'waarom' , 'iets' , 'deze' ,'laat', 'doe', 'm', 'moeten', 'wie',\
            'jou', 'alles' , 'denk' , 'kunnen' , 'eens' , 'echt' , 'weg',\
            'toch' , 'zien' , 'oké' , 'alleen' , 'nou', 'dus', 'nooit',\
            'terug' , 'laten' , 'mee', 'hou' , 'die', 'heb', 'voor' , 'met', 'als', 'ben', 'mijn' ,'u' ,\
            'dit' ,'aan' ,'om' ,'hier' , 'komt' , 'niets' , 'zei' ,\
            'misschien' , 'kijk' , 'iemand' , 'tijd' , 'tegen' , 'uw' ,\
            'toen' , 'zit' , 'net' , 'weten' , 'heel' , 'maken' , 'wordt' ,\
            'dood' , 'mag' , 'altijd' , 'af' , 'wacht' , 'geef' , 'z' , 'lk',\
            'dag' , 'omdat' , 'zeker']
    for word in sentence.split():
        if word in common_nl_words:
            value = True
    return value


def feature_3(sentence):
    sum = 0
    for word in sentence.split():
        word_length = len(word)
        sum += word_length

    if len(sentence) > 0:
        avg_word_length = sum / len(sentence)
    else:
        avg_word_length = 0
    if avg_word_length >= 4.5:
        value = True
    else:
        value = False
    return value


def feature_4(sentence):
    common_bigrams = ['th', 'er', 'on', 'an']
    for word in sentence.split():
        for bigram in common_bigrams:
            if bigram in word:
                value = True
            else:
                value = False
            return value

# at least one word is "en"
def feature_5(sentence):
    for word in sentence.split():
        if word == "en":
            value = True
        else:
            value = False
        return value

def feature_6(sentence):
    substrings = ['the','and','tha','ent','ing','ion','tio','for','nde','has','nce','edt','tis','oft','sth','men']
    for word in sentence.split():
        for substring in substrings:
            if substring in word:
                value = True
            else:
                value = False
            return value


feature_count = [feature_0, feature_1, feature_2, feature_3, feature_4, feature_5, feature_6]