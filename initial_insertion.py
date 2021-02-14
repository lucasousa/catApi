import requests
import json


data = [
    {
        "breed": "Abyssian",
        "location_of_origin": "Asia",
        "coat_length": "Short",
        "body_type": "Semi-foreign",
        "pattern": "Ticked tabby"
    },
    {
        "breed": "Persa",
        "location_of_origin": "Ira",
        "coat_length":"medium",
        "body_type":"rounded",
        "pattern":"White Cat",
    },
    {
        "breed": "Scottish Fold",
        "location_of_origin": "Escocia",
        "coat_length":"medium",
        "body_type":"folded ears",
        "pattern":"Black cat"
    }
]


requests.post("http://127.0.0.1:8000/cats/", data=json.dumps(data[0]))
requests.post("http://127.0.0.1:8000/cats/", data=json.dumps(data[1]))
requests.post("http://127.0.0.1:8000/cats/", data=json.dumps(data[2]))