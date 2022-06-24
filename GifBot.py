import discord
from pprint import pprint
import random
import requests
import bs4
from bs4 import BeautifulSoup

#API
token = "DISCORD BOT TOKEN PURGED"

whitelist = [764138620549988384,
             144502614204219392]

#TardBot
payload = {
    'login_username': 'TardBot',
    'login_password': 'PASSWORD PURGED'
    }

Crews = [
    "• Rev†vaL •",
    "•| Dark Prophecy |•",
    "•|Morbid Purgatory|•",
    "* Sacred Force *",
    "Most Wanted",
    "xTard'sx",
    "FunkyTown",
    "Rev A1",
    "Rev A2",
    "..::ROMAN EMPIRE::..",
    "Outwar Immortals",
    "Arcanum",
    "Bolshevik Revolution"
]

Celebration_Gifs = [
    'https://tenor.com/view/-gif-4519334',
    'https://tenor.com/view/yes-wwe-oh-yes-yeah-gif-7549364',
    'https://tenor.com/view/im-the-best-racer-fox-sports-gif-5943746',
    'https://tenor.com/view/ian-wright-arsenal-boom-celebrate-yes-gif-15563964'
    'https://tenor.com/view/raptors-win-yes-gif-14340146'
    'https://tenor.com/view/fist-pump-kid-happy-celebrate-victory-gif-5228605'
    'https://tenor.com/view/will-smith-victory-smell-is-that-victory-i-smell-gif-13132961'
]
Loser_Gifs = [
    'https://tenor.com/view/sad-face-cry-baby-cute-gif-16293283',
    'https://tenor.com/view/crying-drinking-will-ferrell-gif-9981615',
    'https://tenor.com/view/sad-girl-gif-8382180',
    'https://tenor.com/view/sad-baby-frown-cry-tantrums-gif-4649018',
    'https://tenor.com/view/sad-eyes-so-sad-tears-gif-13901135'
    #'https://tenor.com/view/i-am-just-regrouping-its-been-a-long-fight-drake-drizzy-laugh-now-cry-later-gif-18175179',
    
]


class DiscordClient(discord.Client):
    async def on_ready(self):
        print("Login as")
        print(self.user)
        print("-------")




    async def on_message(message):
        embeds = message.embeds
        for embed in embeds:
            print(embed.to_dict())
    async def on_message(self, message):
        # Whenever a user other than bot says "hi"
        #print(message.content)
        if message.author.bot == False:
            messageContent = message.content.lower()
            if "/roll" in messageContent:
                r1 = random.randint(0, 1000)
                str1 = str(r1)
                Roll_Message = " Has rolled a "+ str1
                await message.channel.send(message.author.mention+ Roll_Message)

        
            if "/archives" in messageContent:
                await message.channel.send(random.choice(Archived_Quotes))
        if message.author.bot == True and message.author.id in whitelist:
            #print(message.content)
            if "```Drake has spawned!" in message.content:#.embeds(0).value:
                print("Drake")
                await message.channel.send('https://tenor.com/view/drake-peeking-sliding-looking-creep-gif-18108648')
            if "```Drake has Died." in message.content:
                print(message.content)
                await message.channel.send('https://tenor.com/view/i-am-just-regrouping-its-been-a-long-fight-drake-drizzy-laugh-now-cry-later-gif-18175177')
            if "```Ganja has Died." in message.content:
                print(message.content)
                await message.channel.send('https://tenor.com/view/chris-tucker-smoke-cigarettes-gif-13814074')
            if "```Zhul has Died." in message.content:
                print(message.content)
                await message.channel.send('https://tenor.com/view/zuul-there-is-no-dana-only-zuul-sick-gif-12114082')
            if message.embeds:  # -> Returns a List[Embed]
                # Check to see if XXXX is in the embeds description/title etc.
                #print(message.embed(0))
                if "Killed by:" in message.embeds[0].title:
                    #results = [crew for crew in Crews if (crew in message.embeds[0].title)]
                    if [crew for crew in Crews if (crew in message.embeds[0].title)]:
                        await message.channel.send(random.choice(Celebration_Gifs))
                        return 
                    else:
                        await message.channel.send(random.choice(Loser_Gifs))
                        await message.channel.send("HAAAAAAAAAAAAAALP")
                        return
            
client = DiscordClient()
client.run(token)
