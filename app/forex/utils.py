import requests
from bs4 import BeautifulSoup
import numpy as np
import datetime
import time

def make_the_soup(url, timer_mean=3, timer_std=4):

    # Waiting during a random time around timer_mean sec.
    time.sleep(abs(np.random.randn()*timer_std + timer_mean))
    # Getting the current time
    now = datetime.datetime.now()
    # Making the soup
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    return soup, now

def get_currency(soup, now):

    dict_values = {
        'year' : now.year,
        'month' : now.month,
        'day' : now.day,
        'hour' : now.hour,
        'minute' : now.minute,
        'second' : now.second
    }
    for tr in soup.find('table').find_all('tr'):
        if tr.find_all('td'):
            dict_values[tr.find_all('td')[0].text.strip()] = np.float(tr.find_all('td')[1].text.strip().replace(',','.'))

    header = str(list(dict_values.keys()))[1:-1].replace('\'','')
    data = np.array([list(dict_values.values())])

    return header, data

def dump_data(f, data):

    np.savetxt(f, data)
    f.flush()
    time.sleep(0.1)
