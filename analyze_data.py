import json

tweetsList = []
print("Lese json Datei")
with open('tweets.json') as f:
    for line in f:
        if line.rstrip():
            tweetsDict = json.loads(line)
            tweetsList.append(tweetsDict)



print("Printing each JSON Decoded Object")
for tweet in tweetsList:
    text = str(tweet["text"]).splitlines()


    print("Tweet ID: " + tweet["id_str"] + " Text: " + str(text))
