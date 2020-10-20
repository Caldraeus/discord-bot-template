import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import sys, traceback
from os import listdir
from os.path import isfile, join

bot = discord.Client()
prefix = ';'
bot = commands.Bot(command_prefix=prefix, description="WaifuBattle Bot", case_insensitive=True)
bot.remove_command("help")

if __name__ == '__main__': # Cog loader v2
    def load_dir_files(path):
        print("\n")
        for item in listdir(path):
            if os.path.isdir(path) and item != ".DS_Store" and item != "__pycache__" and not item.endswith(".py"):
                new_path = path+f"/{item}"
                load_dir_files(new_path)
            elif item.endswith(".py"):
                new_path = path+f"/{item}"
                new_path = new_path.replace(".py", "")
                load_path = new_path.replace("/", ".")
                num = 20
                for letter in str(item):
                    num -= 1
                empty = ""
                for i in range(num): # Makes things look nicer(ish?) in the console... lol
                    empty += " "
                try:
                    print(f"Loading {item}...", end = " ")# print(f"[{path}] : Loading {item}...", end = " ")
                    bot.load_extension(load_path)
                    print(f"{empty}[SUCCESS]")
                except (discord.ClientException, ModuleNotFoundError):
                    print(f"\n{empty}[FAILURE]")
                    print(f'Failed to load extension {item}.\n')
                    traceback.print_exc()

    load_dir_files('cogs')

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


bot.run('NjcxMTk2Mjc1MTQzNzM3MzQ1.Xrg6kA.CV1TEdFj2bllLznFWapk2pZL_pc')
