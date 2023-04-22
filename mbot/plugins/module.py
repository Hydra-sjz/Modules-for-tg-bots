
 

from telethon import TelegramClient, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.client import bots
from mbot.utils.weather import wtr
from requests import get
import os
import requests
import random
import calendar
from datetime import datetime
from mbot import bot

@bot.on(events.NewMessage(pattern='/srt'))
async def stahrt(event):
    """Send a message when the command /start is issued."""
    await event.respond('Hello :)')
    if event.is_channel:
        await event.respond('Activated Bot For Channel')
    if event.is_group:
        await event.respond('Activated Bot For Group Chat :)')
    if event.is_private:
        await event.respond('Activated Bot For Private Chat :)')
    user = event.chat_id
    full = await bot(GetFullUserRequest(user))
    userDetails = f'''New User ID = {user}\nOther Details:\n{full}'''
    print(userDetails)
    f = open("Textfiles/userData.txt", "a")
    f.write(userDetails)
    f.close()
    await event.respond('Click 👉🏻 /help to display list of all commands 😄')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/whoami'))
async def whoami(event):
    chatid = event.chat_id
    await event.reply(f"Your chat id is: `{chatid}`")


@bot.on(events.NewMessage(pattern='hey'))
async def hey(event):
    await event.reply(f"Hello!")


@bot.on(events.NewMessage(pattern='/hlp'))
async def henlp(event):
    helpText = '''
List Of all Commands
/start - To Start The Bot
/help - Display List of all Commands
/whoami - Displays You User Id of Telegram
/joke - Displays a Random Joke
/news - Displays a Top 20 Headlines
/website - gives you our website link
/truthNdare - Truth and Dare Game instructions and command
/insult - gives an insulting line
/today - returns today's date and time
Useless Commands:
/KaisaHaiBhai - EasterEgg
/wassup - EasterEgg
Some Other Useful Links:
GitHub: https://github.com/QuantumByteStudios
QuantumByteChat: https://t.me/quantumbytechat
Website: https://quantumbyte.studio/
Share this bot with your friends: http://t.me/QuantumByteStudios_bot
You Can Add This Bot To Your Telegram Groups and Channels :)
    '''
    await event.respond(f"{helpText}")


@bot.on(events.NewMessage(pattern='/wassup'))
async def wassup(event):
    message = "I am Fine Thanks for Asking :)"
    await event.reply(f"{message}")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/KaisaHaiBhai'))
async def wassup(event):
    message = "Ekdum MAST Bhai😎, Tu Bata?"
    await event.reply(f"{message}")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/joke'))
async def joke(event):
    joke = get("https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun?blacklistFlags=nsfw,religious,political&type=twopart").json()
    setup = joke["setup"]
    delivery = joke["delivery"]
    await event.reply(f"{setup}\n\n{delivery}")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/news'))
async def news(event):
    newsapi = os.environ.get("NEWS_API")
    query_params = {
        "source": "news-api",
        "sortBy": "top",
        "apiKey": newsapi
    }
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=5f1413a68acb460bacbbc67e5d100386"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_api_page = res.json()
    article = open_api_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):

        await event.respond(f"{i + 1, results[i]}")

    raise events.StopPropagation


# Event == Editing a Message


@bot.on(events.MessageEdited)
async def handler(event):
    # Log the date of new edits
    print('Message', event.id, 'changed at', event.date)
    await event.reply(f"You edited a message :)")
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern="/weather"))
async def weather(event):
    city = event.text
    temp = wtr(city)
    print(temp)
    await event.reply(f"{temp}°C")
    raise events.StopPropagation
# @bot.on(events.MessageRead)
# async def handler(event):
#     # Log when someone reads your messages
#     print('Someone has read all your messages until', event.max_id)

# CHAT ACTIONS


@bot.on(events.ChatAction)
async def handler(event):
    # Welcome every new user
    if event.user_joined:
        await event.reply('Welcome, to the Group!!')


@bot.on(events.ChatAction)
async def handler(event):
    # Welcome every new user
    if event.user_added:
        await event.reply('New Member added in the Group!!')


@bot.on(events.ChatAction)
async def handler(event):
    # Welcome every new user
    if event.user_kicked:
        await event.reply('User Kicked from the Group!!')


