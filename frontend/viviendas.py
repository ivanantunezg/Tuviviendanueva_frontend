import requests

class viviendas:
    def __init__(self, url):
        self.url = url

    def getViviendas(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
        
    def getViviendaByID(self, id):
        response = requests.get(self.url + "/" + id)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
