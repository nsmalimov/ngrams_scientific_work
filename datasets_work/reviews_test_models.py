# -*- coding: utf-8 -*-

import csv
import random
import sys

from utils.processing_text import *

csv.field_size_limit(sys.maxsize)

reload(sys)
sys.setdefaultencoding('utf-8')
sys.getdefaultencoding()

# id	question	correctAnswer	answerA	answerB	answerC	answerD
train_file = "testData.tsv"


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

    count = 0

    for i in train_set:

        id = i[0]

        text_split = i[1].split(".")

        # выбрали какое-то предложение
        sentence = text_split[random.randint(0, len(text_split) - 1)]

        sentence = processing_text(sentence)

        sentence_split = sentence.split(" ")

        if (len(sentence_split) < 8):
            continue

        if ('' in sentence_split):
            continue

        for j in sentence_split:
            if not (j.isalpha()):
                continue

        sentence_split = sentence_split[0:8]

        vars = [sentence_split[4], sentence_split[5], sentence_split[6], sentence_split[7]]

        random.shuffle(vars)

        dict[id] = {"text": " ".join(sentence_split), "answer": vars[vars.index(sentence_split[4])],
                    "var_1": vars[0], "var_2": vars[1],
                    "var_3": vars[2], "var_4": vars[3]}

        count += 1

        if (count > 200):
            break

    return dict
