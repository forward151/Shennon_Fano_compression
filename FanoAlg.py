dict_range = {}
res = []
dict_res = {}

def Prepar(string):
    global dict_range, res
    dict_range = {}
    res = []
    string = string
    matrix = []
    for i in string:
        dict_range[i] = round(string.count(i) / len(string), 10)

    dict_range = {i[0]: i[1] for i in sorted(dict_range.items(), key=lambda x: x[1], reverse=True)}
    for i in dict_range:
        matrix.append([i, dict_range[i], ''])
    return matrix

def Fano(matrix):
    global res
    range_dist = 10000000
    xi = 0
    for i in range(len(matrix)):
        list1 = []
        list2 = []
        str_only_symbols = ''.join([i[0] for i in matrix])
        for j in str_only_symbols[0:i]:
            list1.append(dict_range[j])
        for j in str_only_symbols[i::]:
            list2.append(dict_range[j])
        if abs(sum(list1) - sum(list2)) < range_dist:
            range_dist = abs(sum(list1) - sum(list2))
            xi = i

    arr0, arr1 = [], []
    for i in matrix[:xi]:
        i[2] += '0'
        arr0.append(i)
    for i in matrix[xi:]:
        i[2] += '1'
        arr1.append(i)
    if len(arr1) == 1:
        res.append(arr1)
    else:
        Fano(arr1)
    if len(arr0) == 1:
        res.append(arr0)
    else:
        Fano(arr0)
    return res

