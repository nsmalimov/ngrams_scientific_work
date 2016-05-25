import json

import utils.api_microsoft


def microsoft_api_model(dict, num_gram):
    num = 0
    count_correct = 0

    for i in dict:
        print num
        num += 1

        text = dict[i]["text"]
        text_split = text.split(" ")

        query = {
            "queries":
                [
                    {
                        "words": " ".join(text_split[-(num_gram - 1):]),
                        "word": dict[i]["var_1"]
                    },
                    {
                        "words": " ".join(text_split[-(num_gram - 1):]),
                        "word": dict[i]["var_2"]
                    },
                    {
                        "words": " ".join(text_split[-(num_gram - 1):]),
                        "word": dict[i]["var_3"]
                    },
                    {
                        "words": " ".join(text_split[-(num_gram - 1):]),
                        "word": dict[i]["var_4"]
                    }
                ]
        }

        answer = utils.api_microsoft.make_post_api_microsoft(num_gram, str(query))

        if (answer is None):
            continue

        answer = json.loads(answer)

        try:
            res_arr = answer["results"]
        except:
            print answer
            continue

        prob_arr = []

        for j in res_arr:
            prob_arr.append(float(j["probability"]))

        predict_ans = prob_arr.index(max(prob_arr))

        if (dict[i]['answer'] == dict[i]["var_" + str(predict_ans + 1)]):
            count_correct += 1

    print count_correct / (len(dict) + 0.0)
