import os
import json

def dist(old_el_list, new_el, prag):
    distante = [0 if abs(el[0] - new_el[0]) < prag else 1 for el in old_el_list]
    return sum(distante) == len(old_el_list)

def solve_captcha(fname):
    captcha_data = json.load(open(fname, 'r'))
    new_dict = {}
    for k, v in captcha_data.items():
        new_items = [v[0]]
        for i in range(1, len(v)):
            if dist(new_items, v[i], v[0][1]):
                new_items += [v[i]]
        new_dict[k] = new_items
    lista_grupari = []
    for k, v in new_dict.items():
        for grp in v:
            lista_grupari += [(k, grp)]
    sortate_dupa_X = sorted(lista_grupari, key=lambda x: x[1][0])
    #-------------------------------------------------------------
    final_groups = []
    index = 0
    while index < len(sortate_dupa_X):
        grupare = [sortate_dupa_X[index]]        
        for i in range(index + 1, len(sortate_dupa_X)):
            if abs(grupare[0][1][0] - sortate_dupa_X[i][1][0]) < grupare[0][1][1]:
                grupare += [sortate_dupa_X[i]]
            else:
                break
        final_groups += [grupare]
        index = i
        if index == len(sortate_dupa_X) - 1:
            break
    captcha_text = [sorted(group, key=lambda x : x[1][2])[0] for group in final_groups]
    final_captcha = "".join([pair[0] for pair in captcha_text])
    return final_captcha

for fis in os.listdir("date_captcha"):
    full_path = os.path.join("date_captcha", fis)
    text = solve_captcha(full_path)
    print(fis, text)