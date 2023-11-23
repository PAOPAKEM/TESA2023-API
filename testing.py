import requests
import json

def get_mockup_data(id):
    url = 'http://192.168.1.3:7078/'+ str(id)
    #url = 'https://jsonplaceholder.typicode.com/albums'#/'+str(id)
    mockup = requests.get(url)
    if mockup:
        for i in json.loads(mockup.text):
            print(i)
        return json.loads(mockup.text)[0]
            

if __name__ == "__main__":
    print(get_mockup_data(555)["w_date"])