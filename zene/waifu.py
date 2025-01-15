from discord.ext import commands
import requests
import json

class hentai_random(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def waifu(self,ctx):
        url = 'https://api.waifu.pics/sfw/waifu'
        a = json.dumps(requests.get(url).json())
        data = json.loads(a)
        await ctx.send(data["url"])

async def setup(bot):
    await bot.add_cog(hentai_random(bot))