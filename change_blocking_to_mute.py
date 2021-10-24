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
    
    # run
    blocks = json.loads(api.get_blocks().text)
    for user in blocks['users']:
        api.unblock(user['id'])
        api.mute(user['id'])
        print(user['id'])

    # done
    print('Finish at', datetime.now().strftime(config.format_time))
