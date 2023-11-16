# creating 3rd party app which communicate with api to get data

import requests

URL = "http://127.0.0.1:8000/stuinfo/"   ## get all students
# URL = "http://127.0.0.1:8000/stuinfo/2"  ## get student with rollno

r = requests.get(url = URL)

data  = r.json()

print(data)