#!python3
# -*- coding: utf-8 -*-
import requests
from collections import Iterator, Iterable
__author__ = 'wangjj'
__mtime__ = '2016121920:07'
__doc__='''
可迭代对象
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


def get_weather(city):
    global headers
    r = requests.get(
        'http://wthrcdn.etouch.cn/weather_mini?city=' +
        city,
        headers=headers)
    data = r.json()['data']['forecast'][0]
    return '{},{},{}'.format(city, data['low'], data['high'])

# ['北京', '长春', '上海']

# print(get_weather('北京'))
# print(get_weather('上海'))


class WeatherIterator(Iterator):

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        global headers
        r = requests.get(
            'http://wthrcdn.etouch.cn/weather_mini?city=' +
            city,
            headers=headers)
        data = r.json()['data']['forecast'][0]
        return '{},{},{}'.format(city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


class WeatherIterable(Iterable):

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

weather=WeatherIterable(['北京', '长春', '上海'])
for i in weather:
    print(i)