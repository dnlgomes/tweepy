__author__ = 'dnlgomes'
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import csv
#from time import gmtime, strftime


ckey = 'R8LEox3sb0HKLGkSXCzJQQ'
csecret = 'T6pInsq6NVD2cSlrE2aeXqFCKL97dpyJcqr4snNk'
atoken = '214180610-CWauPhpsfZkfKfUk8LjnPFoCyO9oAW7RrSvwU5Mr'
asecret = 'dfBkGwqrwkcAyUGdxzriOcDtOooOftkib1xW6gSPaN4'

class listener(StreamListener):
   global mentions
   mentions = []

   def on_data(self, data):

       decoded = json.loads(data)
       mention = [ decoded['created_at'],
                            decoded['id_str'],
                            decoded['user']['screen_name'],
                            decoded['text'].encode('ascii', 'ignore'),
                            decoded['in_reply_to_status_id_str'],
                            decoded['in_reply_to_screen_name'] ]

       mentions.append(mention)
       print decoded['text'].encode('ascii', 'ignore')
       print len(mentions)


       if len(mentions) == 100:#instead of length will be time strftime("%Y-%m-%d %H:%M:%S", gmtime())
           with open('mentions2.csv', 'wb') as csvfile:#name the file with the date
              csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
              csv_writer.writerow("created_at", "tweet_id", "reply_screen_name", "text", "in_reply_to_status_id_str", "in_reply_to_screen_name")
              for x in mentions:
                 csv_writer.writerow([x[y] for y in range( len(mentions[0]) )])



# for m in mentions:
# 	         csv_writer.writerow( m[y] for y in range( len(mentions[0])) )


       # with open('mentions.csv', 'a') as csvfile:
       #     writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
       #     writer.writerow(mention)


       return True

   def on_error(self, status_code):
       print status_code

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
candidates = ["@LynneForMayor", "@nelsondiaz2015", "@JimFKenney", "@DO2015PHL",
                "@Tmiltonstreet", "@SenTonyWilliams", "@melissaformayor", "@Akalady5"]
twitterStream = Stream(auth, listener())
twitterStream.filter(track=candidates)