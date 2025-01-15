from discord.ext import commands 
import google.generativeai as genai
import json

class GeminiAI(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ai(self, ctx: commands.Context, *, arg: str):
        get_api = json.loads(open('zene/TOKEN.json').read())
        api_id = get_api["GOOGLE_GEMINI_API"]
        genai.configure(api_key=api_id)
        model = genai.GenerativeModel('gemini-pro')
        resonse = model.generate_content(arg)
        await ctx.reply(resonse.text)

async def setup(bot):
    await bot.add_cog(GeminiAI(bot))