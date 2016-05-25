#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import models.american_english


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
            arr = i.split(" ")
            for_2_gram = " ".join(arr[-2:])
            for_3_gram = " ".join(arr[-3:])
            for_4_gram = " ".join(arr[-4:])
            for_5_gram = " ".join(arr[-5:])

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
    f = open(models.american_english.ngrams_filename[gram_num - 2], 'r')
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


def plot(pr_2gram, pr_3gram, pr_4gram, pr_5gram):
    plt.plot([2, 3, 4, 5], [pr_2gram, pr_3gram, pr_4gram, pr_5gram], marker='o')
    plt.xlabel("ngram")
    plt.ylabel("perplexity")
    plt.axis([0, 7, -20, pr_2gram + 50])
    plt.show()

# reformat_to_probability(2)
# reformat_to_probability(3)
# reformat_to_probability(4)
# reformat_to_probability(5)

# arr = models.american_english.read_ngram_files(models.american_english.ngrams_proba_filename, False)
# pr_2gram, pr_3gram, pr_4gram, pr_5gram = get_perplexity(arr)