@bot.on(events.ChatAction)
async def handler(event):
    # Welcome every new user
    if event.created:
        await event.reply('Thanks For Inviting me to this Group :)')
        groupID = event.user_ids
        print(groupID)
        groupUserData = f'''Bot was added in a Group. Group IDs = {groupID}\n'''
        f = open("Textfiles/groupUserData.txt", "a")
        f.write(groupUserData)
        f.close()


@bot.on(events.ChatAction)
async def handler(event):
    # Welcome every new user
    if event.new_title:
        await event.reply('Group Title Was Changed :)')


@bot.on(events.UserUpdate)
async def handler(event):
    # If someone is uploading, say something
    if event.uploading:
        await bot.send_message(event.user_id, 'What are you sending?')


@bot.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply('Bye Bye!!')


@bot.on(events.NewMessage(pattern='/website'))
async def SendWebsiteLink(event):
    await event.reply('https://quantumbyte.studio/')
    raise events.StopPropagation

Truth = [
    "What's the last lie you told?",
    "What was the most embarrassing thing you've ever done on a date?",
    "Have you ever accidentally hit something (or someone!) with your car?",
    "Name someone you've pretended to like but actually couldn't stand.",
    "What's your most bizarre nickname?",
    "What's been your most physically painful experience?",
    "What bridges are you glad that you burned?",
    "What's the craziest thing you've done on public transportation?",
    "If you met a genie, what would your three wishes be?",
    "If you could write anyone on Earth in for President of the United States, who would it be and why?",
    "What's the meanest thing you've ever said to someone else?",
    "Who was your worst kiss ever?",
    "What's one thing you'd do if you knew there no consequences?",
    "What's the craziest thing you've done in front of a mirror?",
    "What's the meanest thing you've ever said about someone else?",
    "What's something you love to do with your friends that you'd never do in front of your partner?",
    "Who are you most jealous of?",
    "What do your favorite pajamas look like?",
    "Have you ever faked sick to get out of a party?",
    "Who's the oldest person you've dated?",
    "How many selfies do you take a day?",
    "Meatloaf says he'd do anything for love, but he won't do “that.” What's your “that?”",
    "How many times a week do you wear the same pants?",
    "Would you date your high school crush today?",
    "Where are you ticklish?",
    "Do you believe in any superstitions? If so, which ones?",
    "What's one movie you're embarrassed to admit you enjoy?",
    "What's your most embarrassing grooming habit?",
    "When's the last time you apologized? What for?",
    "How do you really feel about the Twilight saga?",
    "Where do most of your embarrassing odors come from?",
    "Have you ever considered cheating on a partner?",
    "Have you ever cheated on a partner?",
    "Boxers or briefs?",
    "Have you ever peed in a pool?",
    "What's the weirdest place you've ever grown hair?",
    "If you were guaranteed to never get caught, who on Earth would you murder?",
    "What's the cheapest gift you've ever gotten for someone else?",
    "What app do you waste the most time on?",
    "What's the weirdest thing you've done on a plane?",
    "Have you ever been nude in public?",
    "How many gossip blogs do you read a day?",
    "What is the youngest age partner you'd date?",
    "Have you ever picked your nose in public?",
    "Have you ever lied about your age?",
    "If you had to delete one app from your phone, which one would it be?",
    "What's your most embarrassing late night purchase?",
    "What's the longest you've gone without showering?",
    "Have you ever used a fake ID?", "Who's your hall pass?",
    "When was the last time you peed in bed?",
    "What is the biggest lie you have ever told?",
    "Tell us your most embarrassing vomit story.",
    "Have you ever made out with someone here?",
    "Have you ever cheated or been cheated on?",
    "What are your top three turn-ons?",
    "What is your deepest darkest fear?",
    "What is the most childish thing you still do?",
    "What is something your friends would never expect that you do?",
    "Who is the person you most regret kissing?",
    "When was the last time you lied?",
    "Who was the last person you licked?",
    "What is the most embarrassing picture of you?",
    "What's the most embarrassing thing you've ever done?",
    "Have you ever broken the law?",
    "Do you have any fetishes?",
    "What's the worst thing you've ever done?",
    "What's the worst thing you've ever said to anyone?",
    "What's the biggest misconception about you?",
    "What's a secret you've never told anyone?",
    "What would you do if you were the opposite sex for a week?",
    "What's the worst time you let someone take the blame for something you did?",
    "What do most people think is true about you, but isn't?",
    "What's your biggest regret?",
    "What are your thoughts on polyamory?",
    "What is the biggest thing you've gotten away with?",
    "Why did you break up with your last boyfriend or girlfriend?",
    "What is the most embarrassing series of texts you have on your phone?",
    "When was the last time you cried?",
    "What's your biggest fantasy?",
    "Tell me about your first kiss",
    "What is the most embarrassing thing in your room?",
    "What was the most awkward romantic encounter you have had?",
    "Do you have a hidden talent?",
    "What is the stupidest thing you have ever done?",
    "What pictures or videos of you do you wish didn't exist?",
    "What is your biggest regret?",
    "Who is your crush?",
    "Tell me about your most awkward date.",
    "What is the naughtiest thing you've done in public?",
    "What is the most expensive thing you have stolen?",
    "What's something you're glad your mum doesn't know about you?",
    "What is something that people think you would never be into, but you are?",
    "Who was your first celebrity crush?",
    "What's the worst intimate experience you've ever had?",
    "Have you ever cheated in an exam?",
    "What's the drunkest you've ever been?",
    "What is the silliest thing you have an emotional attachment to?",
    "What's the biggest mistake you've ever made?",
    "What's the most disgusting thing you've ever done?",
    "Who would you like to kiss in this room?",
    "Where's the weirdest place you've had sex?",
    "What is your Worst Habit?",
    "What's the worst thing anyone's ever done to you?",
    "What's the strangest dream you've had?",
    "Have you ever been caught doing something you shouldn't have?",
    "What's the worst date you've been on?",
    "Have you ever lied to get out of a bad date?",
    "Have you ever peed in the shower?",
    "Have you ever shit yourself since you were a child?",
    "What is the most embarrassing thing your parents have caught you doing?",
    "What's the most trouble you've been in?",
    "Who is the sexiest person here?",
    "What secret about yourself did you tell someone in confidence and then they told a lot of other people?",
    "When was the most inappropriate time you farted?",
    "What is the scariest dream you have ever had?",
    "What is the grossest thing that has come out of your body?",
    "What is your favourite thing that your boyfriend or girlfriend does?",
    "Who have you loved but they didn't love you back?",
    "If you starred in a romance, what would it be like?",
    "What was the cruellest joke you played on someone?",
    "What is the most embarrassing thing you have put up on social media?",
    "What is the grossest thing you have had in your mouth?",
    "Tell me about the last time someone unexpectedly walked in on you while you were naked.",
    "What is the most embarrassing nickname you have ever had?",
    "Describe your most recent romantic encounter in detail.",
    "What is the weirdest thing you have done for a boyfriend or girlfriend?",
    "Is it true that you (whatever you or the group suspects they do/did)?",
    "When was the last time you wiped a booger off on something that shouldn't have boogers on it?",
    "What do you really hope your parents never find out about?",
    "Tell me something you don't want me to know.",
    "What have you done that people here would judge you most for doing?",
    "What is something that you have never told anyone?",
    "What is the most disgusting habit you have?"
]

