import copy
import pickle

import kaggle_test_models
import reviews_test_models


def data_from_kaggle():
    dict = kaggle_test_models.prepare_train_set()

    new_dict = {}
    for i in dict:
        text = dict[i]["text"]

        new_dict[i] = {}
        new_dict[i]["text"] = copy.deepcopy(text)
        new_dict[i]["answer"] = copy.deepcopy(dict[i]["answer"])

    return new_dict


def data_from_films_reviews():
    dict = reviews_test_models.prepare_train_set()
    new_dict = {}

    for i in dict:
        new_dict[i] = {}
        new_dict[i]["text"] = copy.deepcopy(dict[i]["text"])
        new_dict[i]["answer"] = copy.deepcopy(dict[i]["answer"])

    return new_dict


dict_1 = data_from_kaggle()
dict_2 = data_from_films_reviews()
dict = {}
dict.update(dict_1)
dict.update(dict_2)

f = open("data_sets_perplexity.pkl", "w")
pickle.dump(dict, f)
f.close()
