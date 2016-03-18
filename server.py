from bottle import request, route, run, template, view
from get_data import get_images


@route('/images')
@view('images')
def images():
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    return {'images': get_images(lat, lon)}

run(host='localhost', port=80, debug=True)
