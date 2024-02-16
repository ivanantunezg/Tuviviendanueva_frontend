import json
import requests

class viviendas:
    def __init__(self, url):
        self.url = url

    def getViviendas(self, params):
        headers = {'Content-Type': 'application/json'}    
        json_data = json.dumps(params)    
        response = requests.get(self.url, data=json_data, headers=headers)

          
        
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
        
    def getViviendaByUserID(self, id):
        response = requests.get(self.url + "/usuarios/" + id)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
        
    def createViviendaByUserID(self, idUsuario,nombre,descripcion,tipo,precio, area,habitaciones,banios, estacionamientos, direccion, ciudad):
        URL_API = self.url + "/usuarios/" + str(idUsuario)
        headers = {'Content-Type': 'application/json'}
        data = {
            'nombre': nombre,
            'descripcion': descripcion,
            'tipo': tipo,
            'precio': precio,
            'caracteristicas': {
                'area': area,
                'habitaciones': habitaciones,
                'banios': banios,
                'estacionamientos': estacionamientos,
            },
            'ubicacion':{
                'direccion': direccion,
                'ciudad': ciudad,
            }
        }
        json_data = json.dumps(data)
        response = requests.post(URL_API, data=json_data, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

