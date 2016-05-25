import json
import pickle

import numpy as np

import models.american_english
from utils.api_microsoft import *


def get_perplexity_am(dict, arr_all):
    gram_dict_2 = arr_all[0]
    gram_dict_3 = arr_all[1]
    gram_dict_4 = arr_all[2]
    gram_dict_5 = arr_all[3]

    pr_2gram = 1.0
    pr_3gram = 1.0
    pr_4gram = 1.0
    pr_5gram = 1.0

    print len(dict)

    count = 0

    for i in dict:
        text = dict[i]["text"]
        answer = dict[i]["answer"]

        text = text + " " + answer

        arr = text.split(" ")
        # print arr
        for_2_gram = " ".join(arr[-2:])
        for_3_gram = " ".join(arr[-3:])
        for_4_gram = " ".join(arr[-4:])
        for_5_gram = " ".join(arr[-5:])

        # print for_2_gram
        # print for_3_gram
        # print for_4_gram
        # print for_5_gram


        try:
            s = gram_dict_2[for_2_gram]
            s = gram_dict_3[for_3_gram]
            s = gram_dict_4[for_4_gram]
            s = gram_dict_5[for_5_gram]

            pr_2gram = pr_2gram * (1 / (gram_dict_2[for_2_gram] + 0.0)) ** (1 / (1 + 0.0))
            pr_3gram = pr_3gram * (1 / (gram_dict_3[for_3_gram] + 0.0)) ** (1 / (1 + 0.0))
            pr_4gram = pr_4gram * (1 / (gram_dict_4[for_4_gram] + 0.0)) ** (1 / (1 + 0.0))
            pr_5gram = pr_5gram * (1 / (gram_dict_5[for_5_gram] + 0.0)) ** (1 / (1 + 0.0))

            count += 1
        except:
            pass

    print count

    # count = 0
    # for i in dict:
    #     text = dict[i]["text"]
    #     answer = dict[i]["answer"]
    #
    #     text = text + " " + answer
    #
    #     arr = text.split(" ")
    #     for_2_gram = " ".join(arr[-2:])
    #
    #     try:
    #         s = gram_dict_2[for_2_gram]
    #         pr_2gram = pr_2gram * (1/(gram_dict_2[for_2_gram] + 0.0)) ** (1/(282+0.0))
    #         count += 1
    #     except:
    #         pass
    #
    # print "2gram " + str(count)
    #
    # count = 0
    # for i in dict:
    #     text = dict[i]["text"]
    #     answer = dict[i]["answer"]
    #
    #     text = text + " " + answer
    #
    #     arr = text.split(" ")
    #     for_3_gram = " ".join(arr[-3:])
    #
    #     try:
    #         s = gram_dict_3[for_3_gram]
    #         pr_3gram = pr_3gram * (1/(gram_dict_3[for_3_gram] + 0.0)) ** (1/(72+0.0))
    #         count += 1
    #     except:
    #         pass
    #
    # print "3gram " + str(count)
    #
    # count = 0
    # for i in dict:
    #     text = dict[i]["text"]
    #     answer = dict[i]["answer"]
    #
    #     text = text + " " + answer
    #
    #     arr = text.split(" ")
    #     for_4_gram = " ".join(arr[-4:])
    #
    #     try:
    #         s = gram_dict_4[for_4_gram]
    #         pr_4gram = pr_4gram * (1/(gram_dict_4[for_4_gram] + 0.0)) ** (1/(20+0.0))
    #         count += 1
    #     except:
    #         pass
    #
    # print "4gram " + str(count)
    #
    # count = 0
    # for i in dict:
    #     text = dict[i]["text"]
    #     answer = dict[i]["answer"]
    #
    #     text = text + " " + answer
    #
    #     arr = text.split(" ")
    #     for_5_gram = " ".join(arr[-5:])
    #
    #     try:
    #         s = gram_dict_5[for_5_gram]
    #         pr_5gram = pr_5gram * (1/(gram_dict_5[for_5_gram] + 0.0)) ** (1/(7+0.0))
    #         count += 1
    #     except:
    #         pass
    #
    # print "5gram " + str(count)

    print pr_2gram
    print pr_3gram
    print pr_4gram
    print pr_5gram

    return pr_2gram, pr_3gram, pr_4gram, pr_5gram


def get_perplexity_microsoft(dict):
    pr_2gram = 1.0
    pr_3gram = 1.0
    pr_4gram = 1.0
    pr_5gram = 1.0

    count = 0

    arr_main = [[], [], [], []]

    for i in dict:
        text = dict[i]["text"]
        answer = dict[i]["answer"]

        arr = text.split(" ")

        for_2_gram = " ".join(arr[-1:])
        for_3_gram = " ".join(arr[-2:])
        for_4_gram = " ".join(arr[-3:])
        for_5_gram = " ".join(arr[-4:])

        query_1 = {"queries": [{"words": for_2_gram, "word": answer}]}
        query_2 = {"queries": [{"words": for_3_gram, "word": answer}]}
        query_3 = {"queries": [{"words": for_4_gram, "word": answer}]}
        query_4 = {"queries": [{"words": for_5_gram, "word": answer}]}

        try:
            result_1 = json.loads(make_post_api_microsoft(2, str(query_1)))["results"][0]["probability"]
            arr_main[0].append(float(abs(result_1)))
        except:
            print json.loads(make_post_api_microsoft(2, str(query_1)))

        try:
            result_2 = json.loads(make_post_api_microsoft(3, str(query_2)))["results"][0]["probability"]
            arr_main[1].append(float(abs(result_2)))
        except:
            print json.loads(make_post_api_microsoft(2, str(query_2)))

        try:
            result_3 = json.loads(make_post_api_microsoft(4, str(query_3)))["results"][0]["probability"]
            arr_main[2].append(float(abs(result_3)))
        except:
            print json.loads(make_post_api_microsoft(2, str(query_3)))

        try:
            result_4 = json.loads(make_post_api_microsoft(5, str(query_4)))["results"][0]["probability"]
            arr_main[3].append(float(abs(result_4)))
        except:
            print json.loads(make_post_api_microsoft(2, str(query_4)))

        print count

        # if (count > 20):
        #    break

        count += 1

    max_P = max([max(arr_main[0]), max(arr_main[1]), max(arr_main[2]), max(arr_main[3])])
    max_P = np.ceil(max_P)

    for i in arr_main[0]:
        pr_2gram = pr_2gram * (max_P - i) ** (1 / (count + 0.0))

    print pr_2gram

    for i in arr_main[1]:
        pr_3gram = pr_3gram * (max_P - i) ** (1 / (count + 0.0))

    print pr_3gram

    for i in arr_main[2]:
        pr_4gram = pr_4gram * (max_P - i) ** (1 / (count + 0.0))

    print pr_3gram

    for i in arr_main[3]:
        pr_5gram = pr_5gram * (max_P - i) ** (1 / (count + 0.0))

    print pr_5gram


f = open("data_sets_perplexity.pkl", "r")
dict = pickle.load(f)
f.close()

print len(dict)

arr = models.american_english.read_ngram_files(models.american_english.ngrams_proba_filename, is_main_files=False)
get_perplexity_am(dict, arr)

# get_perplexity_microsoft(dict)
