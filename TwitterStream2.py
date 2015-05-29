__author__ = 'dnlgomes'
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import  csv


ckey = 'R8LEox3sb0HKLGkSXCzJQQ'
csecret = 'T6pInsq6NVD2cSlrE2aeXqFCKL97dpyJcqr4snNk'
atoken = '214180610-CWauPhpsfZkfKfUk8LjnPFoCyO9oAW7RrSvwU5Mr'
asecret = 'dfBkGwqrwkcAyUGdxzriOcDtOooOftkib1xW6gSPaN4'

class listener(StreamListener):
   global mentions
   mentions = []

   def on_data(self, data):

       decoded = json.loads(data)
       print decoded['text'].encode('ascii', 'ignore')
       return True

   def on_error(self, status_code):
       print status_code

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

hashtags = ["#ronaldreagan","#congress","#troopthanks","#republicans","#donttreadonme","#proudamerican","#takebackamerica","#president","#libertarian","#politics","#america","#freemarket","#patriot","#capitalism","#constitution","#usa","#rights","#god","#conservativepolitics","#sonsofliberty","#gun","#liberty","#conservative","#power","#election2016","#teaparty","#freedom","#country","#gop","#independence",
            "#clinton","#johnkerry","#randpaul","#hillaryforprison2016","#democratssuck","#jebbush","#election","#jeb2016","#poll","#democrat","#barackobama","#republican","#florida","#bush2016","#johnmccain","#rubio","#electoralcollege","#mittromney","#kerry2016","#billclinton","#ohio","#hillary","#philippinepolitics","#cray","#thedailyshow","#stayalittlebitlonger","#hilarious","#segment","#jonstewart","#democrats",
            "#voteordie","#getoutandvote","#president2016","#dankmemes","#publicprank","#tedcruz","#crazy","#voting","#howtobasic","#hillaryclinton","#vote2016","#vitaly","#prank","#mairou","#trolling","#democracy","#helsinki","#suomi","#rautatieasema","#finland","#obama","#maailmakylassa","#gopro","#mk2015","#comedy","#banana","#finally","#futurama","#zoidberg4prez","#zoidberg",
            "#republicofzoidberg","#repost","#benghazi","#clinton2016","#cruz2016","#stophillary","#treason","#iowa","#portsmouth","#berniesanders","#artcups","#froth","#santorum","#gif","#gifnews","#ricksantorum","#art","#streetart","#scottwalker","#fletch"]

twitterStream = Stream(auth, listener())
twitterStream.filter(track=hashtags)