Dare = [
    "Do freestyle rap for 1 minute about the other participants and send video.",
    "Kiss the person to your left and send video.",
    "Do an impression of another player until someone can figure out who it is and send video.",
    "Call your crush.",
    "Dance with no music for 1 minute and send video.",
    "Do a cartwheel and send video.",
    "Let the person on your right draw on your face.",
    "Give your phone to another player who can send one text saying anything they want to one of your contacts.",
    "Drink lemon juice.",
    "Crack an egg on our head and send video.",
    "Swap clothes with someone of the opposite gender for 2 rounds and send video.",
    "Act like a chicken until your next turn.",
    "Burp the alphabet.",
    "Talk in a Jamaican accent until your next turn.",
    "Call a friend, pretend it's their birthday, and sing “Happy Birthday” to them.",
    "Perform ballet for 1 minute.",
    "Shower with your clothes on.",
    "Take a selfie on the toilet and post it.",
    "End each sentence with the word “not” until your next turn.",
    "Name a famous person that looks like each player.",
    "Dance like your life depends on it.",
    "Eat a packet of hot sauce or ketchup straight.",
    "Pour ice down your pants and send video.",
    "Spin around 12 times and try to walk straight.",
    "Put on a blindfold and touch the other players' faces until you can figure out who it is.",
    "Let the other players redo your hairstyle.",
    "Eat a raw egg and send video.",
    "Let the player to your right redo your makeup.",
    "Pretend to be a squirrel until your next turn.",
    "Dump a bucket of cold water on your head and send video.",
    "Lick a bar of soap and send video.",
    "Eat a teaspoon of mustard.",
    "Talk without closing your mouth and send video.",
    "You have 5 minutes to write a country song and perform it.",
    "Let someone paint your nails any way they want.",
    "Do 5 minutes of stand-up comedy and send video.",
    "Quack like a duck until your next turn.",
    "Sing the national anthem in a British accent and send video."
]

