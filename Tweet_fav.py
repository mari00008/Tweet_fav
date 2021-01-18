#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy

api_key = '**********'
api_secret = '**********'
access_token = '**********'
access_token_secret = '**********'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.user_timeline, id="************").items() #idを調査対象のTwitterIDに置き換える

dic = {}

for status in tweets:
        ID = status.id 
        url = "https://twitter.com/matsu_bouzu/status/" + str(ID) # ツイートのURL
        fav = status.favorite_count
        fav = int(fav) # いいね数を文字列から数値に変換
        dic[url]=fav # URLといいね数紐づけ


dic2 = sorted(dic.items(), key=lambda x:x[1])
for tweet in dic2: # いいね数が多い順でツイートを取り出す
    print("いいね数:", tweet[1]) # ツイートのいいね数を表示
    print(tweet[0]) # ツイートのURLを表示

