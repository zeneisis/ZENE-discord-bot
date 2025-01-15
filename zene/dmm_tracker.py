#!/usr/bin/python
# -*- coding: utf-8 -*-
import discord 
from discord.ext import commands
from deep_translator import GoogleTranslator
from PIL import Image, ImageFilter
from io import BytesIO
import requests
import dmm
import json

class dmm_tracker(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def code (self, ctx, *, arg:str):
        if '-' in arg:
            arg = arg.replace('-','00')
        
        get_api = json.loads(open('zene/TOKEN.json').read())

        api_id = get_api["DMM_API_ID"]
        affiliate_id = get_api["DMM_AFFILIATE_ID"]

        api = dmm.API(api_id=api_id, affiliate_id=affiliate_id)

        item_search = api.item_search(site="FANZA", service = 'digital', keyword=arg, output='json')

        data = json.dumps(item_search)
        collect_data = json.loads(data)

        product_title = collect_data["result"]["items"][0]["title"]
        affiliate_url = collect_data["result"]["items"][0]["affiliateURL"]
        volume = collect_data["result"]["items"][0]["volume"]
        image_url = collect_data["result"]["items"][0]["imageURL"]["large"]
        mega = collect_data["result"]["items"][0]["iteminfo"]["maker"][0]["name"]
        date = collect_data["result"]["items"][0]["date"]
        product_id = collect_data["result"]["items"][0]["product_id"]

        #embed_description = []
        actress_lst = []
        price_lst = []

        #try: 
            #sampleURL = collect_data["result"]["items"][0]["sampleMovieURL"]["size_476_306"]
            #embed_description = f'[Xem thử ngay]({sampleURL})'

        #except:
            #embed_description=[]



        try:

            for price in collect_data["result"]["items"][0]["prices"]["deliveries"]["delivery"][0:3]:
                price_lst.append(price["price"] + ' JPY')

        except:
            price_lst = ['None']

        try:
            for actress_name in collect_data["result"]["items"][0]["iteminfo"]["actress"]:
                actress_lst.append(f'**{actress_name["name"]}**' + f'【{actress_name["ruby"]}】')
        
        except:
            actress_lst = ['None']
            
        code_translator = GoogleTranslator(source = 'ja', target = 'vi')

        
        if ctx.channel.is_nsfw():
            embed_Image = image_url
            
            code_embed = discord.Embed(
                color = discord.Colour.blurple(),
                title = product_id.upper(),
                #url = affiliate_url,
                description = f'[**{code_translator.translate(product_title)}**]({affiliate_url})'
                #description = ''.join(embed_description)
            )

            #code_embed.set_thumbnail(url = image_url)
            code_embed.add_field(name = 'Ai Đồ', value = '\n'.join(actress_lst))
            code_embed.add_field(name = 'Giá', value = '\n'.join(price_lst))
            #code_embed.add_field(name = 'Sample', value = f'[Sample]({sampleURL})')
            code_embed.set_image(url = embed_Image)
            code_embed.set_footer(text = f'{mega} {date} {volume} phút')

            await ctx.send(embed=code_embed)
            
        else:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            blurImage = img.filter(ImageFilter.BoxBlur(10))
            blurImage.save('zene/data/image/simBlurImage.jpg')
            file = discord.File('zene/data/image/simBlurImage.jpg', filename="image.png")
            embed_Image = "attachment://image.png"
 
            code_embed = discord.Embed(
                color = discord.Colour.blurple(),
                title = product_id.upper(),
                #url = affiliate_url,
                description = f'[**{code_translator.translate(product_title)}**]({affiliate_url})'
                #description = ''.join(embed_description)
            )

            #code_embed.set_thumbnail(url = image_url)
            code_embed.add_field(name = 'Ai Đồ', value = '\n'.join(actress_lst))
            code_embed.add_field(name = 'Giá', value = '\n'.join(price_lst))
            #code_embed.add_field(name = 'Sample', value = f'[Sample]({sampleURL})')
            code_embed.set_image(url = embed_Image)
            code_embed.set_footer(text = f'{mega} {date} {volume} phút')

            await ctx.send(file=file, embed=code_embed)

        pass

    @commands.command()
    async def idol (self, ctx, *, arg:str):
        if '-' in arg:
            arg = arg.replace('-','00')
        
        get_api = json.loads(open('zene/TOKEN.json').read())

        api_id = get_api["DMM_API_ID"]
        affiliate_id = get_api["DMM_AFFILIATE_ID"]

        api = dmm.API(api_id=api_id, affiliate_id=affiliate_id)

        actress_search = api.actress_search(site="FANZA", keyword=arg, output='json')

        data = json.dumps(actress_search)
        collect_data = json.loads(data)

        actress_name = collect_data["result"]["actress"][0]["name"]
        actress_ruby = collect_data["result"]["actress"][0]["ruby"]
        actress_digitalURL = collect_data["result"]["actress"][0]["listURL"]["digital"]
        bust = collect_data["result"]["actress"][0]["bust"]
        waist = collect_data["result"]["actress"][0]["waist"]
        hip = collect_data["result"]["actress"][0]["hip"]
        height = collect_data["result"]["actress"][0]["height"]
        birthday = collect_data["result"]["actress"][0]["birthday"]
        hobby = collect_data["result"]["actress"][0]["hobby"]
        birthplace = collect_data["result"]["actress"][0]["prefectures"]
        imageURL = collect_data["result"]["actress"][0]["imageURL"]["large"]

        try: 
            bust_cup = collect_data["result"]["actress"][0]["cup"]
        except: 
            bust_cup = ''

        idol_translator = GoogleTranslator(source = 'ja', target = 'vi')
        
        idol_embed = discord.Embed(
            color = discord.Colour.brand_green(),
            title = actress_name + f'【{actress_ruby}】',
            url = actress_digitalURL,
            description='Đến từ ' + str(idol_translator.translate(str(birthplace)))
        )

        idol_embed.set_thumbnail(url=imageURL)
        idol_embed.add_field(name = 'Số đo 3 vòng', value = f'{bust} {waist} {hip} **{bust_cup}**')
        idol_embed.add_field(name = 'Chiều cao', value = height)
        idol_embed.add_field(name = 'Ngày sinh', value = birthday)
        idol_embed.add_field(name = 'Sở thích', value = idol_translator.translate(str(hobby)))
        await ctx.send(embed=idol_embed)
        pass
    

async def setup(bot):
    await bot.add_cog(dmm_tracker(bot))