import discord
from discord.ext import commands

class owner_only(commands.Cog): # Example cog.
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def update(self, ctx, cog, new = None): # Example owner command to reload a cog.
        if new == None:
            lists = self.bot.extensions
            for item in lists:
                item = item.split('.')
                if item[-1] == cog.lower():
                    pwd = '.'.join(item)
                    break

            try:
                await self.bot.reload_extension(str(pwd))
                await ctx.send(f"Successfully updated `{pwd}` with [0] errors.")
            except UnboundLocalError:
                await ctx.send(f"❗ | Cog `{cog}` not found.")
        else:
            try:
                await self.bot.load_extension(cog)
                await ctx.send(f"Loaded new cog `{cog}`.")
            except ValueError:
                await ctx.send(f"❗ | Invalid path for `{cog}`.")

# A setup function the every cog has
async def setup(bot):
    await bot.add_cog(owner_only(bot))