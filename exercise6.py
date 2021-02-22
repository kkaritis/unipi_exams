import tweepy

ACCESS_TOKEN ="1350825370598182914-GP0fRhEZ59UQvGkA95LihzoN2JjOnM"
ACCESS_SECRET ="5wa6V69y3uasjurIvMPq4cMJ79O7upegjzU6P2lj33bQ4"
CONSUMER_KEY ="IX3rDYM2XN6r23nHX4ZCzVU0L"
CONSUMER_SECRET ="6jZJn0CD9ATMNuy0kRON9M3UWuD3LNXjQtQM1Q81D8buJjnfHx"


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

api = connect_to_twitter_OAuth()

#project start
user = input("give user's name ")
word_list=[]
persontweets = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in persontweets:
    word_list.append(tweet.text)

lekseis=[]
for tweet in word_list:
    spasmeno = tweet.split()
    lekseis = lekseis + spasmeno

def Sorting(lekseis):
    lekseis.sort(key=len)
    return lekseis

print(Sorting(lekseis))

SYMBOLS = '{}()[].,:;+-*/&|_#!@$%^><\?`=~'

results = []
for element in lekseis:
    temp = ""
    for ch in element:
        if ch not in SYMBOLS:
            temp += ch

    results.append(temp)


for i in range(5):
    print(results[i])

for j in reversed(range(len(results)-5,len(results))):
    print(results[j])