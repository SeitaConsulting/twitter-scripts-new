from requests_oauthlib import OAuth1Session

class Twitter:
    def __init__(self, config):
        ka = config.key_api
        kas = config.key_apisecret
        kt = config.key_token
        kts = config.key_tokensecret
        self.twitter = OAuth1Session(ka, kas, kt, kts)

    def unblock(self, user_id):
        endpoint = 'https://api.twitter.com/1.1/blocks/destroy.json'

        params = {
            'user_id': user_id,
            'include_entities': False,
            'skip_status': True
        }
        return self.twitter.post(endpoint, params=params)
        
    def get_followers(self, user_id, count, cursor):
        endpoint = 'https://api.twitter.com/1.1/followers/list.json'
  
        params = {
            'user_id': user_id,
            'count': count,
            'cursor': cursor
        }
        return self.twitter.get(endpoint, params=params)

    def get_blocks(self):
        endpoint = 'https://api.twitter.com/1.1/blocks/list.json'

        params = {
            'include_entities': False,
            'skip_status': True
        }
        return self.twitter.get(endpoint, params=params)

    def mute(self, user_id):
        endpoint = 'https://api.twitter.com/1.1/mutes/users/create.json'

        params = {
            'user_id': user_id,
        }
        return self.twitter.post(endpoint, params=params)

    def remove(self, screen_name):
        endpoint = 'https://api.twitter.com/1.1/friendships/destroy.json'

        params = {
            'screen_name': screen_name
        }
        return self.twitter.post(endpoint, params=params)
        
    def search_tweets(self, params):
        endpoint = 'https://api.twitter.com/1.1/search/tweets.json'

        return self.twitter.get(endpoint, json=params)
    
    def send_dm(self, recipient_id, text):
        endpoint = 'https://api.twitter.com/1.1/direct_messages/events/new.json'

        json = {
            'event': {
                'type': 'message_create',
                'message_create': {
                    'target': {
                        'recipient_id': recipient_id
                    },
                    'message_data': {
                        'text': text
                    }
                }
            }
        }
        return self.twitter.post(endpoint, json=json)

    def tweet(self, status):
        endpoint = 'https://api.twitter.com/1.1/statuses/update.json'
        params = {
            'status': status
        }
        
        return self.twitter.post(endpoint, params=params)
