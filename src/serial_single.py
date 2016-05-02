#!/usr/bin/python
import time
import serial
import tweepy
from secretkeys import keys # you need secretkeys.py for your oauth credentials

ser = serial.Serial('/dev/cu.usbserial-DN01AAWR', 9600)
message = ser.readline()

# Starts the api and auth
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Creates the post and logs to a file
def generate_post():

    output_text = ((message).decode())

    # Write the status to a file, for logging
    with open('history.txt', 'a') as f:
        f.write(output_text + '\n')

    return output_text
#generate_post()

# Post the status to Twitter
api.update_status(status=generate_post())