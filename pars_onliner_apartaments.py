import requests
import json

url = "https://r.onliner.by/sdapi/pk.api/search/apartments?number_of_rooms%5B%5D=1&price%5Bmin%5D=4146&price%5Bmax%5D=40000&currency=usd&bounds%5Blb%5D%5Blat%5D=53.76900752082657&bounds%5Blb%5D%5Blong%5D=27.39028930664063&bounds%5Brt%5D%5Blat%5D=54.026730105182416&bounds%5Brt%5D%5Blong%5D=27.73361206054688&page=1&v=0.9106326431195029"

r = requests.get(url,headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}).json()
page_count = r['page']['last']
apartments = r['apartments']
count = 1
result = []
for j in range(1,page_count+1):
    url_page = f'https://r.onliner.by/sdapi/pk.api/search/apartments?number_of_rooms%5B%5D=1&price%5Bmin%5D=4146&price%5Bmax%5D=40000&currency=usd&bounds%5Blb%5D%5Blat%5D=53.76900752082657&bounds%5Blb%5D%5Blong%5D=27.39028930664063&bounds%5Brt%5D%5Blat%5D=54.026730105182416&bounds%5Brt%5D%5Blong%5D=27.73361206054688&page={j}&v=0.9106326431195029'
    r_page = requests.get(url_page,headers={
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }).json()
    for i in apartments:
        address = i["location"]["address"]
        price_usd = i["price"]["amount"]
        price_byn = i["price"]["converted"]["BYN"]["amount"]
        area = i["area"]["total"]
        link = i["url"]
        result.append({
            "Номер" : count,
            "Адрес" : address,
            "Cтоимость в USD" : price_usd,
            "Стоимость в BYN" : price_byn,
            "Площадь м2" : area,
            "Cсылка" : link,
            })
        count += 1

with open('result.json','a') as file:
    json.dump(result, file, indent = 2, ensure_ascii = False)
