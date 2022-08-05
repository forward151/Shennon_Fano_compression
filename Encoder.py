from FanoAlg import Prepar, Fano

def encoder(filename1, filename2, filein, textin):
    if filein:
        file1 = open(filename1, 'r',  encoding='utf-8')
        string = file1.read()
        str_spl = string.split('\n')
        file1.close()
        if str_spl[0] == 'CODE':
            raise BaseException
        else:
            string = '\n'.join(str_spl[1::])
    else:
        if textin == '':
            return [], ''
        string = textin

    dict_res = {}

    matrix = Prepar(string)

    res = Fano(matrix)
    for i in res:
        if i[0][0] == '\n':
            dict_res['Line Break'] = i[0][2]
        else:
            dict_res[i[0][0]] = i[0][2]
    local_list = []
    for i in string:
        if i == '\n':
            local_list.append(dict_res['Line Break'])
        else:
            local_list.append(dict_res[i])
    res_str = ''.join(local_list)
    if filein:
        File = open(filename2, 'w', encoding='utf-8')
        File.write('CODE\n')
        for i in dict_res:
            File.write(f'{i} : {dict_res[i]}\n')
        File.write('\n')
        File.write(str(res_str))
        File.close()
        return None
    else:
        lst = []
        for i in dict_res:
            lst.append(f'{i} : {dict_res[i]}\n')
        return lst, res_str
