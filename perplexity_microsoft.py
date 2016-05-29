#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import json

from utils.api_microsoft import *

filename_2gram = "/american_english/w2.txt"
filename_3gram = "/american_english/w3.txt"
filename_4gram = "/american_english/w4.txt"
filename_5gram = "/american_english/w5.txt"

filename_proba_2gram = "/american_english/in_probably/2gram.txt"
filename_proba_3gram = "/american_english/in_probably/3gram.txt"
filename_proba_4gram = "/american_english/in_probably/4gram.txt"
filename_proba_5gram = "/american_english/in_probably/5gram.txt"

ngrams_filename = [filename_2gram, filename_3gram, filename_4gram, filename_5gram]

ngrams_proba_filename = [filename_proba_2gram, filename_proba_3gram, filename_proba_4gram, filename_proba_5gram]


def get_perplexity(arr_all):
    gram_dict_2 = arr_all[0]
    gram_dict_3 = arr_all[1]
    gram_dict_4 = arr_all[2]
    gram_dict_5 = arr_all[3]

    pr_2gram = 1.0
    pr_3gram = 1.0
    pr_4gram = 1.0
    pr_5gram = 1.0

    count = 0
    for i in gram_dict_5:
        try:
            arr = i.split(" ")[::-1]
            for_2_gram = " ".join(arr[0:2][::-1])
            for_3_gram = " ".join(arr[0:3][::-1])
            for_4_gram = " ".join(arr[0:4][::-1])
            for_5_gram = " ".join(arr[0:5][::-1])

            pr_2gram = pr_2gram * (1 / (gram_dict_2[for_2_gram] + 0.0)) ** (1 / (833946 + 0.0))
            pr_3gram = pr_3gram * (1 / (gram_dict_3[for_3_gram] + 0.0)) ** (1 / (833946 + 0.0))
            pr_4gram = pr_4gram * (1 / (gram_dict_4[for_4_gram] + 0.0)) ** (1 / (833946 + 0.0))
            pr_5gram = pr_5gram * (1 / (gram_dict_5[for_5_gram] + 0.0)) ** (1 / (833946 + 0.0))

            count += 1

        except:
            pass

    # 833946
    print count

    print pr_2gram
    print pr_3gram
    print pr_4gram
    print pr_5gram

    return pr_2gram, pr_3gram, pr_4gram, pr_5gram


def reformat_to_probability(gram_num):
    f = open(ngrams_filename[gram_num - 2], 'r')
    arr = []
    for i in f.readlines():
        s = i.replace("\n", "").replace("\r", "")
        i_split = s.split("\t")

        arr.append(i_split[1:] + [int(i_split[0])])

    f.close()

    last = arr[0][0:(gram_num - 1)]
    num = arr[0][-1]

    some_arr = []

    arr = arr[1:]

    for i in xrange(len(arr)):
        if (last == arr[i][0:(gram_num - 1)]):
            num += arr[i][-1]
            some_arr.append(i)

        if (last == arr[i][0:(gram_num - 1)] and i == 1):
            some_arr.append(0)

        if (last != arr[i][0:(gram_num - 1)] and not (last == arr[i][0:(gram_num - 1)] and i == 1)):
            for j in some_arr:
                arr[j][-1] = arr[j][-1] / (num + 0.0)
            num = 0
            some_arr = []

        last = arr[i][0:(gram_num - 1)]

    for i in xrange(len(arr)):
        if (arr[i][-1] > 1):
            arr[i][-1] = 1

    f = open("/american_english/in_probably/" + str(gram_num) +
             "gram.txt", "w")
    for i in arr:
        f.write(str(i[-1]) + " " + " ".join(i[:gram_num]) + "\n")
    f.close()


def read_ngram_files(ngrams_filename, is_main_files=True):
    arr = []

    for i in ngrams_filename:
        print i
        f = open(i, 'r')
        dict = {}
        for i in f.readlines():
            s = i.replace("\n", "").replace("\r", "")
            if (is_main_files):
                i_split = s.split(" ")
            else:
                i_split = s.split("\t")

            words = " ".join(i_split[1:])
            dict[words] = copy.deepcopy(float(i_split[0]))
        f.close()

        arr.append(copy.deepcopy(dict))

    return arr


def test():
    f = open("/american_english/in_probably/2gram.txt", "r")
    count = 0
    arr = []
    for i in f.readlines():
        i_split = i.split(" ")
        arr.append(float(i_split[0]))

        if (count > 17650):
            print i
            break
        else:
            count += 1

    f.close()

    return arr


def microsoft_api_model():
    query = 0

    num = 0
    count_correct = 0

    for i in dict:
        print num
        num += 1

        text = dict[i]["text"]
        text_split = text.split(" ")

        index_need = 0
        for j in xrange(len(text_split)):
            if ("_" in text_split[j]):
                index_need = j

        text_prepared = " ".join(text_split[0:index_need])

    query = {
        "queries":
            [
                {
                    "words": "i have a little",
                    "word": "dog"
                }
            ]
    }

    answer = make_post_api_microsoft(2, str(query))

    answer = json.loads(answer)

    print answer["results"]

    answer = make_post_api_microsoft(3, str(query))

    answer = json.loads(answer)

    print answer["results"]

    answer = make_post_api_microsoft(4, str(query))

    answer = json.loads(answer)

    print answer["results"]

    answer = make_post_api_microsoft(5, str(query))

    answer = json.loads(answer)

    print answer["results"]

    if (answer is None):
        continue

    answer = json.loads(answer)

    try:
        res_arr = answer["results"]
    except:
        continue

    prob_arr = []

    for j in res_arr:
        prob_arr.append(j["probability"])

    predict_ans = prob_arr.index(max(prob_arr))
    if (dict[i]['answer'] == dict[i]["var_" + str(predict_ans + 1)]):
        count_correct += 1


print count_correct / (len(dict) + 0.0)

microsoft_api_model()

reformat_to_probability(2)
reformat_to_probability(3)
reformat_to_probability(4)
reformat_to_probability(5)

arr = read_ngram_files(ngrams_proba_filename)

pr_2gram, pr_3gram, pr_4gram, pr_5gram = get_perplexity(arr)

print pr_2gram, pr_3gram, pr_4gram, pr_5gram

import matplotlib.pyplot as plt

plt.plot([2, 3, 4, 5], [pr_2gram, pr_3gram, pr_4gram, pr_5gram], marker='o')
plt.xlabel("ngram")
plt.ylabel("perplexity")
plt.axis([0, 7, -20, pr_2gram + 50])
plt.show()
