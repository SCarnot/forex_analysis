import json
import requests
import time
import numpy as np
import datetime

def get_api_result(url, pair, timer_mean=0, timer_std=0.1):

    # Waiting during a random time around timer_mean sec.
    time.sleep(abs(np.random.randn()*timer_std + timer_mean))
    # Getting the current time
    now = datetime.datetime.now()
    # Making the soup
    data_url = url + '?pair={0}'.format(pair)
    page = json.loads(requests.get(data_url).text)

    return page, now

def get_currency(page, now, pair):

    dict_values = {
        'year' : int(now.year),
        'month' : int(now.month),
        'day' : int(now.day),
        'hour' : int(now.hour),
        'minute' : int(now.minute),
        'second' : int(now.second),
        'ask' : page['result'][pair]['a'][0],
        'bid' : page['result'][pair]['b'][0],
        'last trade closed' : page['result'][pair]['c'][0],
        'volume' : page['result'][pair]['v'][0],
        'volume weighted average price' : page['result'][pair]['p'][0]
    }
    dict_values = {keys: np.float(value) for keys, value in dict_values.items()}
    header = str(list(dict_values.keys()))[1:-1].replace('\'','')
    data = np.array([list(dict_values.values())])

    return header, data

def dump_data(f, data):

    np.savetxt(f, data)
    f.flush()
    time.sleep(0.1)
