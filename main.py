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

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir('cogs') if isfile(join('cogs', f))]:
        try:
            bot.load_extension("cogs." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
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
