# -*- coding: utf-8 -*-

import gensim


def word2vec(dict):
    model = gensim.models.Word2Vec. \
        load_word2vec_format('/Users/Nurislam/Downloads/GoogleNews-vectors-negative300.bin', binary=True)

    # доля правильных ответов
    true_answers = 0

    # идём по словарю
    for i in dict:
        text = dict[i]["text"]

        text_split = text.split(" ")

        text_all_in_model = []

        for j in text_split:
            try:
                d = model[j]
                text_all_in_model.append(j)
            except:
                None

        text_split = text_all_in_model

        vars = [dict[i]["var_1"], dict[i]["var_2"], dict[i]["var_3"], dict[i]["var_4"]]

        new_v = []
        for j in vars:
            try:
                d = model[j]
                new_v.append(j)
            except:
                None

        vars = new_v

        # если все нулевые

        if (len(text_split) == 0):
            continue

        marker = False

        for j in vars:
            if (len(j) != 0):
                marker = True

        if not (marker):
            continue

        # если какого-то слова нет, то по каждому идти

        var_sim = []

        for j in vars:
            if not (len(j) == 0):
                var_sim.append(model.n_similarity(text_split, [j]))
            else:
                var_sim.append(0)

        m = max(var_sim)

        answer = var_sim.index(m)

        if (dict[i]["var_" + str(answer + 1)] == dict[i]["answer"]):
            true_answers += 1

    print (true_answers / (len(dict) + 0.0))
