import discord
from discord.ext import commands
import sys, traceback
from os import listdir
from os.path import isfile, join
import os
import asyncio

intents = discord.Intents.all() # All intents, alter if needed.

prefix = ';'

bot = commands.Bot(command_prefix=prefix, description="Bot", case_insensitive=True, intents=intents)
bot.remove_command("help")

async def load_dir_files(path, dash):
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
            if "special_classes" in path:
                num += 3
            for i in range(num): # Makes things look nicer in the console... lol
                empty += " "
            try:
                if "special_classes" in path:
                    dash = '├───────'
                print(f"{dash} Loading {item}...", end = " ")# print(f"[{path}] : Loading {item}...", end = " ")
                await bot.load_extension(load_path)
                print(f"{empty}[SUCCESS]")
            except (discord.ClientException, ModuleNotFoundError):
                print(f"\n{empty}[FAILURE]")
                print(f'Failed to load extension {item}.\n')
                traceback.print_exc()

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

@bot.command(aliases=['botinfo'])
@commands.guild_only()
async def about(ctx):
    await ctx.send("N?A")

@bot.command(aliases=['invite'])
@commands.guild_only()
async def invite_link(ctx):
    await ctx.send("N?A")

async def main():
    await load_dir_files('cogs' ,"├─")
    await bot.start("token here")

asyncio.run(main())

