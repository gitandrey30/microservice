from bs4 import BeautifulSoup
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/')
async def render_data():
    res = requests.get('https://www.gismeteo.by/weather-minsk-4248/now/', headers=headers)
    data = BeautifulSoup(res.text, 'html.parser')
    parse_data = data.select('span')[0]
    parse_data1 = data.select('span')[4]
    parse_info = parse_data.get_text()
    parse_info1 = parse_data1.get_text()
    data_to_render = ('now ' + parse_info + ' °C')
    data_to_render1 = ('feels like ' + parse_info1 + ' °C')
    return {data_to_render, data_to_render1}




headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}

