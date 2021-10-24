from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl, urlsplit
import config

consumer_key = config.key_api
consumer_secret = config.key_apisecret

request_token_url = 'https://api.twitter.com/oauth/request_token'
# Twitter Application Management で設定したコールバックURLsのどれか
oauth_callback = "https://seita-consulting.com"

twitter = OAuth1Session(consumer_key, consumer_secret)

response = twitter.post(
    request_token_url,
    params={'oauth_callback': oauth_callback}
)

# responseからリクエストトークンを取り出す
request_token = dict(parse_qsl(response.content.decode("utf-8")))

access_token_url = 'https://api.twitter.com/oauth/access_token'
# リクエストトークンから連携画面のURLを生成
authenticate_url = "https://api.twitter.com/oauth/authenticate"
authenticate_endpoint = '%s?oauth_token=%s' \
    % (authenticate_url, request_token['oauth_token'])

print(authenticate_endpoint)

print('url:')
url = input()

qs = urlsplit(url).query
qs_d = dict(parse_qsl(qs))

oauth_token = qs_d['oauth_token']
oauth_verifier = qs_d['oauth_verifier']

twitter = OAuth1Session(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_verifier,
)

response = twitter.post(
    access_token_url,
    params={'oauth_verifier': oauth_verifier}
)

# responseからアクセストークンを取り出す
access_token = dict(parse_qsl(response.content.decode("utf-8")))

print(access_token)
