# -*- coding: utf-8 -*-
import copy
import random

filename_2gram = "/ngrams/american_english/w2.txt"
filename_3gram = "/ngrams/american_english/w3.txt"
filename_4gram = "/ngrams/american_english/w4.txt"
filename_5gram = "/ngrams/american_english/w5.txt"

filename_proba_2gram = "/ngrams/american_english/in_probably/2gram.txt"
filename_proba_3gram = "/ngrams/american_english/in_probably/3gram.txt"
filename_proba_4gram = "/ngrams/american_english/in_probably/4gram.txt"
filename_proba_5gram = "/ngrams/american_english/in_probably/5gram.txt"

ngrams_filename = [filename_2gram, filename_3gram, filename_4gram, filename_5gram]

ngrams_proba_filename = [filename_proba_2gram, filename_proba_3gram, filename_proba_4gram, filename_proba_5gram]


def read_ngram_files(ngrams_filename_arr, is_main_files):
    arr = []

    for i in ngrams_filename_arr:
        print i
        f = open(i, 'r')
        dict = {}
        for i in f.readlines():
            s = i.replace("\n", "").replace("\r", "")
            if is_main_files:
                i_split = s.split("\t")
            else:
                i_split = s.split(" ")

            words = " ".join(i_split[1:])
            dict[words] = copy.deepcopy(float(i_split[0]))
        f.close()

        arr.append(copy.deepcopy(dict))

    return arr


def ngram_am(dict, arr, num_gram):
    gram_dict = arr[num_gram - 2]
    count_correct = 0
    for i in dict:
        text = dict[i]["text"]
        text_split = text.split(" ")

        answer_arr = [-1, -1, -1, -1]
        try:
            answer_arr[0] = gram_dict[" ".join(text_split[-(num_gram - 1):]) + " " + dict[i]["var_1"]]
        except:
            pass

        try:
            answer_arr[1] = gram_dict[" ".join(text_split[-(num_gram - 1):]) + " " + dict[i]["var_2"]]
        except:
            pass

        try:
            answer_arr[2] = gram_dict[" ".join(text_split[-(num_gram - 1):]) + " " + dict[i]["var_3"]]
        except:
            pass

        try:
            answer_arr[3] = gram_dict[" ".join(text_split[-(num_gram - 1):]) + " " + dict[i]["var_4"]]
        except:
            pass

        predict_ans = random.randint(0, 3)
        if (dict[i]['answer'] == dict[i]["var_" + str(predict_ans + 1)]):
            count_correct += 1

    print count_correct / (len(dict) + 0.0)
