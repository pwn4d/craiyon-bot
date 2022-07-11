import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

from cogs.craiyon import Craiyon

load_dotenv()

# ENV Vars
TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "c!")  # !craiyon

bot = commands.Bot(COMMAND_PREFIX, description='')

bot.add_cog(Craiyon(bot))


@bot.event
async def on_ready():
    """ Waits for ready """
    print(f"{bot.user} has connected to Discord!")
    await bot.change_presence(
        activity=discord.Activity(
            name=f"{COMMAND_PREFIX}help", type=discord.ActivityType.listening
        )
    )


bot.run(TOKEN)
