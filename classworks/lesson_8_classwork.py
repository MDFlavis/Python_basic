import requests
import asyncio
import random


class SomeError(Exception):
    def __init__(self, text=None):
        self.text = text

# def some_f(number):
#     for num in range(number):
#         if num == 15:
#             raise SomeError('Some text is error')
#
# try:
#     some_f(12)
# except SomeError as e:
#     print('Error', e)

class Product:
    id = ''
    name = ''

    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Parser:
    __headers ={
    }
    __params = {
        'records_per_page': 50,
        'categories': '',
    }
    def __init__(self, start_url:str):
        self.__start_url = start_url
        self.products = []

    def parse(self):
        url = self.__start_url
        while url:
            response = requests.get(url, params=self.__params, headers=self.__headers)
            data = response.json()
            url = data['next']
            self.products.extend(Product(itm) for itm in data)['results']

async  def one(n):
    for num in range(n):
        await asyncio.sleep(random.randint(1, 15))
        print(num, 'one', n)
        await asyncio.sleep(random.randint(1, 15))

if __name__ == '__main__':
    # tasks = [one(n) for n in range(5)]
    # parser = Parser ('url')
    # parser.parse()
    tasks = asyncio.wait([one(n) for n in range(5)])
    asyncio.run()
    print(1)