import models.american_english

gram_num = 3

f = open(models.american_english.ngrams_filename[gram_num - 2], 'r')
dict = {}
arr_bcd = []
arr_cd = []

for i in f.readlines():
    s = i.replace("\n", "").replace("\r", "")
    i_split = s.split("\t")

    arr_bcd.append(i_split[1:] + [int(i_split[0])])
    arr_cd.append(i_split[2:] + [int(i_split[0])])

print arr_bcd[0]
print arr_cd[0]

last = arr_bcd[0][0:(gram_num - 1)]
num = arr_bcd[0][-1]

some_arr = []

for i in xrange(len(arr_bcd)):
    if (last == arr_bcd[i][0:(gram_num - 1)]):
        num += arr_bcd[i][-1]
        some_arr.append(i)

    if (last == arr_bcd[i][0:(gram_num - 1)] and i == 1):
        some_arr.append(0)

    if (last != arr_bcd[i][0:(gram_num - 1)] and not (last == arr_bcd[i][0:(gram_num - 1)] and i == 1)):
        for j in some_arr:
            arr_bcd[j][-1] = arr_bcd[j][-1] / (num + 0.0)
        num = 0
        some_arr = []

    last = arr_bcd[i][0:(gram_num - 1)]

for i in xrange(len(arr_bcd)):
    if (arr_bcd[i][-1] > 1):
        arr_bcd[i][-1] = 1

for i in xrange(len(arr_cd)):
    if (last == arr_cd[i][0:(gram_num - 1)]):
        num += arr_cd[i][-1]
        some_arr.append(i)

    if (last == arr_cd[i][0:(gram_num - 1)] and i == 1):
        some_arr.append(0)

    if (last != arr_cd[i][0:(gram_num - 1)] and not (last == arr_cd[i][0:(gram_num - 1)] and i == 1)):
        for j in some_arr:
            arr_cd[j][-1] = arr_cd[j][-1] / (num + 0.0)
        num = 0
        some_arr = []

    last = arr_cd[i][0:(gram_num - 1)]

for i in xrange(len(arr_cd)):
    if (arr_cd[i][-1] > 1):
        arr_cd[i][-1] = 1

# print arr_bcd[0]
print arr_cd
