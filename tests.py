from utils.connections import connect, get_decoded_data

base_url = 'https://search.codal.ir/api/search/v1/'
tag = 'companies'
url = base_url + tag

print(url)

page = connect(url)

data = get_decoded_data(page)

for i in data:
    print(i)
