import discord
import sys

from . import Bot

client = discord.Client()
bot = Bot(client)

TOKEN = "NDQ0NjE0NDk2MzMwNDQ4ODk2.De7eig.hy2WrY6ahP-FnUPdEMGyTtKPPY8"

@client.event
async def on_ready():
    # on ready is called when the bot has finished logging in and setting things up
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$end"):
        await bot.close(message)

    if message.content.startswith("$help"):
        await bot.help(message)

    if message.content.startswith("$how_to_type"):
        await bot.print_formatting_structures(message)

    if message.content.startswith("$norton"):
        await bot.print_norton_emoji(message)

client.run(TOKEN)
