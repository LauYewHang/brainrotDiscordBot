# Discord's API
import discord
from discord.ext import commands
from discord.ext import tasks

# bot's token
import bot_token



#______________________________________________________________________________________#

ratio_sentence = "ratio + dont care + didnt ask + cry about it + stay mad + get real + L + mald seethe cope harder + h0es mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your’re probably white + not funny didn’t laugh + you’re* + grammar issue + go outside + get good + reported + ad hominem + GG! + ur momdon’t care + didn’t ask + cry about it + stay mad + get real + L + mald seethe cope harder + hoes mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your’re a full time discordian + not funny didn’t laugh + you’re* + grammar issue + go outside + get good + your gay + reported + ad hominem + GG! + ur mom + unknown + random + biased + racially motivated + kys + ur unfunny +ratio don’t care + didn’t ask + cry about it + stay mad + get real + L + mald seethe copedon’t care + didn’t ask + cry about it + stay mad + get real + L + mald seethe cope harder + h0es mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your’re probably white + not funny didn’t laugh + you’re* + grammar issue + go outside + get good + reported + ad hominem + GG! + ur momdon’t care + didn’t ask + cry about it + stay mad + get real + L + mald seethe cope harder + hoes mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your’re a full time discordian + not funny didn’t laugh + you’re* + grammar issue + go outside + get good + your gay + reported + ad hominem + GG! + ur mom + unknown + random + biased + racially motivated + kys + ur unfunny +ratio don’t care + didn’t ask + cry about it + stay mad + get real + so bad + so ass"
ratio_terms = ratio_sentence.split(" + ")

messagesList = []
countList = []
#______________________________________________________________________________________#



#______________________________________________________________________________________#
# create a new class extends from discord.ext.commands.Bot
class uwuBrainrotBot(commands.Bot):
    async def on_ready(self):
        print("It is brainrot time everyone!!")
        task_loop.start()

# create an Intents for the bot
botIntents = discord.Intents.default()
# enable message (to read and send message)
botIntents.message_content = True

# create a bot object
myBrainrotBot = uwuBrainrotBot(command_prefix = "?", intents = botIntents)
#______________________________________________________________________________________#



#______________________________________________________________________________________#
# create a command (for myBrainrotBot)
@myBrainrotBot.command()
async def skibidi(context): # the function name "skibidi" is the command itself
    await context.send("uwu")
#______________________________________________________________________________________#



#______________________________________________________________________________________#
# keep repeating a task
# source: https://stackoverflow.com/questions/76063036/how-to-make-an-endless-loop-in-python-for-a-discord-bot
@tasks.loop(seconds=1)
async def task_loop():
    for i in range(0, len(messagesList)):
        checked_L = False
        if (len(messagesList[i].reactions) != 0):
            for j in messagesList[i].reactions:
                if (j.emoji == "🇱"):
                    checked_L = True
                    if (countList[i] != j.count):
                        countList[i] = j.count
                        reply = "Twin you got L + "
                        for k in range(0, j.count):
                            reply = reply + ratio_terms[k] + " "
                        await messagesList[i].reply(reply + ":skull:")
                        break
            if (not checked_L):
                countList[i] = 0
        else:
            countList[i] = 0
#______________________________________________________________________________________#

# safe version (prevent spam)
"""
@tasks.loop(seconds=1)
async def task_loop():
    for i in range(0, len(messagesList)):
        if (len(messagesList[i].reactions) != 0):
            for j in messagesList[i].reactions:
                if (j.emoji == "🇱"):
                    if (countList[i] < j.count):
                        countList[i] = j.count
                        reply = "You got L + "
                        for k in range(0, j.count):
                            reply = reply + ratio_terms[k] + " "
                        await messagesList[i].reply(reply)
"""

#______________________________________________________________________________________#
@myBrainrotBot.listen("on_message")
async def add_message(message):
    if (len(messagesList) < 100):
        messagesList.append(message)
        countList.append(0)
    else:
        messagesList.remove(messagesList[0])
        countList.remove(countList[0])
        messagesList.append(message)
        countList.append(0)
#______________________________________________________________________________________#



# alternative
"""
@commands.command()
async def skibidi(context):
    await context.send("uwu")

myBrainrotBot.add_command(skibidi) # you need to add the command yourself
"""

# run the discord bot
myBrainrotBot.run(bot_token.uwuMyToken)