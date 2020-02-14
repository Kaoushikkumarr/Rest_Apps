import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


# def get_resource(id=None):
#     data = {}
#     if id is not None:
#         data = {
#             'id': id
#         }
#     req = requests.get(BASE_URL + ENDPOINT, data = json.dumps(data))
#     print(req.status_code)
#     print(req.json())
#
# get_resource()

# def get_resource(id):
#     req = requests.get(BASE_URL + ENDPOINT + id + '/')
#     print(req.status_code)
#     ''' 1XX--- Informational
#         2XX--- Successful
#         3XX--- Redirectional
#         4XX--- Client Error (403 csrf token error)
#         5XX--- Server Error '''
#     print(req.json())
#



# def get_all():
#     req = requests.get(BASE_URL + ENDPOINT)
#     print(req.status_code)
#     print(req.json())
# # get_resource('300')
#
#
# def create_resource():
#     new_emp = {
#         'eno': 5,
#         'ename': 'Shiva',
#         'esal': '7000',
#         'eaddr': 'Chennai',
#     }
#     req = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
#     print(req.status_code)
#     print(req.json())
# create_resource()
#
# def update_resource(id):
#     new_emp = {
#         'id':id,
#         'esal': '30000',
#         'eaddr': 'Jaipur',
#     }
#     req = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
#     print(req.status_code)
#     print(req.json())
# update_resource(2)

#
def delete_resource(id):
    data = {
        'id':id,
    }
    req = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(req.status_code)
    print(req.json())
delete_resource(20)
