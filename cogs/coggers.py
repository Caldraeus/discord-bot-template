import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import math
import os

class ProfileCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """
    @commands.command(aliases=['setcolour', "setc"])
    @commands.guild_only()
    async def profile_colour(self, ctx, r: int = None, g: int = None, b: int = None):
        if r != None and g != None and b != None:
            try:
                
                color = discord.Colour.from_rgb(r,g,b)
                embed = discord.Embed(colour=color)
                current = h.user_color(ctx.author.id)
                embed.set_author(name=f"Profile colour successfully changed to [{r}, {g}, {b}]. Previously set as {current}")
                h.user_color(ctx.author.id, [r, g, b])
                await ctx.send(embed=embed)
            except SyntaxError:
                await ctx.send("<:redtick:605424981245034511> | Numbers can not be lower than 0 or higher than 255.")
        else:
            await ctx.send("<:redtick:605424981245034511> | Invalid format. Example: `;setc 255 255 255`.")
    """

# A setup function the every cog has
def setup(bot):
    bot.add_cog(ProfileCommands(bot))
