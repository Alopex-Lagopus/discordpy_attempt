import os

import discord
from discord.ext.commands import Bot

GUILD = os.getenv("D_GUILD")
TOKEN = os.getenv("D_TOKEN")


class MyCustomBot(Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents, command_prefix="!")
        self.synced = False

    async def setup_hook(self):
        await self.load_extension("extension_file")
        await self.tree.sync(guild=discord.Object(id=GUILD))

    async def on_ready(self):
        await self.wait_until_ready()
        print("Bot finished loading")

bot = MyCustomBot()

bot.run(TOKEN)
