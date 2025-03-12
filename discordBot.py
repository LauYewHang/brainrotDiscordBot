# Discord's API
import discord
from discord.ext import commands

# bot's token
import bot_token

#______________________________________________________________________________________#
# create a new class extends from discord.ext.commands.Bot
class uwuBrainrotBot(commands.Bot):
    async def on_ready(self):
        print("It is brainrot time everyone!!")

# create an Intents for the bot
botIntents = discord.Intents.default()
# enable message (to read and send message)
botIntents.message_content = True

# create a bot object
myBrainrotBot = uwuBrainrotBot(command_prefix = "?", intents = botIntents)
#______________________________________________________________________________________#

# create a command (for myBrainrotBot)
@myBrainrotBot.command()
async def skibidi(context): # the function name "skibidi" is the command itself
    await context.send("uwu")

# alternative
"""
@commands.command()
async def skibidi(context):
    await context.send("uwu")

myBrainrotBot.add_command(skibidi) # you need to add the command yourself
"""

# run the discord bot
myBrainrotBot.run(bot_token.uwuMyToken)