import discord
from discord.ext import commands
from hentai import Hentai, Format, Utils, Sort, Option, Tag

class nhentai(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def nhentai (self, ctx, *, arg):
        if ctx.channel.is_nsfw():
            doujin = Hentai(arg)
            Hentai.exists(doujin.id)
            await ctx.send(f'**{doujin.title(Format.Pretty)}: ** {doujin.url}')
        else:
            await ctx.send('Qua kênh NSFW mà xài')

    @commands.command()
    async def search (self, ctx, *, arg):
        try: 
            if ctx.channel.is_nsfw():
                TaggedDoujin = list(Utils.search_by_query(f'{arg}', sort = Sort.PopularWeek))
                t = 0
                for doujin in TaggedDoujin[0:5] :
                    t = t + 1
                    h_embed = discord.Embed(
                        title = f'{t}. {doujin.title(Format.Pretty)}',
                        description = doujin.url,
                        color = discord.Colour.teal()
                    )

                    h_embed.set_image(url = doujin.image_urls[0])
                    await ctx.send(embed = h_embed)
                    #await ctx.send(f'**{t}. {doujin.title(Format.Pretty)} [{doujin.id}]**\n{doujin.image_urls[0]}')
            else:
                await ctx.send('Qua kênh NSFW mà xài')
        except:
            await ctx.send('Không tìm thấy')

async def setup(bot):
    await bot.add_cog(nhentai(bot))

