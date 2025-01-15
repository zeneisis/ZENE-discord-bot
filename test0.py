import dmm
import json
from deep_translator import GoogleTranslator

api_id = 'KqU1nVdGnUKmFcmDHV1Q'
affiliate_id = 'otomachi2068-993'

api = dmm.API(api_id=api_id, affiliate_id=affiliate_id)
code = 'はしもとありな'

item_search = api.actress_search(site="FANZA", keyword=code, output='json')

data = json.dumps(item_search)
collect_data = json.loads(data)
translator = GoogleTranslator(source = 'ja', target = 'vi')



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

print(translator.translate(str(hobby)))