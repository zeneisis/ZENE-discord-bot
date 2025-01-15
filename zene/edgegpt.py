import asyncio
import discord
import json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from discord.ext import commands


class EdgeGPT(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def gpt(self, ctx: commands.Context, *, arg: str):
        cookies = json.loads(open('zene/bing_cookies_zene.json', encoding = 'utf-8').read())
        bot = Chatbot(cookies = cookies)
        remove_character =  list(range(1,50))

        response = await bot.ask(prompt = arg, conversation_style = ConversationStyle.balanced, simplify_response = True)
        data_dump = json.dumps(response, indent = 2)
        get_data = json.loads(data_dump)
        responsed = str(get_data['text'])

        for i in remove_character:
            if str(i) in responsed:
                responsed = responsed.replace(f'[^{i}^]','')
            elif 'Bing' in responsed:
                responsed = responsed.replace('Bing','Zene')
            
            if ctx.author.id == 262844868919951360:
                responsed = responsed.replace('bạn','chủ nhân').replace('Bạn','Chủ nhân').replace('tôi','em').replace('Tôi','Em').replace('của mình','của chủ nhân').replace('mình','em')
            elif ctx.author.id != 262844868919951360:
                responsed = responsed.replace('bạn','người anh em').replace('Bạn','Người anh em')

        await bot.close()
        await ctx.reply(f'{responsed}')


async def setup(bot):
    await bot.add_cog(EdgeGPT(bot))