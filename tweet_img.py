import os
import time
import tweepy
consumer_key="shfmjmVN1v4DKFzXzedFOboku"
consumer_secret="6KNBjelFLxiEQ3q4SF1NenOmTR1He9JgZbnCcAxNsIsFkLREoz"
access_token="	969421023471915009-boQ6xDZ8wi5QndehpBzR7kjdjqhrXWc"
access_token_secret="9MhLSVp8h1rwObv2SCpzHpdfp5IM54sgAHnbd2MFJrvU7"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/user/desktop/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 900*600"+img
    os.system(cmd)
    print("pic taken")
    #read image from location
    file=open(img, 'rb')
    data=file.read()
    api.update_with_media(img,status="nice")
    print("wait for 5 seconds")
    a=a+1
    b=b+1
    print("success")
