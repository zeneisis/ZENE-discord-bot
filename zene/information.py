import discord 
from discord.ext import commands
from discord.ext.commands.bot import Bot
import random

class information(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx: commands.Context, member: discord.Member):
        try: 
            if member.id == 262844868919951360:
                sex0 = 'Nam'
                economic0 = 'Cần tiền ủng hộ'
                await ctx.send(f'```Đồng Chí: {member.name}\nGiới Tính: {sex0}\nTrạng Thái: {economic0}```')
            elif member.id == 797507405587677185:
                await ctx.send('Yamete kudasai!!!! Oniiiii-chan')
            elif member.id == 323427262194253825 and 347588077272694785:
                sex0 = 'Không thể xác định'
                economic0 = 'Daiza'
                await ctx.send(f'```Đồng Chí: {member.name}\nGiới Tính: {sex0}\nTrạng Thái: {economic0}```')
            else:
                sex = random.choice(['Mail','Free mail','Tuesday','Không thể xác định'])
                economic = random.choice(['Daiza','Giàu','Nghèo','Cần tiền ủng hộ'])
                await ctx.send(f'```Đồng Chí: {member.name}\nGiới Tính: {sex}\nTrạng Thái: {economic}```')
        except:
            await ctx.send('Muốn xem info của ai thì tag tên vào')

async def setup(bot):
    await bot.add_cog(information(bot))