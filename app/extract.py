import utils
import os
import time
import numpy as np

url = 'https://investir.lesechos.fr/traders/forex/'

if __name__ == '__main__':

    #Create dump file if not created (not tracked by git)
    if not os.path.exists('../data/'):
        os.makedirs('../data/')

    finename = '../data/forex.csv'

    soup, now = utils.make_the_soup(url)
    header, data = utils.get_currency(soup, now)

    with open(finename, 'wb') as f:
        np.savetxt(f, data, header=header)
        try:
            while True:
                soup, now = utils.make_the_soup(url)
                header, data = utils.get_currency(soup, now)
                utils.dump_data(f, data)
                print('Forex currency data loaded at ', now.hour, ':', now.minute, ':', now.second)
                time.sleep(180)

        except KeyboardInterrupt:
            print('Manual break by user')
