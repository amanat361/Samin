import praw
import time
import random

r = praw.Reddit(user_agent = "Good Steam Games by Samin /u/amanat361bot")
r.login(disable_warning=True)

steam_games = ['[Grand Theft Auto 5](http://store.steampowered.com/app/271590/)', '[No Man\'s sky](http://store.steampowered.com/app/275850/)', '[Doom](http://store.steampowered.com/app/379720/)', '[ARK: Survival Evolved](http://store.steampowered.com/app/346110/)', '[Rocket League](http://store.steampowered.com/app/252950/)']
words_to_match = ['link me a good game', '!game', 'what is a good game', 'what\'s a good game', 'link me a game']
cache = []

def run_bot():
      
    print "Getting Subreddit..."
    subreddit = r.get_subreddit("pcmasterrace")
    
    print "Getting Comments..."
    comments = subreddit.get_comments(limit=25)
    
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        
        if comment.id not in cache and isMatch:
            comment.reply("{} is a great game!\n\n -----  \n\n  This action was done automatically, if you have any questions or concerns, contact the creator: /u/amanat361".format(random.choice(steam_games)))     
            
            print "Mission Accomplished"
        
            cache.append(comment.id)
            
    print "Loop finished, wait 10 seconds."   
         
while True:
    run_bot()
    time.sleep(10)