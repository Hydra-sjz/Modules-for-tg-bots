from pyrogram import Client, filters


def aesthetify(string):
    PRINTABLE_ASCII = range(0x21, 0x7f)
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@Client.on_message(
    filters.command(["ae"]))
async def aesthetic(client, message):
    status_message = await message.reply_text("...")
    text = "".join(str(e) for e in message.command[1:])
    text = "".join(aesthetify(text))
    await status_message.edit(text)

# DART------------

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS


@Client.on_message(
    filters.command(["throw", "dart"])
)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# LUCK------------

# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["luck", "cownd"])
)
async def luck_cownd(client, message):
    """ /luck an @animatedluck """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# GOAL------------ 

# EMOJI CONSTANTS
GOAL_E_MOJI = "⚽"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["goal", "shoot"])
)
async def roll_shoot(client, message):
    """ @Goal """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# PONG------------ 

# EMOJI CONSTANTS
PONG_E_MOJI = "🎳"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["pog", "piong"])
)
async def pog_ping(client, message):
    """ @pog """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=PONG_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# BASKETBALL------------ 

# EMOJI CONSTANTS
BALL_E_MOJI = "🏀"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["ball", "shoot"])
)
async def ball_shoot(client, message):
    """ @ball """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=BALL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# DICE------------ 

# EMOJI CONSTANTS
ROLL_E_MOJI = "🎲"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["roll", "dice"])
)
async def roll_dice(client, message):
    """ @roll """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=ROLL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


# RUN-----------------

import random

RUN_STRINGS = (
    "A broken of a demeanly filled with darkness \
    Why have you come to remind it ",
    "We have become the lives to be the underwater to the underwater that we do not know.",
    "You want the bad call ... but you need good thunder ....",
    "Oh Bloody Grama Virtues!",
    "Sea MUGGie I Am Going to Pay The Bill.",
    "Want with me!",
    "You are not a male chaff !!",
    "I locked it, and the good beach is done by the good beach.",
    "Kindi ... Kindi ...!",
    "Giving the stems and then showing one and show the ISI Mark",
    "Dayveyeese, Kingfisher ... Childe ...!.",
    "You have made your father for half of the midnight?",
    "This is the King of our work.",
    "I'm fetts to feed ...."
    "Mumak is every Bearby Kachyo ...",
    "Oh it moves it .... When we moves it ...",
    "The self of carpenter is the virtue of a carpenter.",
    "Why not to feel this intelligence in Da Vijaya ...!",
    "Where was this time ...."
    "Save me only ...."
    "I know his father's name is Bhavaniami ....",
    "Da Dasa ...",
    "Uppukam's English Salt Mongo Tree .....",
    "Children ..",
    "Your father to Paul ....",
    "Car Engine Out Completely .....",
    "This is the eye or magnety ...",
    "Before falling in the 4th pegging, I will arrive there.",
    "The drunk rains and wast ...."
    "To tell me I love Yo ...."
    "No, the Meenaka of Verbapur is not ....",
    "Look out for the wall!",
    "Get back here!",
    "Don't leave me alone with them!!",
    "Naruto run activated",
    "Hey take responsibilty for what you just did!",
    "Run everyone, they just dropped a bomb 💣😱",
    "Legend has it, they're still running.",
    "Ah, what a waste. I liked that one.",
    "As The Doctor would say... RUN!",
    "Hasta la vista, baby.",
    "And they disappeared forever, never to be seen again.",
)


