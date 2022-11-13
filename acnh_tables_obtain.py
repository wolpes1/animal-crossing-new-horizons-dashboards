import pandas

def obtain_url(name = str):
    return f'https://nookipedia.com/wiki/{name}/New_Horizons'

def read_page(url):
    return pandas.read_html(url)

def get_table(page):
    return page[0]

def save_table(table, filename):
    table.to_excel(f'{filename}.xlsx')

def get_file_from_html(name = str, filename = str):
    url = obtain_url(name)
    page = read_page(url)
    table = get_table(page)
    save_table(table, filename)

get_file_from_html('bugs', 'acnh_insetos')
get_file_from_html('fish', 'acnh_peixes')