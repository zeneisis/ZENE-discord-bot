from discord.ext import commands
import wikipedia

def wiki_sum(arg):
    wikipedia.set_lang('vi')
    definition = wikipedia.summary(arg, sentences=3)
    return definition

class wiki(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx, *, arg):
        try:
            await ctx.send(wiki_sum(arg))
        except:
            await ctx.send('T tìm rồi nhưng ko có. Dùng từ khóa khác đi')

async def setup(bot):
    await bot.add_cog(wiki(bot))