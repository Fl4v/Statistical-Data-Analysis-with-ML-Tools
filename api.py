import requests
from os import environ
from PIL import Image
from urllib.request import urlretrieve


class NasaApod:
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': environ['NASA_API_KEY']}

    def __init__(self):

        json_data = requests.get(self.nasa_url, params=self.params).json()

        global image_name
        image_name = str(json_data['title'] + '.jpg')

        urlretrieve(json_data['url'], 'data/' + image_name)

    def open_daily_image(self):
        img = Image.open('data/' + image_name)
        img.show()


class NasaEarth:
    pass
