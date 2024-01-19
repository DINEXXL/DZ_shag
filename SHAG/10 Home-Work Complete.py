import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import datetime

conn = sqlite3.connect("weather.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE weather
             (date_time text, temperature text)"""
)


def get_temperature():
    response = requests.get(
        "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D1%8C"
    )
    soup = BeautifulSoup(response.text, "html.parser")

    temperature = soup.find("div", {"class": "temperature"}).text

    return temperature


def update_weather():
    while True:
        temperature = get_temperature()
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        c.execute("INSERT INTO weather VALUES (?, ?)", (date_time, temperature))
        conn.commit()

        time.sleep(1800)


update_weather()
