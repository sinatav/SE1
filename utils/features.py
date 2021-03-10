def show_data_raw(data):
    for L in list(data[0].keys()):
        print(L, end='\t')
    print()
    for L in data:
        for J in list(L.values()):
            print(J, end='\t')
        print()


def show_dict_data(data):
    for i in data:
        print(i)
