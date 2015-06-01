__author__ = 'dnlgomes'
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import csv
from time import gmtime, strftime


ckey = 'R8LEox3sb0HKLGkSXCzJQQ'
csecret = 'T6pInsq6NVD2cSlrE2aeXqFCKL97dpyJcqr4snNk'
atoken = '214180610-CWauPhpsfZkfKfUk8LjnPFoCyO9oAW7RrSvwU5Mr'
asecret = 'dfBkGwqrwkcAyUGdxzriOcDtOooOftkib1xW6gSPaN4'

class listener(StreamListener):
   global mentions
   mentions = []
   global today
   today = '2015-06-01 11:47:10'#strftime("%Y-%m-%d")
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
       print strftime("%Y-%m-%d %H:%M:%S")

       global today
       if strftime("%Y-%m-%d %H:%M:%S") > today:#instead of length will be time strftime("%Y-%m-%d %H:%M:%S", gmtime()) per hour
           today = strftime("%Y-%m-%d") + " 23:59:59"
           #write per hour
           with open('mentions' + strftime("%Y-%m-%d") + '.csv', 'wb') as csvfile:#name the file with the date
              csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
              header = "created_at" + "," + "tweet_id" + "," + "reply_screen_name" + "," + "text" + "," + "in_reply_to_status_id_str" + "," + "in_reply_to_screen_name"
              csv_writer.writerow(header)
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
                "@Tmiltonstreet", "@SenTonyWilliams", "@melissaformayor", "@Akalady5", "@HillaryClinton"]
twitterStream = Stream(auth, listener())
twitterStream.filter(track=candidates)