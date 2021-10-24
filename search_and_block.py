from datetime import datetime
import config
import json
import random
import time
import urllib.parse

import twitterlib

def read_cursor(path):
    with open(path, 'r') as f:
        data = f.read()
    return int(data)

def write_cursor(cursor, path):
    with open(path, 'w') as f:
        f.write(str(cursor))

if __name__ == '__main__':
    print('Start at', datetime.now().strftime(config.format_time))

    # init
    api = twitterlib.Twitter(config)
    path = config.path + '/db/' + __file__.replace('.py', '') + '-' + 'cursor.txt'
    query = '#安倍晋三の不起訴処分に抗議します'
    
    # run
    count = 20
    cursor = read_cursor(path)
    epoch = 1
    for i in range(epoch):
        params = {
            'q': query,
            'result_type': 'mixed',
            'count': count
        }
        res = api.search_tweets(params)
        print(res)
        print(res.keys())

    # done
    print('Finish at', datetime.now().strftime(config.format_time))
