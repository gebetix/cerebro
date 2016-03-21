from urllib.request import urlopen
import json


def get_images(lat, lon):
    distance = 500

    url_search = "https://api.instagram.com/v1/media/search?lat=%s&lng=%s&distance=%s&client_id=3d56e75ea0ae4b96aa459aa22530a519"
    url_oembed = "https://api.instagram.com/oembed?url=%s"

    data_search = json.loads(urlopen(url_search % (lat, lon, distance)).read().decode('utf8'))
    data_search = data_search["data"]

    for image in data_search:
        data_oembed = json.loads(urlopen(url_oembed % (image['link'])).read().decode('utf8'))
        yield data_oembed["html"]
