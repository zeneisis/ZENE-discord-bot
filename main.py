
#ssh omazio2068@raspberrypi.local -f "cd ~/Downloads/zene_bot; python /home/omazio2068/Downloads/zene_bot/main.py"
#ssh omazio2068@raspberrypi.local -f "cd ~/Downloads/zene_bot; pkill -f /home/omazio2068/Downloads/zene_bot/main.py"

import discord 
import asyncio
import time
import json 
import os
import sys
from colorama import Fore
from colorama import Style
from tqdm import tqdm
from discord.ext import commands
#from discord.ext.commands.bot import BotBase

data = json.loads(open('zene/TOKEN.json').read())
TOKEN = data['DISCORD_TOKEN']
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=['z/','Z/','h/','H/'], intents=intents)

async def load_extensions():
    with open("extensions.txt") as file:
        extensions = [e for e in file.read().splitlines() if e]
    for extension in extensions:
        try:
            await bot.load_extension(extension)
            print("Loading",format(extension),Fore.GREEN + '...Done' + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Failed loading {}: {}".format(extension, e) + Style.RESET_ALL)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Black Myth: Wukong'))

async def main():
    await load_extensions()
    print(Fore.CYAN + 'Booting up Zene...' + Style.RESET_ALL)
    for xx in tqdm(range(100)):
        time.sleep(0.01)
    print(Fore.GREEN + '---------DONE---------' + Style.RESET_ALL)
    await bot.start(TOKEN)

def restart_bot():
    os.execv(sys.executable,['python'] + sys.argv)

@bot.command(name='restart')
async def restart(ctx:commands.Context):
    if ctx.author.id == 262844868919951360:
        await ctx.send('🫡 わかりました、ご主人様。')
        restart_bot()
    else:
        await ctx.send('Unauthorized!!!')
    

asyncio.run(main())