import copy
import math
import pickle

filename_2gram = "/Users/Nurislam/PycharmProjects/ngrams/google_ngram/googlebooks-eng-all-2gram-20120701-ae"
filename_3gram = "/Users/Nurislam/PycharmProjects/ngrams/google_ngram/googlebooks-eng-all-3gram-20120701-ae"
filename_4gram = "/Users/Nurislam/PycharmProjects/ngrams/google_ngram/googlebooks-eng-all-4gram-20120701-ae"
filename_5gram = "/Users/Nurislam/PycharmProjects/ngrams/google_ngram/googlebooks-eng-all-5gram-20120701-ae"

filename_proba_2gram = "/Users/Nurislam/PycharmProjects/ngrams/google_ngram/in_probably/2gram.txt"
filename_proba_3gram = "/Users/Nurislam/PycharmProjects/ngrams/google_ngram/in_probably/3gram.txt"
filename_proba_4gram = "/Users/Nurislam/PycharmProjects/ngrams/google_ngram/in_probably/4gram.txt"
filename_proba_5gram = "/Users/Nurislam/PycharmProjects/ngrams/google_ngram/in_probably/5gram.txt"

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
        # print i
        try:
            arr = i.split(" ")[::-1]
            for_2_gram = " ".join(arr[0:2][::-1])
            for_3_gram = " ".join(arr[0:3][::-1])
            for_4_gram = " ".join(arr[0:4][::-1])
            for_5_gram = " ".join(arr[0:5][::-1])

            print for_2_gram
            print for_3_gram
            print for_4_gram
            print for_5_gram

            a = gram_dict_2[for_2_gram]
            b = gram_dict_3[for_3_gram]
            c = gram_dict_4[for_4_gram]
            d = gram_dict_5[for_5_gram]

            # pr_2gram = pr_2gram * (1/(gram_dict_2[for_2_gram] + 0.0)) ** (1/(833946+0.0))
            # pr_3gram = pr_3gram * (1/(gram_dict_3[for_3_gram] + 0.0)) ** (1/(833946+0.0))
            # pr_4gram = pr_4gram * (1/(gram_dict_4[for_4_gram] + 0.0)) ** (1/(833946+0.0))
            # pr_5gram = pr_5gram * (1/(gram_dict_5[for_5_gram] + 0.0)) ** (1/(833946+0.0))

            count += 1

        except:
            pass

    # 833946
    print count

    # print pr_2gram
    # print pr_3gram
    # print pr_4gram
    # print pr_5gram


def reformat_to_probability(gram_num):
    print gram_num
    f = open(ngrams_filename[gram_num - 2], 'r')
    arr = []
    last_words = 0
    last_count = 0

    for i in f.readlines():

        s = i.replace("\n", "").replace("\r", "")
        i_split = s.split("\t")

        if (last_words == 0):
            last_words = i_split[0]
            last_count = i_split[-2]
            continue

        if (i_split[0] != last_words):
            arr.append(last_words.split(" ") + [int(last_count)])

        last_count = i_split[-2]
        last_words = i_split[0]

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

    f = open("/Users/Nurislam/PycharmProjects/ngrams/google_ngram/in_probably/" + str(gram_num) +
             "gram.txt", "w")
    for i in arr:
        f.write(str(i[-1]) + " " + " ".join(i[:gram_num]) + "\n")
    f.close()


def read_ngram_files(ngrams_filename):
    arr = []

    for i in ngrams_filename:
        print i
        f = open(i, 'r')
        dict = {}
        for i in f.readlines():
            s = i.replace("\n", "").replace("\r", "").lower()
            i_split = s.split(" ")
            words = " ".join(i_split[1:])
            dict[words] = copy.deepcopy(float(i_split[0]))
        f.close()

        arr.append(copy.deepcopy(dict))

    return arr


def test():
    f = open("/Users/Nurislam/PycharmProjects/ngrams/american_english/in_probably/2gram.txt", "r")
    count = 0
    arr = []
    for i in f.readlines():
        i_split = i.split(" ")
        arr.append(float(i_split[0]))

        # print count

        if (count > 17650):
            print i
            break
        else:
            count += 1

    f.close()

    return arr


# reformat_to_probability(2)
# reformat_to_probability(3)
# reformat_to_probability(4)
# reformat_to_probability(5)

arr = read_ngram_files(ngrams_proba_filename)

get_perplexity(arr)
