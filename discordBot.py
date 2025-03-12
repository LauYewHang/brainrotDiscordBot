# Discord's API
import discord
from discord.ext import commands

# bot's token
import bot_token

# create a new class extends from discord.ext.commands.Bot
class uwuBrainrotBot(commands.Bot):
    async def on_ready(self):
        print("It is brainrot time everyone!!")

# create an Intents for the bot
# the integer argument is the `permission integer` from Bot Permissions section of Bot tab (which you tick which permission you need like send messages, read messages)
botIntents = discord.Intents(113664)

# create a bot object
myBrainrotBot = uwuBrainrotBot(command_prefix = "? ", intents = botIntents)

# run the discord bot
myBrainrotBot.run(bot_token.uwuMyToken)