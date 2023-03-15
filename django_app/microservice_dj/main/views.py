import sqlite3
import time
from datetime import datetime, date
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json

from .form import AuthForm



def get_start_page(request):
    context = {
        "form" : AuthForm
    }
    return render(request, 'start_page.html', context)


def get_data(request):
    url = ("https://select.by/kursy-valyut/natsbank-rb/dollar")
    res = requests.get(url)
    print(res)
    print(res.headers.get('content-type'))
    # print(res.text)
    data = BeautifulSoup(res.text, 'html.parser')
    parse_data = data.select('span')[4]
    parse_info = parse_data.get_text()
    print(parse_info)
    print(type(parse_info))
    date_today = date.today()
    print(f'today is {date_today}')
    connect_db = sqlite3.connect('db.sqlite3')
    cursor = connect_db.cursor()
    query = '''INSERT INTO storage VALUES(?, ?);'''
    cursor.execute(query, (date_today, parse_info) )
    # cursor.execute(f"INSERT INTO storage VALUES ('{date_today}', '{parse_info}');")
    connect_db.commit()
    connect_db.close()
    context = {
        "parse_info": parse_info,
        'date_today': date_today,
    }
    return render(request, "main_page.html", context)


def get_auth(request):
    return render(request, 'auth.html')



def get_error(request):
    return render(request, 'error_page.html')





