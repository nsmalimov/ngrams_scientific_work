import models.american_english


def reformat_to_probability(arr, gram_num):
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

    dict = {}

    for i in arr:
        dict[" ".join(i[0:2])] = i[-1]

    return dict


def read_data(gram_num):
    f = open(models.american_english.ngrams_filename[gram_num - 2], 'r')
    dict = {}
    arr = []
    for i in f.readlines():
        s = i.replace("\n", "").replace("\r", "")
        i_split = s.split("\t")

        arr.append(i_split[1:] + [int(i_split[0])])

        s = ""
        for j in i_split[1:]:
            s += j + " "
        s = s[:-1]
        dict[s] = int(i_split[0])

    f.close()

    return dict, arr


gram_num = 2
dict, arr = read_data(gram_num)

dict_proba = reformat_to_probability(arr, gram_num)

print len(dict)

p_ab = 1 / (len(dict) + 0.0)

res_arr = []

dict_1 = {}

for i in dict:
    try:
        num_1 = dict[i]
        res = p_ab * dict_proba[i]
        res_arr.append((res - dict_proba[i]) ** 2)
    except:
        print i

print sum(res_arr) / (len(res_arr) + 0.0)
