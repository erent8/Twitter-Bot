import tweepy

# API anahtarlarınızı buraya giriniz.
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Tweepy API'sini başlatır
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Bir tweet gönder
api.update_status('Selam Twitter')

# Yeni mention'ları kontrol et ve yanıtla
for tweet in tweepy.Cursor(api.mentions_timeline).items():
    try:
        print(f'Mention from @{tweet.user.screen_name}')
        tweet.favorite()
        tweet.user.follow()
        api.update_status(f'@{tweet.user.screen_name} Merhaba!', in_reply_to_status_id=tweet.id)
    except tweepy.TweepError as e:
        print(e.reason)
