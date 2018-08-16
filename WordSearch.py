import time
import itertools

def read_files():
    new_list = open("C:\\Users\\1405003\\Desktop\\wordlistnew.txt", "r")
    keyword_list = open("C:\\Users\\1405003\\Desktop\\keywords.txt", "r")

    word_array = []
    keywords = []
    for line in new_list:
        word_array.append(line.rstrip("\n").lower())
    for line in keyword_list:
        keywords.append(line.rstrip("\n").lower())

    return word_array, keywords


def type_one(dict, key):
    start_time = time.time()

    count = [0 for i in range(len(key))]

    dictt = {word: 0 for word in dict}

    for word in dict:
        dictt[word] += 1

    for i in range(len(key)):
        if key[i] in dictt:
            count[i] = dictt[key[i]]

    print(count)
    print("----- %s -----" % (time.time() - start_time))


def type_two(dict, key):
    start_time = time.time()

    dictt = {word: 0 for word in dict}

    for word in dict:
        dictt[word] += 1
    count = [0 for i in range(len(key))]

    for i in range(len(key)):
        for k in dict:
            if key[i] in k:
                count[i] += 1
    print(count)
    print("----- %s -----" % (time.time() - start_time))


search_dict, keys = read_files()

type_one(search_dict, keys)
type_two(search_dict, keys)
