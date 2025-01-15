import json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from discord.ext import commands

class testGPT(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def testgpt(self, ctx: commands.Context, *, arg: str):
        cookies =json.loads(open('zene/bing_cookies_zene.json', encoding='utf-8').read())
        bot = Chatbot(cookies=cookies)

        response = await bot.ask(prompt = arg, conversation_style=ConversationStyle.balanced, simplify_response=True)
        data_dump = json.dumps(response, indent=2)
        get_data = json.loads(data_dump)
        responsed = str(get_data['text'])

        await bot.close()
        await ctx.reply(f'{responsed}')

async def setup(bot):
    await bot.add_cog(testGPT(bot))