from utils.dataCleaning import *
from utils.connections import *

url = 'https://search.codal.ir/api/search/v1/companies'

con = int(input("for crawling data enter 1:\n"))
if con == 1:
    print("data is crawling from source destination:")
    data = get_decoded_data(connect(url))
    print("data is saved in a dict form")
else:
    exit()


