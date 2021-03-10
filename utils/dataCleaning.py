def clean_data(data_list):
    for i in data_list:
        del i['t']
        del i['st']
    return data_list


def print_raw_(data):
    for i in data:
        print(i)
        

def print_cleaned_(data):
    cleaned_data = clean_data(data)
    
    print_raw_(cleaned_data)