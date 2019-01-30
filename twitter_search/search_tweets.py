import tweepy

class TwitterSearch():
    def __init__(self):
        consumer_key = 'vPoMMxcDnog0qCeQu6breGyue'
        consumer_secret = 'rZ2xoBKk4bBMXk9FIoGDE1VLH5dJtLw9VNkqEDp6SGAkyawCwm'
        access_token = '1090486404671565824-LLIC9W1rw2lTaNvx9KT7AyVVSCefxx'
        access_token_secret = 'CEeWThZpkKbF4szc0pZXgqUnAJBjXtJXpGnjcwHcaLw3f'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def print_me(self):
        user = self.api.me()

    def get_tweets(self,keyword):
        response = []
        search = tweepy.Cursor(self.api.search, q=keyword, lang = 'en').items(30)
        for item in search:
            response.append({'name': item.user.name, 'screen_name': item.user.screen_name, 'tweet':item.text})
        return response