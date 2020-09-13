import utils
import os
import time
import numpy as np

url = 'https://api.kraken.com/0/public/Ticker'
pair = 'XXBTZEUR'
finename = '../data/XXBTZEUR.csv'

if __name__ == '__main__':

    #Create dump file if not created (not tracked by git)
    if not os.path.exists('../../data/'):
        os.makedirs('../../data/')

    page, now = utils.get_api_result(url, pair&
    header, data = utils.get_currency(page, now, pair)

    with open(finename, 'wb') as f:
        np.savetxt(f, data, header=header)
        try:
            while True:
                page, now = utils.get_api_result(url, pair)
                header, data = utils.get_currency(page, now, pair)
                utils.dump_data(f, data)
                print('{0} data loaded at '.format(pair), now.hour, ':', now.minute, ':', now.second)
                time.sleep(30)

        except KeyboardInterrupt:
            print('Manual break by user')
