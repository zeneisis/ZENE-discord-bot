import json
import requests
from discord.ext import commands

class han2viet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def han(self,ctx, *, arg):
        payload = f"mode=trans&lang=3&input={arg}" # PUT WHAT YOU WANT

        url = "https://hvdic.thivien.net/transcript-query.json.php"
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}

        response = requests.request("POST", url, headers=headers, data=payload.encode())
        result = json.loads(response.text)["result"]

        list = []
        for a in result:
            if a["o"] == '':
                pass
            else:
                list.append(' '.join(a["o"]))

        while('' in list):
            list.remove('')

        response = '\n'.join(list)
        await ctx.reply(f"{response}\nhttps://hvdic.thivien.net/whv/{arg}")




async def setup(bot):
    await bot.add_cog(han2viet(bot))