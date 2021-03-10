from IPython.display import display
import pandas as pd
import csv


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


def save_csv(data, name):
    with open(name + '.csv', 'w', newline='') as output:
        dict_writer = csv.DictWriter(output, data[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(data)


def display_dataframe(data):
    display(pd.DataFrame(data))
