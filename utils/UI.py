from utils.dataCleaning import *
from utils.connections import *
from utils.features import *

url = 'https://search.codal.ir/api/search/v1/companies'

con = int(input("for crawling data enter 1:\n"))
if con == 1:
    print("data is crawling from source destination:")
    data = get_decoded_data(connect(url))
    print("data is saved in a dict form")
    op1 = int(input("wanna see data?\n1. yes\t2. no\n"))
    if op1 == 1:
        show_data_raw(data)
else:
    exit("BYEEEEE!")