@Client.on_message(
    filters.command("run")
)
async def run(_, message):
    """ /run strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# lucky number------------

import random

LNM_STRINGS = (
    "1",
    "8",
    "4",
    "7",
    "3",
    "9",
    "5",
    "2",
    "6",
    "10",
)


@Client.on_message(
    filters.command("lnm")
)
async def lnm(_, message):
    """ /lnm strings """
    effective_string = random.choice(LNM_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

#INSULT

import random

NINSUL_STRINGS = (
    "`Owww ... Such a stupid idiot.`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 544 section 9 prevents me from replying to stupid humans like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",
)


@Client.on_message(
    filters.command("insultt")
)
async def insultt(_, message):
    """ /insultt strings """
    effective_string = random.choice(NINSUL_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# MEETOO

import random

MEETO_STRINGS = (
    "`Me too thanks`",
    "`Haha yes, me too`",
    "`Same lol`",
    "`Me irl`",
    "`Same here`",
    "`Haha yes`",
    "`Same pinch bsdk`",
)


@Client.on_message(
    filters.command("metoo")
)
async def metoo(_, message):
    """ /metoo strings """
    effective_string = random.choice(MEETO_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)


# ENGMUSIC

import random

ENGSO_STRINGS = (
    "🎶 I'm in love with the shape of you\nWe push and pull like a magnet do\nAlthough my heart is falling too\nI'm in love with your body\nAnd last night you were in my room\nAnd now my bedsheets smell like you\nEvery day discovering something brand new 🎶\n🎶I'm in love with your body\nOh—I—oh—I—oh—I—oh—I\nI'm in love with your body\nOh—I—oh—I—oh—I—oh—I\nI'm in love with your body\nOh—I—oh—I—oh—I—oh—I\nI'm in love with your body 🎶\n**-Shape of You**",
    "🎶 I've been reading books of old\nThe legends and the myths\nAchilles and his gold\nHercules and his gifts\nSpiderman's control\nAnd Batman with his fists\nAnd clearly I don't see myself upon that list 🎶\n-**Something Just Like This**",
    "🎶 I don't wanna live forever\n'Cause I know I'll be livin' in vain\nAnd I don't wanna fit wherever\nI just wanna keep callin' your name\nUntil you come back home\nI just wanna keep callin' your name\nUntil you come back home\nI just wanna keep callin' your name\nUntil you come back home 🎶\n-**I don't Wanna Live Forever**",
    "🎶 Oh, hush, my dear, it's been a difficult year\nAnd terrors don't prey on\nInnocent victims\nTrust me, darling, trust me darling\nIt's been a loveless year\n I'm a man of three fears\nIntegrity, faith and\nCrocodile tears\nTrust me, darling, trust me, darling 🎶\n**-Bad Lier**",
    "🎶 Walking down 29th and Park\nI saw you in another's arms\nOnly a month we've been apart\nYou look happier\n\n Saw you walk inside a bar\nHe said something to make you laugh\nI saw that both your smiles were twice as wide as ourn\nYeah, you look happier, you do 🎶\n**-Happier**",
    "🎶 I took the supermarket flowers from the windowsill\nI threw the day old tea from the cup\nPacked up the photo album Matthew had made\nMemories of a life that's been loved\nTook the get well soon cards and stuffed animals\nPoured the old ginger beer down the sink\nDad always told me, 'don't you cry when you're down'\nBut mum, there's a tear every time that I blink 🎶\n**-Supermarket Flowers**",
    "🎶 And you and I we're flying on an aeroplane tonight\nWe're going somewhere where the sun is shining bright\nJust close your eyes\nAnd let's pretend we're dancing in the street\nIn Barcelona\nBarcelona\nBarcelona\nBarcelona🎶\n**-Barcelona**",
    "🎶 Maybe I came on too strong\nMaybe I waited too long\nMaybe I played my cards wrong\nOh, just a little bit wrong\nBaby I apologize for it\n\nI could fall, or I could fly\nHere in your aeroplane\nAnd I could live, I could die\nHanging on the words you say\nAnd I've been known to give my all\nAnd jumping in harder than\nTen thousand rocks on the lake 🎶\n**-Dive**",
    "🎶 I found a love for me\nDarling just dive right in\nAnd follow my lead\nWell I found a girl beautiful and sweet\nI never knew you were the someone waiting for me\n'Cause we were just kids when we fell in love\nNot knowing what it was\n\nI will not give you up this time\nBut darling, just kiss me slow, your heart is all I own\nAnd in your eyes you're holding mine🎶\n**-Perfect**",
    "🎶 I was born inside a small town, I lost that state of mind\nLearned to sing inside the Lord's house, but stopped at the age of nine\nI forget when I get awards now the wave I had to ride\nThe paving stones I played upon, they kept me on the grind\nSo blame it on the pain that blessed me with the life 🎶\n **-Eraser**",
    "🎶 Say, go through the darkest of days\nHeaven's a heartbreak away\nNever let you go, never let me down\nOh, it's been a hell of a ride\nDriving the edge of a knife.\nNever let you go, never let me down\n\nDon't you give up, nah-nah-nah\nI won't give up, nah-nah-nah\nLet me love you \n Let me love you 🎶\n**-Let me Love You**",
    "🎶 I'll stop time for you\nThe second you say you'd like me to\nI just wanna give you the loving that you're missing\nBaby, just to wake up with you\nWould be everything I need and this could be so different\nTell me what you want to do\n\n'Cause I know I can treat you better\nThan he can\nAnd any girl like you deserves a gentleman 🎶\n**-Treat You Better**",
    "🎶 You're the light, you're the night\nYou're the color of my blood\nYou're the cure, you're the pain\nYou're the only thing I wanna touch\nNever knew that it could mean so much, so much\nYou're the fear, I don't care\n'Cause I've never been so high\nFollow me through the dark\nLet me take you past our satellites\nYou can see the world you brought to life, to life\n\nSo love me like you do, lo-lo-love me like you do\nLove me like you do, lo-lo-love me like you do 🎶\n**-Love me Like you Do**",
    "🎶 Spent 24 hours\nI need more hours with you\nYou spent the weekend\nGetting even, ooh ooh\nWe spent the late nights\nMaking things right, between us\nBut now it's all good baby\nRoll that Backwood baby\nAnd play me close\n\n'Cause girls like you\nRun around with guys like me\n'Til sundown, when I come through\nI need a girl like you, yeah yeah 🎶\n**-Girls Like You**",
    "🎶 Oh, angel sent from up above\nYou know you make my world light up\nWhen I was down, when I was hurt\nYou came to lift me up\nLife is a drink and love's a drug\nOh, now I think I must be miles up\nWhen I was a river dried up\nYou came to rain a flood 🎶\n**-Hymn for the Weekend**",
    "🎶 I've known it for a long time\nDaddy wakes up to a drink at nine\nDisappearing all night\nI don’t wanna know where he's been lying\nI know what I wanna do\nWanna run away, run away with you\nGonna grab clothes, six in the morning, go 🎶\n**-Runaway**",
    "🎶 You were the shadow to my light\nDid you feel us\nAnother start\nYou fade away\nAfraid our aim is out of sight\nWanna see us\nAlive 🎶\n**-Faded**",
    "🎶 It's been a long day without you, my friend\nAnd I'll tell you all about it when I see you again\nWe've come a long way from where we began\nOh I'll tell you all about it when I see you again\nWhen I see you again 🎶\n**-See you Again**",
    "🎶 I can swallow a bottle of alcohol and I'll feel like Godzilla\nBetter hit the deck like the card dealer\nMy whole squad's in here, walking around the party\nA cross between a zombie apocalypse and big Bobby 'The\nBrain' Heenan which is probably the\nSame reason I wrestle with mania 🎶\n**-Godzilla**",
    "🎶 Yeah, I'm gonna take my horse to the old town road\nI'm gonna ride 'til I can't no more\nI'm gonna take my horse to the old town road\nI'm gonna ride 'til I can't no more (Kio, Kio) 🎶\n**-Old Town Road**",
    "🎶 Oh-oh, ooh\nYou've been runnin' round, runnin' round, runnin' round throwin' that dirt all on my name\n'Cause you knew that I, knew that I, knew that I'd call you up\nYou've been going round, going round, going round every party in L.A.\n'Cause you knew that I, knew that I, knew that I'd be at one, oh 🎶\n**-Attention**",
    "🎶 This hit, that ice cold\nMichelle Pfeiffer, that white gold\nThis one for them hood girls\nThem good girls straight masterpieces\nStylin', wilin', livin' it up in the city\nGot Chucks on with Saint Laurent\nGotta kiss myself, I'm so pretty\n\nI'm too hot (hot damn)\nCalled a police and a fireman\nI'm too hot (hot damn)\nMake a dragon wanna retire man\nI'm too hot (hot damn)\nSay my name you know who I am\nI'm too hot (hot damn)\nAnd my band 'bout that money, break it down 🎶\n**-Uptown Funk**",
    "🎶 Just a young gun with the quick fuse\nI was uptight, wanna let loose\nI was dreaming of bigger things\nAnd wanna leave my own life behind\nNot a yes sir, not a follower\nFit the box, fit the mold\nHave a seat in the foyer, take a number\nI was lightning before the thunder\n\nThunder, feel the thunder\nLightning then the thunder\nThunder, feel the thunder\nLightning then the thunder\nThunder, thunder 🎶\n**-Thunder**",
    "🎶 Oh, love\nHow I miss you every single day\nWhen I see you on those streets \nOh, love\nTell me there's a river I can swim that will bring you back to me\n'Cause I don't know how to love someone else\nI don't know how to forget your face\nNo, love\nGod, I miss you every single day and now you're so far away\nSo far away 🎶\n**-So Far Away**",
    "🎶 And if you feel you're sinking, I will jump right over\nInto cold, cold water for you\nAnd although time may take us into different places\nI will still be patient with you\nAnd I hope you know 🎶\n**-Cold Water**",
    "🎶 When you feel my heat\nLook into my eyes\nIt's where my demons hide\nIt's where my demons hide\nDon't get too close\nIt's dark inside\nIt's where my demons hide\nIt's where my demons hide 🎶\n**-Demons**",
    "🎶 Who do you love, do you love now?\nI wanna know the truth (whoa)\nWho do you love, do you love now?\nI know it's someone new\nYou ain't gotta make it easy, where you been sleepin'? 🎶\n**-Who do  Love ?**",
    "🎶 Your touch is magnetic\n'Cause I can't forget it\n(There's a power pulling me back to you)\nAnd baby I'll let it\n'Cause you're so magnetic I get it\n(When I'm waking up with you, oh) 🎶\n**-Magnetic**",
    "🎶 Girl my body don't lie, I'm outta my mind\nLet it rain over me, I'm rising so high\nOut of my mind, so let it rain over me\n\nAy ay ay, ay ay ay let it rain over me\nAy ay ay, ay ay ay let it rain over me 🎶\n**-Rain over Me**",
    "🎶 I miss the taste of a sweeter life\nI miss the conversation\nI'm searching for a song tonight\nI'm changing all of the stations\nI like to think that we had it all\nWe drew a map to a better place\nBut on that road I took a fall\nOh baby why did you run away?\n\nI was there for you\nIn your darkest times\nI was there for you\nIn your darkest night 🎶\n**-Maps**",
    "🎶 I wish—I wish that I was bulletproof, bulletproof\nI wish—I wish that I was bulletproof, bulletproof\n(Bullet-bulletproof, bullet-bullet-bulletproof)\nI'm trippin' on my words and my patience\nWriting every verse in a cadence\nTo tell you how I feel, how I feel, how I feel (Yeah)\nThis is how I deal, how I deal, how I deal (Yeah)\nWith who I once was, now an acquaintance\nThink my confidence (My confidence) is in the basement\nTryin' to keep it real, keep it real, keep it real (Yeah)\n'Cause I'm not made of steel, made of steel 🎶\n**-Bulletproof**",
    "🎶 You won't find him down on Sunset\nOr at a party in the hills\nAt the bottom of the bottle\nOr when you're tripping on some pills\nWhen they sold you the dream you were just 16\nPacked a bag and ran away\nAnd it's a crying shame you came all this way\n'Cause you won't find Jesus in LA\nAnd it's a crying shame you came all this way\n'Cause you won't find Jesus in LA 🎶\n-**Jesus in La**",
)


@Client.on_message(
    filters.command("engsongs")
)
async def engsongs(_, message):
    """ /engsongs strings """
    effective_string = random.choice(ENGSO_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)


# LOVE-------

import random

LOV_STRINGS = (
    "(๑♡⌓♡๑)",
    "꒰⑅ᵕ༚ᵕ꒱˖♡",
    "♡˖꒰ᵕ༚ᵕ⑅꒱",
    "(◍•ᴗ•◍)❤",
    "(✿ ♡‿♡)",
    "♡(ӦｖӦ｡)",
    "(灬º‿º灬)♡",
    "( ˘ ³˘)♥",
    "(っ˘з(˘⌣˘ )",
    "(๑˙❥˙๑)",
    "(●’3)♡(ε`●)",
    "(๑♡⌓♡๑)",
    "(｡♡‿♡｡)",
    "(●♡∀♡)",
    "( ◜‿◝ )♡",
    "♡(> ਊ <)♡",
)


@Client.on_message(
    filters.command("love")
)
async def love(_, message):
    """ /love strings """
    effective_string = random.choice(LOV_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# SHRUGLE-------

import random

SRG_STRINGS = (
    "¯\_(ツ)_/¯",
    "¯\_༼ •́ ͜ʖ •̀ ༽_/¯",
    "¯\_( ͡° ͜ʖ ͡°)_/¯",
    "乁༼☯‿☯✿༽ㄏ",
    "¯\_༼ᴼل͜ᴼ༽_/¯",
    "乁[ᓀ˵▾˵ᓂ]ㄏ",
    "¯\_(☯෴☯)_/¯",
    "乁ʕ •̀ ۝ •́ ʔㄏ",
    "乁║ ˙ 益 ˙ ║ㄏ",
    "乁( ⁰͡ Ĺ̯ ⁰͡ ) ㄏ",
    "¯\_〳 •̀ o •́ 〵_/¯",
    "乁( •_• )ㄏ",
    "乁[ ◕ ᴥ ◕ ]ㄏ",
    "¯\_ʘ‿ʘ_/¯",
    "¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "¯\(◉‿◉)/¯",
)


@Client.on_message(
    filters.command("shrug")
)
async def shrug(_, message):
    """ /shrug strings """
    effective_string = random.choice(SRG_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# TOSS TAIL-------

import random

THT_STRINGS = (
    "Heads",
    "Tails",
    "Tails",
    "Heads",
    "Tails",
    "Heads",
    "Heads",
    "Heads",
    "Tails",
    "Tails",
)


@Client.on_message(
    filters.command("toss")
)
async def toss(_, message):
    """ /toss strings """
    effective_string = random.choice(THT_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)


#  TABLE--------

import random

TBL_STRINGS = (
    "(ノಠ益ಠ)ノ彡┻━┻",
    "(╯°□°）╯︵ ┻━┻",
    "(┛◉Д◉)┛彡┻━┻",
    "(ﾉ≧∇≦)ﾉ ﾐ ┻━┻",
    "(ﾉ´･ω･)ﾉ ﾐ ┻━┻",
    "(┛ಸ_ಸ)┛彡┻━┻",
    "(╯ರ ~ ರ)╯︵ ┻━┻",
    "(ノಥ,_｣ಥ)ノ彡┻━┻",
    "(┛✧Д✧))┛彡┻━┻",
    "┻┻︵¯\(ツ)/¯︵┻┻",
    "┻┻︵ヽ(`Д´)ﾉ︵┻┻",
    "(/¯◡ ‿ ◡)/¯ ~ ┻━┻",
    "┻━┻ミ＼(≧ﾛ≦＼)",
    "(ノ￣皿￣)ノ ⌒== ┫",
    "(┛❍ᴥ❍)┛彡┻━┻",
    "─=≡Σ(╯°□°)╯︵┻┻",
    "┻━┻ ヘ╰( •̀ε•́ ╰)",
    "ʕノ•ᴥ•ʔノ ︵ ┻━┻",
    "(ヘ･_･)ヘ┳━┳",
    "I ran out of tables, will order more.",
    "Go do some work instead of flippin tables.",
)


@Client.on_message(
    filters.command("table")
)
async def table(_, message):
    """ /table strings """
    effective_string = random.choice(TBL_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

#  YES OR NO--------

import random

DCD_STRINGS = (
    "Yes",
    "No",
    "maybe",
)


@Client.on_message(
    filters.command("decide")
)
async def decide(_, message):
    """ /decide strings """
    effective_string = random.choice(DCD_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Truth-------

TRUTH_STRINGS = (
    " What’s the last lie you told?",
    "What was the most embarrassing thing you’ve ever done on a date?",
    "Have you ever accidentally hit something (or someone!) with your car?",
    "Name someone you’ve pretended to like but actually couldn’t stand.",
    "What’s your most bizarre nickname?",
    "What’s been your most physically painful experience?",
    "What bridges are you glad that you burned?",
    "What’s the craziest thing you’ve done on public transportation?",
    "If you met a genie, what would your three wishes be?",
    "If you could write anyone on Earth in for President of the United States, who would it be and why?",
    "What’s the meanest thing you’ve ever said to someone else?",
    "Who was your worst kiss ever?",
    "What’s one thing you’d do if you knew there no consequences?",
    "What’s the craziest thing you’ve done in front of a mirror?",
    "What’s the meanest thing you’ve ever said about someone else?",
    "What’s something you love to do with your friends that you’d never do in front of your partner?",
    "Who are you most jealous of?",
    "What do your favorite pajamas look like?",
    "Have you ever faked sick to get out of a party?",
    "Who’s the oldest person you’ve dated?",
    "How many selfies do you take a day?",
    "Meatloaf says he’d do anything for love, but he won’t do “that.” What’s your “that?”",
    "How many times a week do you wear the same pants?",
    "Would you date your high school crush today?",
    "Where are you ticklish?",
    "Do you believe in any superstitions? If so, which ones?",
    "What’s one movie you’re embarrassed to admit you enjoy?",
    "What’s your most embarrassing grooming habit?",
    "When’s the last time you apologized? What for?",
    "How do you really feel about the Twilight saga?",
    "Where do most of your embarrassing odors come from?",
    "Have you ever considered cheating on a partner?",
    "Have you ever cheated on a partner?",
    "Boxers or briefs?",
    "Have you ever peed in a pool?",
    "What’s the weirdest place you’ve ever grown hair?",
    "If you were guaranteed to never get caught, who on Earth would you murder?",
    "What’s the cheapest gift you’ve ever gotten for someone else?",
    "What app do you waste the most time on?",
    "What’s the weirdest thing you’ve done on a plane?",
    "Have you ever been nude in public?",
    "How many gossip blogs do you read a day?",
    "What is the youngest age partner you’d date?",
    "Have you ever picked your nose in public?",
    "Have you ever lied about your age?",
    "If you had to delete one app from your phone, which one would it be?",
    "What’s your most embarrassing late night purchase?",
    "What’s the longest you’ve gone without showering?",
    "Have you ever used a fake ID?",
    "Who’s your hall pass?",
    "Be honest: Do you have a favorite child?",
    "Which of your family members annoys you the most and why?",
    "What is your greatest fear in a relationship?",
    "What’s your biggest pet peeve about the person to your left?",
    "What’s the most embarrassing text in your phone right now?",
    "Have you ever seen a dead body?",
    "What celebrity do you think is overrated?",
    "Have you ever lied to your boss?",
    "Have you ever stolen something from work?",
    "What’s the longest you’ve gone without brushing your teeth?",
    "What’s your biggest regret in life?",
    "Who would you hate to see naked?",
    "Describe the weirdest thing you’ve ever done while inebriated.",
    "Have you ever regifted a present?",
    "Would you break up with your partner for $1 million?",
    "Have you ever had a crush on a coworker?",
    "Do you still have feelings for any of your exes?",
    "What’s the smallest tip you’ve ever left at a restaurant?",
    "Have you ever regretted something you did to get a crush or partner’s attention?",
    "What’s one job you could never do?",
    "Have you ever ghosted a friend?",
    "Have you ever ghosted a partner?",
    "What’s the most scandalous photo in your cloud?",
    "If you switched genders for a day, what would you do?",
    "How many photo editing apps do you have on your phone?",
    "How many pairs of granny panties do you own?",
    "What are your favorite and least favorite of your body parts?",
    "When’s the last time you got dumped?",
    "What’s the most childish thing you still do?",
    "When’s the last time you dumped someone?",
    "If you had to pick someone in this room to be your partner on a game show, who would it be and why?",
    "Would you date someone shorter than you?",
    "Have you ever lied for a friend?",
    "Name one thing you’d change about every person in this room.",
    "When’s the last time you made someone else cry?",
    "What’s the most embarrassing thing you’ve done in front of a crowd?",
    "If you could become invisible, what’s the worst thing you’d do?",
    "After you’ve dropped a piece of food, what’s the longest time you’ve left it on the floor before eating it?",
    "What’s one thing in your life you wish you could change?",
    "If you could date two people at once, would you do it? If so, who?",
    "What’s something that overwhelms you?",
    "What was the greatest day of your life?",
    "What’s one useless skill you’d love to learn anyway?",
    "If I went through your cabinets, what’s the weirdest thing I’d find?",
    "Have you ever farted and blamed it on someone else?",
    "What’s the worst thing you’ve ever done at work?",
    "How many people have you kissed?",
    "What’s your number?",
    "Have you ever gotten mad at a friend for posting an unflattering picture of you?",
    "What’s your most absurd dealbreaker?",
    "Who in this room would you list as your emergency contact?",
    "What’s something you would die if your mom found out about?",
    "What’s the scariest thing that’s ever happened to you?",
    "If you could set anyone here up with your best friend, who would it be and why?",
    "How often do you wash your sheets?",
    "Have you ever farted in an elevator?",
    "Who was your first love?",
    "What’s the last purchase you regretted?",
    "Have you ever sent a sext?",
    "Have you ever sent a sext to the wrong person? Who?",
    "What’s the weirdest dream you’ve ever had?",
    "Have you ever had a one-night stand?",
    "Are you scared of getting old?",
    "What do you want on your tombstone?",
    "If you had one week to live and you had to marry someone in this room, who would it be?",
    "What’s the last movie that made you cry?",
    "List one positive and one negative thing about everyone in the room.",
    "When was your first time?",
    "Who was your first?",
    "What’s the most sinful thing you’ve done in a house of worship?",
    "Who would you call to help bury a body?",
    "Who would call you to help bury a body? Would you do it?",
    "When’s the last time you cried and why?",
    "What’s your favorite possession?",
    "Has anyone ever walked in on you in the bathroom?",
    "Who in this group would you want to swap lives with for a week?",
    "What was your biggest fear as a child?",
    "What’s your biggest fear today?",
    "What’s the most embarrassing thing your parents have caught you doing?",
    "Name a band you only pretend to like.",
    "What’s the last song that made you cry?",
    "Have you ever had a wardrobe malfunction?",
    "What’s the last thing you Googled?",
    "What is that one thing you would never do for all the money in the world?",
    "Who is your favorite person in your immediate family?",
    "If you could only hear one song for the rest of your life, what would it be?",
    "When’s the last time your partner embarrassed you?",
)

@Client.on_message(
    filters.command("truth")
)
async def truth(_, message):
    """ /truth strings """
    effective_string = random.choice(TRUTH_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Rather-------

WYR_STRINGS = (
    "Would you rather 🔴 go into the past and meet your ancestors or 🔵 go into the future and meet your great-great grandchildren?",
    "Would you rather 🔴 have more time or 🔵 more money?",
    "Would you rather 🔴 have a rewind button or 🔵 a pause button on your life?",
    "Would you rather 🔴 be able to talk with the animals or 🔵 speak all foreign languages?",
    "Would you rather 🔴 win the lottery or 🔵 live twice as long?",
    "Would you 🔴 feel worse if no one showed up to your wedding or 🔵 to your funeral?",
    "Would you rather 🔴 be without internet for a week, or 🔵 without your phone?",
    "Would you rather 🔴 meet your Nikola Tesla, or 🔵 the Elbert Einstein?",
    "Would you rather 🔴 the aliens that make first contact be robotic or 🔵 organic?",
    "Would you rather 🔴 lose the ability to read or 🔵 lose the ability to speak?",
)

@Client.on_message(
    filters.command("rather")
)
async def rather(_, message):
    """ /rather strings """
    effective_string = random.choice(WYR_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Dare-----

DARE_STRINGS = (
    "Change your profile pic to some naked character for 3 days.",
    "Do a photograph reveal.",
    "Share your telegram password.",
    "Send 'I Love You' to 20 people in your PM [Private Messaging] list and share screenshots of the task.",
    "Send hentai to 10 people in your PM [Private Messaging list and share screenshots of the task.",
    "Send your phone number to 10 people in the group and share screenshots of the task.",
    "Share your every social media account username.",
    "Send most embarrising photograph.",
    "Send 'I want your nudes' to 10 people in your PM [Private Messaging list and share screenshots of the task.]",
    "Make your phone number public for 3 minutes.",
    "Set your bio as, 'I am gay and I want to sleep with the person reading this right now' for 2 days.",
    "Send the pictures of your ex's panties.",
    "Ask for nudes from strangers and share screenshots of the task.",
    "Share screenshot from most recent chat on WhatsApp.",
    "Join/Start Voice Chat and sing a song.",
    "Join/Start Voice Chat and say, 'Ara Ara', in sexy voice",
    "Go to a random group with its Voice Chat ongoing and members speaking. Join the group and shout 'Fuck you all'. [Screen Record the task and send it in group.]",
    "Go to a random group with its Voice Chat ongoing and members speaking. Join the group and seduce a person. [Screen Record the task and send it in group.]",
    "Download a nude pic using google, PM it to a member of random Anime themed Group with caption as, 'These nudes are mine, wanna share yours?'. [Share screenshots of the task.]",
    "Open the top most chat on your PM List and screen record chat for last 3 days and send it in group.",
    "Reveal your instagram password to someone who is online.",
    "Click a photo of yours right now and send it in group.",
    "Set your bio as, 'Free blowjob if you send your nudes.' for 2 days.",
    "Join/Start Voice Chat and say, 'Onii Chan no Hentai', in sexy voice.",
    "Let someone from the players log in to your Telegram account.",
    "Send 10 most recent images from your galary.",
    "Send more suggestions to @tg",
)

@Client.on_message(
    filters.command("dare")
)
async def dare(_, message):
    """ /dare strings """
    effective_string = random.choice(DARE_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Tord------

TORD_STRINGS = (
    "Change your profile pic to a dog.",
    "Do a photograph reveal.",
    "Share your telegram password.",
    "Send 'I Love You' to 20 people in your PM [Private Messaging] list and share screenshots of the task.",
    "Send hentai to 10 people in your PM [Private Messaging list and share screenshots of the task.",
    "Send your phone number to 10 people in the group and share screenshots of the task.",
    "Share your every social media account username.",
    "Send most embarrising photograph.",
    "Send 'I want your nudes' to 10 people in your PM [Private Messaging list and share screenshots of the task.",
    "Make your phone number public for 3 minutes.",
    "Set your bio as, 'I am gay and I want to sleep with the person reading this right now' for 2 days.",
    " What’s the last lie you told?",
    "What was the most embarrassing thing you’ve ever done on a date?",
    "Have you ever accidentally hit something (or someone!) with your car?",
    "Name someone you’ve pretended to like but actually couldn’t stand.",
    "What’s your most bizarre nickname?",
    "What’s been your most physically painful experience?",
    "What bridges are you glad that you burned?",
    "What’s the craziest thing you’ve done on public transportation?",
    "If you met a genie, what would your three wishes be?",
    "If you could write anyone on Earth in for President of the United States, who would it be and why?",
    "What’s the meanest thing you’ve ever said to someone else?",
    "Who was your worst kiss ever?",
    "What’s one thing you’d do if you knew there no consequences?",
    "What’s the craziest thing you’ve done in front of a mirror?",
    "What’s the meanest thing you’ve ever said about someone else?",
    "What’s something you love to do with your friends that you’d never do in front of your partner?",
    "Who are you most jealous of?",
    "What do your favorite pajamas look like?",
    "Have you ever faked sick to get out of a party?",
    "Who’s the oldest person you’ve dated?",
    "How many selfies do you take a day?",
    "Meatloaf says he’d do anything for love, but he won’t do “that.” What’s your “that?”",
    "How many times a week do you wear the same pants?",
    "Would you date your high school crush today?",
    "Where are you ticklish?",
    "Do you believe in any superstitions? If so, which ones?",
    "What’s one movie you’re embarrassed to admit you enjoy?",
    "What’s your most embarrassing grooming habit?",
    "When’s the last time you apologized? What for?",
    "How do you really feel about the Twilight saga?",
    "Where do most of your embarrassing odors come from?",
    "Have you ever considered cheating on a partner?",
    "Have you ever cheated on a partner?",
    "Boxers or briefs?",
    "Have you ever peed in a pool?",
    "What’s the weirdest place you’ve ever grown hair?",
    "If you were guaranteed to never get caught, who on Earth would you murder?",
    "What’s the cheapest gift you’ve ever gotten for someone else?",
    "What app do you waste the most time on?",
    "What’s the weirdest thing you’ve done on a plane?",
    "Have you ever been nude in public?",
    "How many gossip blogs do you read a day?",
    "What is the youngest age partner you’d date?",
    "Have you ever picked your nose in public?",
    "Have you ever lied about your age?",
    "If you had to delete one app from your phone, which one would it be?",
    "What’s your most embarrassing late night purchase?",
    "What’s the longest you’ve gone without showering?",
    "Have you ever used a fake ID?",
    "Who’s your hall pass?",
    "Who will be your choice to become your boyfriend/girlfriend from the group?",
    "If you had a chance to kill someone, who would it be from the group?",
    "Who is the most hated and liked person in your group from your perspective?",
    "Have you ever loved someone, if so, who was it and for how long, if not, how will you show your love to them?",
    "If you were asked to propose someone from your friends on Telegram, who will be your first choice and why?",
    "If you were to hate someone from your friends on Telegram, who will be your first choice and why?",
    "What are your views on the topic of Human Cannibalism?",
    "If you were asked to kill someone in your most horrific way, how will it be?",
    "Join/Start Voice Chat and sing a song.",
    "Join/Start Voice Chat and say, 'Ara Ara', in sexy voice",
    "Go to a random group with its Voice Chat ongoing and members speaking. Join the group and shout 'Fuck you all'. [Screen Record the task and send it in group.]",
    "Go to a random group with its Voice Chat ongoing and members speaking. Join the group and seduce a person. [Screen Record the task and send it in group.]",
    "Download a nude pic using google, PM it to a member of random Anime themed Group with caption as, 'These nudes are mine, wanna share yours?'. [Share screenshots of the task.]",
    "Open the top most chat on your PM List and screen record chat for last 3 days and send it in group.",
    "Reveal your instagram password to someone who is online.",
    "Click a photo of yours right now and send it in group.",
    "Set your bio as, 'Free blowjob if you send your nudes.' for 2 days.",
    "Join/Start Voice Chat and say, 'Onii Chan no Hentai', in sexy voice.",
    "Let someone from the players log in to your Telegram account.",
    "Send 10 most recent images from your galary.",
)

@Client.on_message(
    filters.command("tord")
)
async def tord(_, message):
    """ /tord strings """
    effective_string = random.choice(TORD_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Good night----

GDNIGHT_STRINGS = (
    "`Good night keep your dreams alive`",
    "`Night, night, to a dear friend! May you sleep well!`",
    "`May the night fill with stars for you. May counting every one, give you contentment!`",
    "`Wishing you comfort, happiness, and a good night’s sleep!`",
    "`Now relax. The day is over. You did your best. And tomorrow you’ll do better. Good Night!`",
    "`Good night to a friend who is the best! Get your forty winks!`",
    "`May your pillow be soft, and your rest be long! Good night, friend!`",
    "`Let there be no troubles, dear friend! Have a Good Night!`",
    "`Rest soundly tonight, friend!`",
    "`Have the best night’s sleep, friend! Sleep well!`",
    "`Have a very, good night, friend! You are wonderful!`",
    "`Relaxation is in order for you! Good night, friend!`",
    "`Good night. May you have sweet dreams tonight.`",
    "`Sleep well, dear friend and have sweet dreams.`",
    "`As we wait for a brand new day, good night and have beautiful dreams.`",
    "`Dear friend, I wish you a night of peace and bliss. Good night.`",
    "`Darkness cannot last forever. Keep the hope alive. Good night.`",
    "`By hook or crook you shall have sweet dreams tonight. Have a good night, buddy!`",
    "`Good night, my friend. I pray that the good Lord watches over you as you sleep. Sweet dreams.`",
    "`Good night, friend! May you be filled with tranquility!`",
    "`Wishing you a calm night, friend! I hope it is good!`",
    "`Wishing you a night where you can recharge for tomorrow!`",
    "`Slumber tonight, good friend, and feel well rested, tomorrow!`",
    "`Wishing my good friend relief from a hard day’s work! Good Night!`",
    "`Good night, friend! May you have silence for sleep!`",
    "`Sleep tonight, friend and be well! Know that you have done your very best today, and that you will do your very best, tomorrow!`",
    "`Friend, you do not hesitate to get things done! Take tonight to relax and do more, tomorrow!`",
    "`Friend, I want to remind you that your strong mind has brought you peace, before. May it do that again, tonight! May you hold acknowledgment of this with you!`",
    "`Wishing you a calm, night, friend! Hoping everything winds down to your liking and that the following day meets your standards!`",
    "`May the darkness of the night cloak you in a sleep that is sound and good! Dear friend, may this feeling carry you through the next day!`",
    "`Friend, may the quietude you experience tonight move you to have many more nights like it! May you find your peace and hold on to it!`",
    "`May there be no activity for you tonight, friend! May the rest that you have coming to you arrive swiftly! May the activity that you do tomorrow match your pace and be all of your own making!`",
    "`When the day is done, friend, may you know that you have done well! When you sleep tonight, friend, may you view all the you hope for, tomorrow!`",
    "`When everything is brought to a standstill, friend, I hope that your thoughts are good, as you drift to sleep! May those thoughts remain with you, during all of your days!`",
    "`Every day, you encourage me to do new things, friend! May tonight’s rest bring a new day that overflows with courage and exciting events!`",
)

@Client.on_message(
    filters.command("goodnight")
)
async def goodnight(_, message):
    """ /goodnight strings """
    effective_string = random.choice(GDNIGHT_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Gmorning----

GDMORNING_STRINGS = (
    "`Life is full of uncertainties. But there will always be a sunrise after every sunset. Good morning!`",
    "`It doesn’t matter how bad was your yesterday. Today, you are going to make it a good one. Wishing you a good morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good morning!`",
    "`May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning!`",
    "`May the sun shower you with blessings and prosperity in the days ahead. Good morning!`",
    "`Every sunrise marks the rise of life over death, hope over despair and happiness over suffering. Wishing you a very enjoyable morning today!`",
    "`Wake up and make yourself a part of this beautiful morning. A beautiful world is waiting outside your door. Have an enjoyable time!`",
    "`Welcome this beautiful morning with a smile on your face. I hope you’ll have a great day today. Wishing you a very good morning!`",
    "`You have been blessed with yet another day. What a wonderful way of welcoming the blessing with such a beautiful morning! Good morning to you!`",
    "`Waking up in such a beautiful morning is a guaranty for a day that’s beyond amazing. I hope you’ll make the best of it. Good morning!`",
    "`Nothing is more refreshing than a beautiful morning that calms your mind and gives you reasons to smile. Good morning! Wishing you a great day.`",
    "`Another day has just started. Welcome the blessings of this beautiful morning. Rise and shine like you always do. Wishing you a wonderful morning!`",
    "`Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today. Good morning!`",
    "`A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. Here’s me wishing you a good morning!`",
    "`The darkness of night has ended. A new sun is up there to guide you towards a life so bright and blissful. Good morning dear!`",
    "`Wake up, have your cup of morning tea and let the morning wind freshen you up like a happiness pill. Wishing you a good morning and a good day ahead!`",
    "`Sunrises are the best; enjoy a cup of coffee or tea with yourself because this day is yours, good morning! Have a wonderful day ahead.`",
    "`A bad day will always have a good morning, hope all your worries are gone and everything you wish could find a place. Good morning!`",
    "`A great end may not be decided but a good creative beginning can be planned and achieved. Good morning, have a productive day!`",
    "`Having a sweet morning, a cup of coffee, a day with your loved ones is what sets your “Good Morning” have a nice day!`",
    "`Anything can go wrong in the day but the morning has to be beautiful, so I am making sure your morning starts beautiful. Good morning!`",
    "`Open your eyes with a smile, pray and thank god that you are waking up to a new beginning. Good morning!`",
    "`Morning is not only sunrise but A Beautiful Miracle of God that defeats the darkness and spread light. Good Morning.`",
    "`Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good Morning!`",
    "`If you want to gain health and beauty, you should wake up early. Good Morning!`",
    "`Birds are singing sweet melodies and a gentle breeze is blowing through the trees, what a perfect morning to wake you up. Good morning!`",
    "`This morning is so relaxing and beautiful that I really don’t want you to miss it in any way. So, wake up dear friend. A hearty good morning to you!`",
    "`Mornings come with a blank canvas. Paint it as you like and call it a day. Wake up now and start creating your perfect day. Good morning!`",
    "`Every morning brings you new hopes and new opportunities. Don’t miss any one of them while you’re sleeping. Good morning!`",
    "`Start your day with solid determination and great attitude. You’re going to have a good day today. Good morning my friend!`",
    "`Friendship is what makes life worth living. I want to thank you for being such a special friend of mine. Good morning to you!`",
    "`A friend like you is pretty hard to come by in life. I must consider myself lucky enough to have you. Good morning. Wish you an amazing day ahead!`",
    "`The more you count yourself as blessed, the more blessed you will be. Thank God for this beautiful morning and let friendship and love prevail this morning.`",
    "`Wake up and sip a cup of loving friendship. Eat your heart out from a plate of hope. To top it up, a fork full of kindness and love. Enough for a happy good morning!`",
    "`It is easy to imagine the world coming to an end. But it is difficult to imagine spending a day without my friends. Good morning.`",
)

@Client.on_message(
    filters.command("morning")
)
async def morning(_, message):
    """ /morning strings """
    effective_string = random.choice(GDMORNING_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Abuse----

ABUSE_STRINGS = (
    "Owww ... Such a stupid idiot.",
    "Don't drink and type.",
    "I think you should go home or better a mental asylum.",
    "Command not found. Just like your brain.",
    "Do you realize you are making a fool of yourself? Apparently not.",
    "You can type better than that.",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",
    "Sorry, we do not sell brains.",
    "Believe me you are not normal.",
    "I bet your brain feels as good as new, seeing that you never use it.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "Zombies eat brains... you're safe.",
    "You didn't evolve from apes, they evolved from you.",
    "Come back and talk to me when your I.Q. exceeds your age.",
    "I'm not saying you're stupid, I'm just saying you've got bad luck when it comes to thinking.",
    "What language are you speaking? Cause it sounds like bullshit.",
    "Stupidity is not a crime so you are free to go.",
    "You are proof that evolution CAN go in reverse.",
    "I would ask you how old you are but I know you can't count that high.",
    "As an outsider, what do you think of the human race?",
    "Brains aren't everything. In your case they're nothing.",
    "Ordinarily people live and learn. You just live.",
    "I don't know what makes you so stupid, but it really works.",
    "Keep talking, someday you'll say something intelligent! (I doubt it though)",
    "Shock me, say something intelligent.",
    "Your IQ's lower than your shoe size.",
    "Alas! Your neurotransmitters are no more working.",
    "Are you crazy you fool.",
    "Everyone has the right to be stupid but you are abusing the privilege.",
    "I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.",
    "You should try tasting cyanide.",
    "Your enzymes are meant to digest rat poison.",
    "You should try sleeping forever.",
    "Pick up a gun and shoot yourself.",
    "You could make a world record by jumping from a plane without parachute.",
    "Stop talking BS and jump in front of a running bullet train.",
    "Try bathing with Hydrochloric Acid instead of water.",
    "Try this: if you hold your breath underwater for an hour, you can then hold it forever.",
    "Go Green! Stop inhaling Oxygen.",
    "God was searching for you. You should leave to meet him.",
    "give your 100%. Now, go donate blood.",
    "Try jumping from a hundred story building but you can do it only once.",
    "You should donate your brain seeing that you never used it.",
    "Volunteer for target in an firing range.",
    "Head shots are fun. Get yourself one.",
    "You should try swimming with great white sharks.",
    "You should paint yourself red and run in a bull marathon.",
    "You can stay underwater for the rest of your life without coming back up.",
    "How about you stop breathing for like 1 day? That'll be great.",
    "Try provoking a tiger while you both are in a cage.",
    "Have you tried shooting yourself as high as 100m using a canon.",
    "You should try holding TNT in your mouth and igniting it.",
    "Try playing catch and throw with RDX its fun.",
    "I heard phogine is poisonous but i guess you wont mind inhaling it for fun.",
    "Launch yourself into outer space while forgetting oxygen on Earth.",
    "You should try playing snake and ladders, with real snakes and no ladders.",
    "Dance naked on a couple of HT wires.",
    "Active Volcano is the best swimming pool for you.",
    "You should try hot bath in a volcano.",
    "Try to spend one day in a coffin and it will be yours forever.",
    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",
    "You can be the first person to step on sun. Have a try.",
)

@Client.on_message(
    filters.command("abuse")
)
async def abuse(_, message):
    """ /abuse strings """
    effective_string = random.choice(ABUSE_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

# Cry-----

CRI_STRINGS = (
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
)

@Client.on_message(
    filters.command("cry")
)
async def cry(_, message):
    """ /cry strings """
    effective_string = random.choice(CRI_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)


RUNML_STRINGS = (
    "ഇരുട്ട് നിറഞ്ഞ എന്റെ ഈ ജീവിതത്തിലേക്ക് ഒരു തകർച്ചയെ \
    ഓർമ്മിപ്പിക്കാൻ എന്തിന് ഈ ഓട്ടക്കാലണ ആയി നീ വന്നു",
    "നമ്മൾ നമ്മൾ പോലുമറിയാതെ അധോലോകം ആയി മാറിക്കഴിഞ്ഞിരിക്കുന്നു ഷാജിയേട്ടാ...",
    "എന്നെ ചീത്ത വിളിക്കു... വേണമെങ്കിൽ നല്ല ഇടി ഇടിക്കു... പക്ഷെ ഉപദേശിക്കരുത്.....",
    "ഓ ബ്ലഡി ഗ്രാമവാസീസ്!",
    "സീ മാഗ്ഗി ഐ ആം ഗോയിങ് ടു പേ ദി ബിൽ.",
    "പോരുന്നോ എന്റെ കൂടെ!",
    "തള്ളെ കലിപ്പ് തീരണില്ലല്ലോ!!",
    "ശബരിമല ശാസ്താവാണെ ഹരിഹരസുതനാണെ ഇത് ചെയ്തവനെ ഞാൻ പൂട്ടും നല്ല മണിച്ചിത്രത്താഴിട്ട് പൂട്ടും .",
    "ഞാൻ കണ്ടു...!! കിണ്ടി... കിണ്ടി...!",
    "മോന്തയ്ക്കിട്ട് കൊടുത്തിട്ട് ഒന്ന് എടുത്ത് കാണിച്ചുകൊടുക്ക് അപ്പോൾ കാണും ISI മാർക്ക് ",
    "ഡേവീസേട്ട, കിങ്ഫിഷറിണ്ടാ... ചിൽഡ്...! .",
    "പാതിരാത്രിക്ക് നിന്റെ അച്ഛൻ ഉണ്ടാക്കി വെച്ചിരിക്കുന്നോ പൊറോട്ടയും ചിക്കനും....",
    "ഇത് ഞങ്ങളുടെ പണിസാധനങ്ങളാ രാജാവേ.",
    "കളിക്കല്ലേ കളിച്ചാൽ ഞാൻ തീറ്റിക്കുമെ പുളിമാങ്ങ....",
    "മ്മക്ക് ഓരോ ബിയറാ കാച്ചിയാലോ...",
    "ഓ പിന്നെ നീ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് പ്രണയം.... നമ്മൾ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് കമ്പി...",
    "കള്ളടിക്കുന്നവനല്ലേ കരിമീനിന്റെ സ്വാദറിയു.....",
    "ഡാ വിജയാ നമുക്കെന്താ ഈ ബുദ്ധി നേരത്തെ തോന്നാതിരുന്നത്...!",
    "ഇത്രേം കാലം എവിടെ ആയിരുന്നു....!",
    "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ....",
    "എനിക്കറിയാം ഇവന്റെ അച്ഛന്റെ പേര് ഭവാനിയമ്മ എന്നാ....",
    "ഡാ ദാസാ... ഏതാ ഈ അലവലാതി.....",
    "ഉപ്പുമാവിന്റെ ഇംഗ്ലീഷ് സാൾട് മംഗോ ട്രീ.....",
    "മക്കളെ.. രാജസ്ഥാൻ മരുഭൂമിയിലേക്ക് മണല് കയറ്റിവിടാൻ നോക്കല്ലേ.....",
    "നിന്റെ അച്ഛനാടാ പോൾ ബാർബർ....",
    "കാർ എൻജിൻ ഔട്ട് കംപ്ലീറ്റ്‌ലി.....",
    "ഇത് കണ്ണോ അതോ കാന്തമോ...",
    "നാലാമത്തെ പെഗ്ഗിൽ ഐസ്‌ക്യൂബ്സ് വീഴുന്നതിനു മുൻപ് ഞാൻ അവിടെ എത്തും.....",
    "അവളെ ഓർത്ത് കുടിച്ച കല്ലും നനഞ്ഞ മഴയും വേസ്റ്റ്....",
    "എന്നോട് പറ ഐ ലവ് യൂ ന്ന്....",
    "അല്ല ഇതാര് വാര്യംപിള്ളിയിലെ മീനാക്ഷി അല്ലയോ... എന്താ മോളെ സ്കൂട്ടറില്....",
    "ഓ.. ധിക്കാരം... പഴേപോലെ തന്നെ....ഒരു മാറ്റോമില്ല.....ചുമ്മാതല്ല ഗതി പിടിക്കാത്തത്....!!!",
    "അള്ളാ... പിള്ളേരുടെ ഓരോ... പെഷനെ...",
    "എനിക്ക് എഴുതാൻ അല്ലെ അറിയൂ സാറേ.... വായിക്കാൻ അറിയില്ലല്ലോ....",
    "ഇന്ന് ഇനി നീ മിണ്ടരുത്... ഇന്നത്തെ കോട്ട കഴിഞ്ഞ്.....",
    "ചാരമാണെന്ന് കരുതി ചെകയാൻ നിൽക്കണ്ട കനൽ കെട്ടിട്ടില്ലെങ്കിൽ പൊള്ളും.",
    "ഒറ്റ ജീവിതമേ ഉള്ളു മനസിലാക്കിക്കോ, സ്വർഗ്ഗമില്ല നരകമില്ല, 'ഒറ്റ ജീവിതം', അത് എവിടെ എങ്ങനെ വേണമെന്ന് അവനവൻ തീരുമാനിക്കും",
    "വാട്ട് എ ബോംബെസ്റ്റിക് എക്സ്പ്ലോഷൻ! സച് എ ടെറിഫിക് ഡിസ്ക്ലോസ്!!",
    "ഗോ എവേ സ്ടുപ്പിഡ് ഇൻ ദി ഹൗസ് ഓഫ് മൈ വൈഫ്‌ ആൻഡ് ഡോട്ടർ യൂവിൽ നോട്ട് സി എനി മിനിറ്റ് ഓഫ് ദി ടുഡേ... ഇറങ്ങി പോടാ..",
    "ഐ കാൻ ഡു ദാറ്റ്‌ ഡു കാൻ ഐ ദാറ്റ്‌",
    "ക്രീം ബിസ്കറ്റിൽ ക്രീം ഉണ്ടന്ന് കരുതി ടൈഗർ ബിസ്കറ്റിൽ ടൈഗർ ഉണ്ടാകണമെന്നില്ല. പണി പാളും മോനെ...",
    "പട പേടിച്ചു പന്തളത്തു ചെന്നപ്പോ പന്തോം കുത്തി പട പന്തളത്തോട്ടെന്ന് പറഞ്ഞ പോലെ ആയല്ലോ.",
    "എന്റ കർത്താവെ.... എന്നെ നീ നല്ലവനാകാൻ സമ്മതിക്കൂല്ല അല്ലെ.",
    "കാർ എൻജിൻ ഔട്ട് കംപ്ലീറ്റ്‌ലി......",
    "തള്ളെ കലിപ്പ് തീരണില്ലല്ലോ!!",
    "പാതിരാത്രിക്ക് നിന്റെ അച്ഛൻ ഉണ്ടാക്കി വെച്ചിരിക്കുന്നോ പൊറോട്ടയും ചിക്കനും....",
    "ഓ പിന്നെ നീ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് പ്രണയം.... നമ്മൾ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് കമ്പി....",
    "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ....",
    "അവളെ ഓർത്ത് കുടിച്ച കള്ളും നനഞ്ഞ മഴയും വേസ്റ്റ്....",
    "ഇത്രേം കാലം എവിടെ ആയിരുന്നു....!",
    "ഇൻഗ്ലീഷ് തീരെ പിടി ഇല്ല അല്ലെ....",
    "ആൾ ദി ഡ്രീംസ്‌ ലൈക്‌ ട്വിങ്കിൽ സ്റ്റാർസ്...",
    "എന്റെ പ്രാന്തൻ മുത്തപ്പാ അവനെ ഒരു വഴിയാക്കി തരണേ",
    "പെങ്ങളെ കെട്ടിയ സ്ത്രീധന തുക തരുമോ അളിയാ",
    "നീ വല്ലാതെ ക്ഷീണിച്ചു പൊയി",
    "കണ്ണിലെണ്ണയൊഴിച്ചു കാത്തിരിക്കുവായിരുന്നളിയാ.",
    "ചെല്ലാക്കണ്ടു എന്നിച്ചു പോടാ തടി.യാ .\
    ഷട്ട് ഉഒ യുവർ മൗത് ബ്ലഡി gramavasis.",
    "പോയി ചാവട .\
    നിന്നെ കൊണ്ട് ചാവാൻ patto.",
    "നിന്നെ കൊണ്ട് നാട്ടുകാർക്കും ഗുണോല്ല്യ വിട്ടുകാർക്കും ഗുണോല്ല്യ എന്തിനാ ഇങ്ങനെ നാണം കേട്ടു ജീവിക്കുന്നട പാട് വാഴെ ചെങ്കതളി വാഴ .",
)

@Client.on_message(
    filters.command("runml")
)
async def runml(_, message):
    """ /runml strings """
    effective_string = random.choice(RUNML_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)


ANIME_STRING = (
    "Typical of Goku to say something that crazy…",
    "Excuse me but are you by any chance the oddball in your family?– Ash Ketchum",
    "The world isn't perfect. But it's there for us, doing the best it can....that's what makes it so damn beautiful.~ Roy Mustang (Full Metal Alchemist)",
    "To know sorrow is not terrifying. What is terrifying is to know you can't go back to happiness you could have.~ Matsumoto Rangiku (Bleach)",
    "Those who stand at the top determine what's wrong and what's right! This very place is neutral ground! Justice will prevail, you say? But of course it will! Whoever wins this war becomes justice!~ Don Quixote Doflamingo (One Piece)",
    "Fear is freedom! Subjugation is liberation! Contradiction is truth! Those are the facts of this world! And you will all surrender to them, you pigs in human clothing!~ Satsuki Kiryuuin (Kill la Kill)",
    "I am the hope of the universe. I am the answer to all living things that cry out for peace. I am protector of the innocent. I am the light in the darkness. I am truth. Ally to good! Nightmare to you!~ Son Goku (Dragon Ball Z)",
    "Religion, ideology, resources, land, spite, love or just because… No matter how pathetic the reason, it’s enough to start war. War will never cease to exist… reasons can be thought up after the fact… Human nature pursues strife.~ Paine (Naruto Shippuden)",
    "People, who can’t throw something important away, can never hope to change anything.~ Armin Arlert (Shingeki no Kyojin / Attack on Titan)",
    "I want you to be happy. I want you to laugh a lot. I don’t know what exactly I’ll be able to do for you, but I’ll always be by your side.~ Kagome (InuYasha)",
    "Thinking you’re no-good and worthless is the worst thing you can do~ Nobito (Doraemon)"
    "Don’t give up, there’s no shame in falling down! True shame is to not stand up again!~ Shintaro Midorima (Kuroko No Basket)",
    "The true measure of a shinobi is not how he lives but how he dies. It’s not what they do in life but what they did before dying that proves their worth.",
    "Knowing you’re different is only the beginning. If you accept these differences you’ll be able to get past them and grow even closer.– Miss Kobayashi",
    "Giving up is what kills people.– Hellsing",
    "No matter how deep the night, it always turns to day, eventually. – One Piece",
    "A dream is worth less than nothing if you don’t have someone else to share it.~Dousan Saitou",
    "You’ll only realize that you truly love someone if they already caused you enormous pain. Your enemies can never hurt you the way your loved ones can. It’s the people close to your heart that can give you the most piercing wound. Love is a double-edged sword, it can heal the wound faster or it can sink the blade even deeper.– Kenshin Himura",
    "I do not need a Heaven. However, if I must go to Heaven then please, God, do not divide Heaven in two. Please do not divide the robots from the humans.– Chiisana Hoshi yo Yume",
    "What you can’t accomplish alone, becomes doable when you’re with someone else.– Taichi Yaegashi",
    "Just like games, no matter how well you have things lined up in your life, there’s always something to keep you on your toes.– Junichirou Kagami",
    "Do exactly as you like. That is the true meaning of pleasure. Pleasure leads to joy and joy leads to happiness.– Gilgamesh",
    "If you can’t do something, then don’t. Focus on what you can do.~Shiroe",
    "You can call me what you like, but I will be taking your cake.-L (from Death Note)",
    "This world is rotten. The rotten should die.― Tsugumi Ohba",
    "Kakashi~Things i like and things i hate…. I don’t feel like telling you that. My dreams for the future… Never really thought about it. As for my hobbies… I have lots of hobbies",
    "Most of us can relate to Shikamaru… Genius at birth, Lazy by choice",
    "Yo momma’s so fat. Kakashi uses Kamui on her and runs out of Chakra",
    "Any girl can be glamorous. All you have to do is stand still and look stupid",
    "The moment you find the courage to give up your life for someone… would be the moment you understand love",
    "Love, passion, why do we get caught up by such troublesome feelings? The mind couldn’t ever get things straight, and you lose control to know what is sensible. Deep down it’s all so vexing",
    "Feelings you have for each other will not be known unless you voice them",
    "Sometimes good people make bad choices, it doesn’t mean they are bad people, it means they’re human. -Sui Ishida",
    "Rather than a person who hurts others, become the person getting hurt. -Sui Ishida",
    "Everybody makes a wrong turn once in a while– Ash Ketchum",
    "Make your wonderful dream a reality, it will become your truth. If anyone can, it’s you.– N, Pokemon Black/White",
    "It’s more important to master the cards you’re holding than to complain about the ones your opponent was dealt.– Grimsley",
    "We do have a lot in common. The same earth, the same air, the same sky. Maybe if we started looking at what’s the same, instead of looking at what’s different, well, who knows?– Meowth",
    "That day four years ago… When I wasn’t needed by anyone. When nobody cared about me. When I had given up on living and was about to jump off the roof of a building… FB saved me with a single message. I didn’t care if it was a joke or not. I was just happy that somebody knew… that I was alive… that it was OK for me to live.~Moeka Kiryuu",
    "Look, even if we were enemies in the world you were before, right now I’m your only ally. Even if the whole world turned against you, I would continue to be your only ally.– Moeka Kiryuu",
    "When I realized, I was already on the roof of a building… I had come to hate everything. I was sick of sitting in my room holding my knees too. If nobody was going to notice or care if I died then… what’s the point in living?~Meoka Kiryuu",
    "It is those who possess wisdom who are the greatest fools. History has shown us this. You could say that this is the final warning from God to those who resist.– Rintaro Okabe",
    "The universe has a beginning, but no end. — Infinity. Stars, too, have their own beginnings, but their own power results in their destruction. — Finite.– Rintaro Okabe"
    "Living should mean no do-overs. This is for the best.~Rintaro Okabe",
    "What kind of mad scientist worries about not getting enough vegetables?– Rintaro Okabe",
    "There are two types of lies: Lies that hurt, and lies that don’t hurt.– Itaru Hashida",
    "There are two things that collectors always want. The first is an item of extreme rarity. The second is colleagues to whom they can brag about their collection.- Kurapika",
    "People only find me interesting because they can't tell whether I'm serious or not.- Killua Zoldyck",
    "If you want to get to know someone, find out what makes them angry.- Gon Freecss",
    "It takes a mere second for treasure to turn to trash.- Hisoka Morow",
    "Human potential for evolution is limitless. - Isaac Netero",
    "You should enjoy the little detours to the fullest. Because that's where you'll find things more important than what you want.- Ging Freecss",
    "You Want To Keep Everyone From Dying? That’s Naïve. It’s War. People Die-Monkey D. Luffy",
    "Justice Will Prevail, You Say? But Of Course, It Will! Whoever Wins This War Becomes Justice!-Donquixote Doflamingo",
    "People’s Dreams... Have No Ends -Marshall 'Blackbeard' D. Teach",
    "Only I Can Call My Dream Stupid!-Roronoa Zoro",
    "When Do You Think People Die? When They Are Shot In The Heart With A Pistol? No. When They Are Ravaged By An Uncurable Disease? No. When They Drink A Soup Made From Poisonous Mushrooms? No. It’s When... They Are Forgotten!-Dr.Hiriluk",
)

@Client.on_message(
    filters.command("funanimes")
)
async def animeds(_, message):
    """ /animes strings """
    effective_string = random.choice(ANIME_STRING)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
