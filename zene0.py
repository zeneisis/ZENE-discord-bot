import dmm
import json
from deep_translator import GoogleTranslator
from PIL import Image, ImageFilter
from io import BytesIO
import requests

api_id = 'KqU1nVdGnUKmFcmDHV1Q'
affiliate_id = 'otomachi2068-993'

api = dmm.API(api_id=api_id, affiliate_id=affiliate_id)
code = 'mdvr00247'

item_search = api.item_search(site="FANZA", keyword=code, output='json')

data = json.dumps(item_search)
collect_data = json.loads(data)

product_title = collect_data["result"]["items"][0]["title"]
affiliate_url = collect_data["result"]["items"][0]["affiliateURL"]
image_url = collect_data["result"]["items"][0]["imageURL"]["large"]
#prices =  collect_data["result"]["items"][0]["prices"]["deliveries"]["delivery"]
mega = collect_data["result"]["items"][0]["iteminfo"]["maker"][0]["name"]
#sampleURL = collect_data["result"]["items"][0]["sampleMovieURL"]["size_476_306"]
date = collect_data["result"]["items"][0]["date"]
try:
    price_lst = []
    for price in collect_data["result"]["items"][0]["prices"]["deliveries"]["delivery"][0:3]:
        price_lst.append(price["price"] + ' YPN')
except:
    price_lst = ['None']


#actress_name = collect_data["result"]["items"][0]["iteminfo"]["actress"][0]["name"]
try:
    lst = []
    for actress_name in collect_data["result"]["items"][0]["iteminfo"]["actress"]:
        lst.append(actress_name["name"] + f'({actress_name["ruby"]})')

except:
    lst = []

try: 
    sampleURL = collect_data["result"]["items"][0]["sampleMovieURL"]["size_476_306"]
    a = sampleURL
except:
    a = ''

translator = GoogleTranslator(source = 'ja', target = 'vi')

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
blurImage = img.filter(ImageFilter.BoxBlur(10))
blurImage.save('zene/data/image/simBlurImage.jpg')

print(translator.translate(product_title))
print(affiliate_url)
print(a)
print(image_url)
print(mega)
print(date)
print(lst)