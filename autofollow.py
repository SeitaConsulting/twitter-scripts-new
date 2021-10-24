import config_0to1_consulting as config

from requests_oauthlib import OAuth1Session
import csv
import datetime
import json
import random
import time

def follow(user_id):
    endpoint = 'https://api.twitter.com/1.1/friendships/create.json'
    params = {
        'user_id': user_id
    }

    count = 0
    res = None
    finished = False
    while not finished:
        try:
            res = t.post(endpoint, params)
            finished = True
        except:
            count += 1
            if count > 5:
                return { 'error': 'Retrying limit exceeded.' }
            time.sleep(30)

    return json.loads(res.text)

def get_history():
    path = '{}/history.csv'.format(config.wd)

    history = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            history.append(row[1])
    print(history)
    return history

def add_to_history(row):
    path = '{}/history.csv'.format(config.wd)
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def get_followers(user_id, count, cursor):
    endpoint = 'https://api.twitter.com/1.1/followers/list.json'
    params = {
        'user_id': user_id,
        'count': count, #max 200
        'cursor': cursor
    }

    res = t.get(endpoint, params=params)
    return json.loads(res.text)

def get_list_members(list_id):
    endpoint = 'https://api.twitter.com/1.1/lists/members.json'
    params = {
        'list_id': list_id,
        'count': 5000
    }

    res = t.get(endpoint, params=params)
    return json.loads(res.text)

def get_relationships(user_ids):
    endpoint = 'https://api.twitter.com/1.1/friendships/lookup.json'
    params = {
        'user_id': user_ids,
    }

    res = t.get(endpoint, params=params)
    return json.loads(res.text)

def now():
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def run():
    print('Started at', now())
    
    list_members = get_list_members(list_id)['users']
    member = random.choice(list_members)

    count = 0
    cursor = -1
    finished = False
    loop = 0
    while not finished:
        res = get_followers(
            user_id=member['id'],
            count=100,
            cursor=cursor
        ) #The reason count is 100 is the limit of relationship below.
        followers = res['users']
        cursor = res['next_cursor']

        user_ids = []
        for follower in followers:
            user_ids.append(str(follower['id']))
        user_ids = ','.join(user_ids)

        relationships = get_relationships(user_ids)
        for relationship in relationships:
            if 'following' not in relationship['connections'] and 'blocking' not in relationship['connections'] and 'followed_by' not in relationship['connections'] and relationship['id_str'] not in log:
                res = follow(relationship['id'])
                if not 'errors' in res:
                    add_to_history([now(), relationship['id']])
                    count += 1
                time.sleep(5)
            if count == 25: #limit per an execution
                finished = True
                break

        loop += 1
        if loop % 15 == 0:
            time.sleep(925)
        
    print('Ended at', now())


if __name__ == '__main__':
    #initalize
    list_id = 1164816424260403200 #CEO
    log = get_history()
    t = OAuth1Session(
        config.CONSUMER_KEY,
        config.CONSUMER_SECRET,
        config.ACCESS_TOKEN,
        config.ACCESS_TOKEN_SECRET
    )

    #run
    run()
