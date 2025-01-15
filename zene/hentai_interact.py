from discord.ext import commands
import discord
import requests
import json
import random

nsfw_direct = 'Qua kênh NSFW mà xài'
warning = 'Xem hentai nhiều có hại cho sức khỏe. Chọn số dưới 10 thôi'

class hentai_random(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hen(self, ctx, number: int):
        if number <= 10:
            if ctx.channel.is_nsfw():
                for i in range(0, number):
                    url = ['https://api.waifu.pics/nsfw/waifu',
                           'http://api.nekos.fun:8080/api/lewd',
                           'http://api.nekos.fun:8080/api/hentai',
                           'https://api.waifu.pics/nsfw/neko',
                           'https://neko-love.xyz/api/v1/nekolewd']
                    a = json.dumps(requests.get(random.choice(url)).json())
                    if 'image' in a:
                        s = a.replace('image','url')
                        data = json.loads(s)
                    else:
                        data = json.loads(a)
                    await ctx.send(data["url"])
            else:
                await ctx.send(nsfw_direct)
        else:
            await ctx.send(warning)

    @commands.command()
    async def hentai(self, ctx, number: int):
        for i in range(0, number):
            url = [
                'https://api.waifu.pics/nsfw/waifu',
                'http://api.nekos.fun:8080/api/lewd',
                'http://api.nekos.fun:8080/api/hentai',
                'https://api.waifu.pics/nsfw/neko',
                'https://neko-love.xyz/api/v1/nekolewd'
                ]
            a = json.dumps(requests.get(random.choice(url)).json())
            if 'image' in a:
                s = a.replace('image','url')
                data = json.loads(s)
            else:
                data = json.loads(a)
            await ctx.send(data["url"])

    @commands.command()
    async def hentrap(self, ctx, number: int):
        if number <= 10:
            if ctx.channel.is_nsfw():
                url = 'https://api.waifu.pics/nsfw/trap'
                a = json.dumps(requests.get(url).json())
                data = json.loads(a)
                await ctx.send(data["url"])
            else:
                await ctx.send(nsfw_direct)
        else:
            await ctx.send(warning)

    @commands.command()
    async def henneko(self, ctx, number: int):
        if number <= 10:
            if ctx.channel.is_nsfw():
                for i in range(0, number):
                    url = ['https://api.waifu.pics/nsfw/neko',
                           'https://neko-love.xyz/api/v1/nekolewd']
                    a = json.dumps(requests.get(random.choice(url)).json())
                    data = json.loads(a)
                    await ctx.send(data["url"])
            else:
                await ctx.send(nsfw_direct)
        else:
            await ctx.send(warning)

    @commands.command()
    async def henbj(self, ctx):
        if ctx.channel.is_nsfw():
            url = 'https://api.waifu.pics/nsfw/blowjob'
            a = json.dumps(requests.get(url).json())
            data = json.loads(a)
            await ctx.send(data["url"])
        else:
            await ctx.send(nsfw_direct)

    @commands.command()
    async def mlem(self,ctx):
        url = 'http://api.nekos.fun:8080/api/lick'
        a = json.dumps(requests.get(url).json())
        data = json.loads(a)
        await ctx.send(data["image"])

    @commands.command()
    async def slap(self,ctx,*,god: discord.Member=None):
        try: 
            if god.id == 262844868919951360:
                await ctx.send('<@262844868919951360> Có đứa định slap Onii-sama. Để em xiên nó :angry:')
            else:
                url = 'http://api.nekos.fun:8080/api/slap'
                a = json.dumps(requests.get(url).json())
                data = json.loads(a)
                await ctx.send(data["image"])
        except:
            url = 'http://api.nekos.fun:8080/api/slap'
            a = json.dumps(requests.get(url).json())
            data = json.loads(a)
            await ctx.send(data["image"])

    @commands.command()
    async def waifu(self,ctx):
        url = 'https://api.waifu.pics/sfw/waifu'
        a = json.dumps(requests.get(url).json())
        data = json.loads(a)
        await ctx.send(data["url"])

async def setup(bot):
    await bot.add_cog(hentai_random(bot))