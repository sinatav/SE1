from utils.connections import connect, get_decoded_data
from utils.dataCleaning import *
from utils.features import save_csv

base_url = 'https://search.codal.ir/api/search/v1/'
tag = 'companies'
url = base_url + tag

print("data fetched from:")
print(url)

page = connect(url)

data = get_decoded_data(page)

print("raw data dictionary is as below:")
print_raw_(data)

print("data dictionary after cleaning is as below:")
print_cleaned_(data)

save_csv(data, "test")

