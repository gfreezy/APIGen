def change_dict(type_dict, immutable_dict):
    return_dict = {}
    for i,j in type_dict.items():
        if j == 'int':
            return_dict[i] = immutable_dict.get(i, type=int)
    return return_dict
