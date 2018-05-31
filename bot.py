import discord
import sys
import time

class Bot():
    def __init__(self, client):
        self.client = client

    async def help(self, message):
        await message.channel.send("***Commands:*** `$help`, `$end`, `$how_to_type`")

    async def print_formatting_structures(self, message):
        await message.channel.send('__**Typing formatting:**__')
        await message.channel.send('\*\*bold\*\*')
        await message.channel.send('\*\*\*bold italics\*\*\*')
        await message.channel.send('\_\_underline\_\_')
        await message.channel.send('\*italics\* or \_italics\_')
        await message.channel.send('\_\_\*underline italics\*\_\_')
        await message.channel.send('\_\_\*\*\*underline bold italics\*\*\*\_\_')
        await message.channel.send('\~\~Strikethrough\~\~')

    async def print_norton_emoji(self, message):
        for x in range(10):
            time.sleep(5)
            await self.create_emoji(message)

    async def create_emoji(self, message): 
        await message.channel.send('<donttip:451739289949044737>')
        
    async def close(self, message):
        """ Closes the application and logs out the bot. """
        await message.channel.send("Closing the bot...")
        self.client.logout()
        sys.exit()
