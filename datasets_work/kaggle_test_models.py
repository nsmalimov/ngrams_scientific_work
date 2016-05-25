# -*- coding: utf-8 -*-

import csv
import sys

import utils.processing_text

csv.field_size_limit(sys.maxsize)

reload(sys)
sys.setdefaultencoding('utf-8')
sys.getdefaultencoding()

train_file = "training_set.tsv"


def open_file(filename):
    file_array = []
    with open(filename) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            file_array.append(line)
        return file_array


def prepare_train_set():
    train_set = open_file(train_file)
    dict = {}

    for i in train_set:

        var = [i[3], i[4], i[5], i[6]]

        var[0] = utils.processing_text.processing_text(var[0])
        var[1] = utils.processing_text.processing_text(var[1])
        var[2] = utils.processing_text.processing_text(var[2])
        var[3] = utils.processing_text.processing_text(var[3])

        for j in xrange(len(var)):
            j_split = var[j].split(" ")
            var[j] = j_split[0]

        flag = False
        for j in var:
            if var.count(j) > 1:
                flag = True
                break

        if (flag):
            continue

        s = utils.processing_text.processing_text(i[1])

        if not ("_" in s):
            continue

        index_need = 0

        s_split = s.split(" ")

        for j in xrange(len(s_split)):
            if ("_" in s_split[j]):
                index_need = j

        if (index_need < 3):
            continue

        arr = ['A', 'B', 'C', 'D']

        dict[i[0]] = {"text": " ".join(s_split[0:index_need]), "answer": var[arr.index(i[2])],
                      "var_1": var[0], "var_2": var[1], "var_3": var[2], "var_4": var[3]}

    return dict

# dict = prepare_train_set()

# print len(dict)

# arr = models.american_english.read_ngram_files(models.american_english.ngrams_filename, True)

# models.american_english.ngram_am(dict, arr, 2)
# models.american_english.ngram_am(dict, arr, 3)
# models.american_english.ngram_am(dict, arr, 4)
# models.american_english.ngram_am(dict, arr, 5)

# models.word2vec.word2vec(dict)

# models.microsoft_api.microsoft_api_model(dict, 2)
# models.microsoft_api.microsoft_api_model(dict, 3)
# models.microsoft_api.microsoft_api_model(dict, 4)
# models.microsoft_api.microsoft_api_model(dict, 5)
