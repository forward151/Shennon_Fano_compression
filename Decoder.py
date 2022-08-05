def decoder(filename1, filename2, filein, textin):
    if filein:
        File = open(filename1, 'r')
        text = File.read()
        File.close()
        spl_txt = text.split('\n')
        if spl_txt[0] == 'TEXT':
            raise BaseException
        else:
            text = '\n'.join(spl_txt[1::])
    else:
        if textin == '':
            return ''
        text = textin
    code_dict = {}
    lst = text.split('\n')
    for i in lst:
        if i != '':
            if i[0] == ' ':
                code_dict[i.split(' ')[3]] = ' '
            elif i[0:2] == 'Li':
                code_dict[i.split(' ')[3]] = '\n'
            else:
                code_dict[i.split(' ')[2]] = i.split(' ')[0]
        else:
            break
    code_str = lst[-1]
    lst_out = []
    itr = ''

    for i in code_str:
        itr += i
        if itr in code_dict:
            if code_dict[itr] == 'Line Break':
                lst_out.append('\n')
            else:
                lst_out.append(code_dict[itr])
            itr = ''
            continue
    if filein:
        File2 = open(filename2, 'w')
        File2.write('TEXT\n')
        File2.write(''.join(lst_out))
        File2.close()
        return None
    else:
        return ''.join(lst_out)