from io import BytesIO
import requests
from PIL import Image
from coords import coords
from random import shuffle


def new_place(place):
    toponym_to_find = place
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        pass
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    a = [float(i) for i in toponym['boundedBy']['Envelope']['lowerCorner'].split()]
    b = [float(i) for i in toponym['boundedBy']['Envelope']['upperCorner'].split()]
    delta = [str(max(b[0], a[0]) - min(b[0], a[0])), str(max(b[1], a[1]) - min(b[1], a[1]))]
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        'z': coords(delta[0], delta[1]),
        "spn": ",".join([delta[0], delta[1]]),
        "l": "sat",
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    mg = Image.open(BytesIO(response.content))
    mg.show()


spisok = [['Крассная площадь', 'Москва'], ['Египет Пирамида Хеопса', 'Египет'],
          ['Санкт-Петербург Дворцовая площадь', 'Санкт-Петербург'], ['Италия Рим Челио', 'Рим'],
          ['Россия Республика Татарстан Казань проезд Шейнкмана', 'Казань']]
del spisok[:-1]
shuffle(spisok)
for i in spisok:
    new_place(i[0])
    print("Какой это город?")
    answer = input()
    while answer != i[1]:
        print('Неверно, попробуйте ещё раз.')
        answer = input()