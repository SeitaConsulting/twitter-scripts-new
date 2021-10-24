from bs4 import BeautifulSoup
from datetime import datetime
import config, message
import json
import os
import random
import requests
import time
import urllib.parse

import twitterlib

if __name__ == '__main__':
    print('Start at', datetime.now().strftime(config.format_time))

    # init
    api = twitterlib.Twitter(config)

    soup = BeautifulSoup(open('./socialdog.txt'), 'html.parser')
    links = soup.find_all('a')
    users = []

    flag = False
    for link in links:
        if link.text.startswith('@') and flag:
            users.append(link.text[1:])
        if link.text.endswith('bpe1o'):
            flag = True
            
    # run
    for user in users:
        api.remove(user)
        print(user)
        time.sleep(1)
        
    # done
    print('Finish at', datetime.now().strftime(config.format_time))
