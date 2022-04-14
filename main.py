import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sys, traceback
from os import listdir
from os.path import isfile, join
from discord.utils import find
from discord import Webhook, AsyncWebhookAdapter
import os

intents = discord.Intents.all()
bot = discord.Client()
bot = commands.Bot(command_prefix=";", description="Bot", case_insensitive=True, intents=intents)
bot.remove_command("help")


intents = discord.Intents.all() # All intents, alter if needed.
bot = discord.Client()

prefix = ';'

bot = commands.Bot(command_prefix=prefix, description="Bot", case_insensitive=True, intents=intents)
bot.remove_command("help")

if __name__ == '__main__': # Cog loader V3
    def load_dir_files(path, dash):
        #print("\n")
        for item in listdir(path):
            if os.path.isdir(path) and item != ".DS_Store" and item != "__pycache__" and not item.endswith(".py") and not item.endswith(".md") and not item.endswith(".json"):
                new_path = path+f"/{item}"
                load_dir_files(new_path, f"{dash}───")
            elif item.endswith(".py"):
                new_path = path+f"/{item}"
                new_path = new_path.replace(".py", "")
                load_path = new_path.replace("/", ".")
                num = 100
                for letter in str(item + dash):
                    num -= 1
                empty = ""
                for i in range(num): # Makes things look nicer in the console... lol
                    empty += " "
                try:
                    print(f"{dash} Loading {item}...", end = " ")# print(f"[{path}] : Loading {item}...", end = " ")
                    bot.load_extension(load_path)
                    print(f"{empty}[SUCCESS]")
                except (discord.ClientException, ModuleNotFoundError):
                    print(f"\n{empty}[FAILURE]")
                    print(f'Failed to load extension {item}.\n')
                    traceback.print_exc()

    load_dir_files('cogs' ,"├─")

@bot.event
async def on_ready():
    print(f'Success - Logged in.')
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command(aliases=['h'])
@commands.guild_only()
async def help(ctx, *, module = "general"):
    await ctx.send("N?A")
    """
    try:
        embed = h.get_help(module)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"<:redtick:605424981245034511> | No module named {module}.")
    """

@bot.command(aliases=['botinfo'])
@commands.guild_only()
async def about(ctx):
    await ctx.send("N?A")

@bot.command(aliases=['invite'])
@commands.guild_only()
async def invite_link(ctx):
    await ctx.send("N?A")


bot.run('HKJSHdkljsHLkjhskjDHKJShskjhdskjdhsjdhskdhhelloworldHDJKShKJDH')
