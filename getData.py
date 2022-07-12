
import requests
import json

response = requests.get(url="https://api.publicapis.org/entries")

if response.status_code == 200:
    try:
        # dict_data = json.loads(response.text)
        dict_data = response.json()
    except:
        print("Something wring")
    else:
        print("Total number od records are : ", dict_data["count"])
        list_of_objects = dict_data["entries"]
        for obj in list_of_objects[:10]:
            print(obj["API"])
            print(obj["Description"])
            print(obj["Link"].replace('/', ''))
            print()
        print()



