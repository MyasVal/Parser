import requests
from bs4 import BeautifulSoup  # для парсинга старниц
from model import Houses
from requests import get
import csv
import time
import random


def parser(url:str):
    list_house = []
    create_csv()
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, 'lxml')
    houses = soup.find_all('div', class_='sEnLiDetails')
    for house in houses:
        name = house.find('div', class_='sEnLiTitle').text.strip()
        price = house.find('div', class_='sEnLiPrice').text.strip()
        address = house.find('div', class_='sEnLiCity').text.strip()
        date = house.find('div', class_='sEnLiDate today').text.strip()
        list_house.append(Houses(name=name, price=price, address=address, date=date))

        write_csv(list_house)


def create_csv():
    with open(f'galvsnab.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'name',
            'price',
            'address',
            'date'
        ])


def write_csv(houses: list[Houses]):
    with open(f'galvsnab.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for house in houses:
            writer.writerow([
                houses.name,
                houses.price,
                houses.address,
                houses.date
            ])

if __name__ == '__main__':
    parser(url='https://kzn.bezposrednikov.ru/')