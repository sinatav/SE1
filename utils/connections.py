from urllib.request import urlopen
import ast


def connect(url):
    req = urlopen(url)
    page = req.read()

    return page


def get_decoded_data(page):
    data_list = ast.literal_eval(page.decode('utf-8'))

    return data_list
