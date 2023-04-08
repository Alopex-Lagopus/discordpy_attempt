import os

import discord
from discord.ext import commands
from discord import app_commands

GUILD = os.getenv("D_GUILD")

class MyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ### Works / Registered ###
    @app_commands.command(name="test_apc")
    async def testapc(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")

    ### Does not register? and prefix command doesn't work ###
    @commands.hybrid_command(name="testhybrid", with_app_command=True)
    async def testhybrid(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")

    ### Does not register (as expected), but prefix command works ###
    @commands.command(name="testcommand")
    async def testcommand(self, ctx):
        await ctx.send("Hello!")

### Doesn't work / Trying to add an app_command outside the cog ###
@app_commands.command(name="test_individual_apc")
async def test_individual_apc(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

### Works outside of cog ###
@commands.command(name="individual_command")
async def individual_command(ctx):
    await ctx.send("Hello!")

### Prefix works, but app_command doesn't ###
@commands.hybrid_command(name="individual_hybrid_command", with_app_command=True)
async def individual_hybrid_command(ctx):
    await ctx.send("Hello!")

async def setup(bot):

    await bot.add_cog(MyCommands(bot), guild=discord.Object(id=GUILD))
    bot.tree.add_command(test_individual_apc)
    bot.add_command(individual_command)
    bot.add_command(individual_hybrid_command)
