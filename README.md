Rest_Apps

# Multiples startproject.
# Without Rest APIs.

Serialization:
--------------
Python object into json object.

1. By using python inbuilt module json.
      json.dumps(data)

2. By using django serialize() function
      from django.core.serializers import serialize
          json_data = serialize('json', [emp,], fields=('eno', 'ename', 'eaddr'))
