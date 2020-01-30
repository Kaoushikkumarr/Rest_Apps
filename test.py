import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resource(id):
    req = requests.get(BASE_URL + ENDPOINT + id + '/')
    print(req.status_code)
    ''' 1XX--- Informational
        2XX--- Successful
        3XX--- Redirectional
        4XX--- Clent Error (403 csrf token error)
        5XX--- Server Error '''
    print(req.json())
id = input("Enter some ID:")
get_resource(id)
