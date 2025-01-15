from deep_translator import GoogleTranslator
from discord.ext import commands

class translate(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def trans(self, ctx, *, arg):
        try:
            text = str(arg)
            code_translator = GoogleTranslator(source = 'auto', target = 'vi')
            translateText = code_translator.translate(text)
            await ctx.reply(f'{translateText}')
        except:
            await ctx.reply('http://translate.google.com/')

async def setup(bot):
    await bot.add_cog(translate(bot))