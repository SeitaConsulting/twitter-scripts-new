from datetime import datetime
import config, message
import json
import os
import random
import time
import urllib.parse

import twitterlib

def get_message():
    msgs = message.msgs

    return random.choice(list(msgs.items())) #p, msg

def ngword_in(text):
    for word in config.ngwords:
        if word in text:
            return True

    return False

def read_log(path):
    ids = []
    with open(path, 'r') as f:
        ids.append(f.read().split(',')[0])
    return ids

def write_log(path, params):
    with open(path, 'a') as f:
        f.write('{},{}\n'.format(params['i'], params['p']))

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
    path = '{}/db/{}_{}'.format(config.path, os.path.basename(__file__).replace('.py', ''), 'cursor.txt')
    path2 = '{}/db/{}_{}'.format(config.path, os.path.basename(__file__).replace('.py', ''), 'log.txt')
    url = 'https://compath.seita-consulting.com'
    log = read_log(path2);
    
    # run
    count = 40
    cursor = read_cursor(path)
    epoch = 1
    for i in range(epoch):
        if cursor == 0:
            print('All done. Cursor is 0.')
            break
        
        res = api.get_followers(1340727282, count, cursor)
        res = json.loads(res.text)

        for user in res['users']:
            if not ngword_in(user['name']) and not ngword_in(user['description']) and not user['id_str'] in log:
                # generate message
                p, msg = get_message()
                
                # set params for analytics
                params = { #サイト側で追加したいのは、サイトの訪問日時、滞在時間、スクロール情報、サイトA/Bテストパターン
                    't': datetime.now().strftime(config.format_time), #メッセージの送信日時
                    'i': user['id_str'], #ユーザーID
                    'p': p, #メッセージのパターン
                    's': 'twitter_dm' #ソース
                }
                query = urllib.parse.urlencode(params)

                # insert url & query params into message
                msg = msg.replace('@@@query@@@', url + '?' + query)

                # send DM and wait a few second
                api.send_dm(user['id'], msg)
                write_log(path2, params)
                log.append(user['id_str'])
                time.sleep(config.time_sleep)
            else:
                print(user['screen_name'])
        
        cursor = res['next_cursor']
        write_cursor(cursor, path)

    # done
    print('Finish at', datetime.now().strftime(config.format_time))