Insults = [
    "If I throw a stick, will you leave?",
    "You're a gray sprinkle on a rainbow cupcake.",
    "If your brain was dynamite, there wouldn't be enough to blow your hat off.",
    "You are more disappointing than an unsalted pretzel.",
    "Light travels faster than sound, which is why you seemed bright until you spoke.",
    "We were happily married for one month, but unfortunately, we've been married for 10 years.",
    "Your kid is so annoying he makes his Happy Meal cry.",
    "You have so many gaps in your teeth it looks like your tongue is in jail.",
    "Your secrets are always safe with me. I never even listen when you tell me them.",
    "I'll never forget the first time we met. But I'll keep trying.",
    "I forgot the world revolves around you. My apologies! How silly of me.",
    "I only take you everywhere I go just so I don't have to kiss you goodbye.",
    "Hold still. I'm trying to imagine you with a personality.",
    "Our kid must have gotten his brain from you! I still have mine.",
    "Your face makes onions cry.",
    "The only way my husband would ever get hurt during an activity is if the TV exploded.",
    "You look so pretty. Not at all gross today.",
    "It's impossible to underestimate you.",
    "Her teeth were so bad she could eat an apple through a fence.",
    "I'm not insulting you; I'm describing you.",
    "I'm not a nerd; I'm just smarter than you.",
    "Don't be ashamed of who you are. That's your parents' job.",
    "Your face is just fine, but we'll have to put a bag over that personality.",
    "You bring everyone so much joy… when you leave the room.",
    "I thought of you today. It reminded me to take out the trash.",
    "Don't worry about me. Worry about your eyebrows.",
    "You are the human version of period cramps.",
    "If you're going to be two-faced, at least make one of them pretty.",
    "You are like a cloud. When you disappear, it's a beautiful day.",
    "I'd rather treat my baby's diaper rash than have lunch with you.",
    "Child, I've forgotten more than you ever knew.",
    "You just might be why the middle finger was invented in the first place.",
    "I know you are, but what am I?",
    "I see no evil, and I definitely don't hear your evil.",
    "You have miles to go before you reach mediocre.",
    "When you look in the mirror, say hi to the clown you see in there for me, would ya?",
    "Bye, hope to see you never.",
    "Complete this sentence for me: “I never want to see you ____!”",
    "Remember that time you were saying that thing I didn't care about? Yeah… that is now.",
    "I was today years old when I realized I didn't like you.",
    "N'Sync said it best: “BYE, BYE, BYE.”",
    "Wish I had a flip phone so I could slam it shut on this conversation.",
    "How many licks till I get to the interesting part of this conversation?",
    "Wow, your maker really didn't waste time giving you a personality, huh?",
    "You're cute. Like my dog. He also always chases his tail for entertainment.",
    "Someday you'll go far… and I really hope you stay there.",
    "Oh, I'm sorry. Did the middle of my sentence interrupt the beginning of yours?",
    "You bring everyone so much joy! You know, when you leave the room. But, still.",
    "Oops, my bad. I could've sworn I was dealing with an adult.",
    "Did I invite you to the barbecue? Then why are you all up in my grill?"
]


@bot.on(events.NewMessage(pattern='/truthNdare'))
async def tnd(event):
    message = "Inorder to play Truth and Dare add this bot in your friends group, then type \"/truth\" for a truth question and \"/dare\" for a dare."
    await event.reply(f"{message}")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/truth'))
async def truthQuestion(event):
    number = int(random.uniform(0, len(Truth)))
    sawal = Truth[number]
    await event.reply(f"{sawal}")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/dare'))
async def dareQuestion(event):
    number = int(random.uniform(0, len(Dare)))
    sawal = Dare[number]
    await event.reply(f"{sawal}")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/insult'))
async def insultLines(event):
    number = int(random.uniform(0, len(Insults)))
    insult = Insults[number]
    await event.reply(f"{insult}")
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/today'))
async def today(event):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    await event.reply(f"Today : {dt_string}")
    raise events.StopPropagation

