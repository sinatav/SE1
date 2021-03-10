from utils.dataCleaning import *
from utils.connections import *
from utils.features import *

url = 'https://search.codal.ir/api/search/v1/companies'

con = int(input("for crawling data enter 1:\n"))
if con == 1:
    print("data is crawling from source destination:")
    data = get_decoded_data(connect(url))
    print("data is saved in a dict form")
    op1 = int(input("wanna clean data?\n1. yes\t2. no\n"))
    if op1 == 1:
        data = clean_data(data)
    op1 = int(input("wanna see raw data or in a dict form?\n1. raw\t2. dict\n"))
    if op1 == 1:
        show_data_raw(data)
    elif op1 == 2:
        show_dict_data(data)
    op1 = int(input("wanna save csv?\n1. yes\t2. no\n"))
    if op1 == 1:
        name = input("what will be the name of your file?\n")
        save_csv(data, name)

else:
    exit("BYEEEEE!")
