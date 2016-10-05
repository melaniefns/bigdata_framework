# coding: utf-8
# Python 3.5.1

import collections

#### Implementation of the Map/Reduce Algorithm

text = """You have to dream
before your dream
can come true"""

def input_reader(text):
    """
    Input Reader of the Map/Reduce Algorithm

    Parameters
    ---------
    text = a text with many lines

    Returns
    -------
    a list of each line of the text
    """
    return text.split('\n')


def Map(line):
    """
    Map of the Map/Reduce Algorithm

    Parameters
    ----------
    line = a string wich is the line of the text

    Returns
    -------

    a list of a two elements list : the first element is each word
    in the list and the second it's its occurence in the list ( i.e. 1)

    """
    if line =="" :
        pass
    else :
        return [[word,1] for word in line.split()]

## test of the Map function

print(Map(input_reader(text)[2]))

def shuffle_sort(Map, list_lines):
    """
    shuffle_sort function of the Map/Reduce Algorithm

    Parameters :
    ------------
    Map : function
    list_lines : a list of the lines of the text

    Return :
    it returns a list of list of two elements :
    1. each word in the text shuffled and sorted
    2. a list of its occurence in the next or an integer
    if the word appears only one time

    """
    list_words=list()
    list_shuffle_sort=list()

    ## creation of the list of the words in the text sorted
    if list_lines ==[] :
        pass
    else :
        for line in list_lines :
            for double in Map(line) :
                list_words.append(double[0].lower())

    list_words.sort()

    ## creation of the list_shuffle_sort which is the list
    ## returned by the function

    dict_key_value=collections.Counter(list_words)
    list_without_duplicates=list(set(list_words))
    list_without_duplicates.sort()

    for word in list_without_duplicates :

        if dict_key_value[word]==1 :
            list_shuffle_sort.append([word,1])

        else :
            list_appearance=list()
            for k in range(dict_key_value[word]):
                list_appearance.append(1)
            list_shuffle_sort.append([word,list_appearance])


    return list_shuffle_sort


## test of the shuffle_sort function

print(shuffle_sort(Map, input_reader(text)))


### function Reduce

def Reduce(list_double):

    """
    Reduction of the Map/Reduce Algorithm

    Parameters
    ----------
    list_double : it's a list of the list of the shuffle and sort handled by the Framework

    Returns
    -------
    list of the list of reduces generate by the function
    """
    list_reduce=list()

    for double in list_double:

        if isinstance(double[1],int)==True:
            list_reduce.append(double)
        else :
            list_reduce.append([double[0],sum(double[1])])

    return list_reduce

## test of the reduce function

print(Reduce(shuffle_sort(Map, input_reader(text))))
