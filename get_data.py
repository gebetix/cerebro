from urllib.request import urlopen
import json


def get_images(lat, lon):
    distance = 200

    url = "https://api.instagram.com/v1/media/search?lat=%s&lng=%s&distance=%s&client_id=3d56e75ea0ae4b96aa459aa22530a519"

    data = json.loads(urlopen(url % (lat, lon, distance)).read().decode('utf8'))
    data = data["data"]

    for image in data:
        yield image['images']['standard_resolution']['url']

