from flask import request
import requests, json

class usuarios:
    def __init__(self, url):
        self.url = url

    def login(self, email, contrasenia):
        try:

            URL_API = self.url + "/login"
            headers = {'Content-Type': 'application/json'}
            data = {
                'email': email,
                'contrasenia': contrasenia
            }
            json_data = json.dumps(data)
            response = requests.post(URL_API, data=json_data, headers=headers)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return None
        except Exception as ex:
            return {'status': 'Error al iniciar sesión'}
        
    def registrarse(self,email,nombre,apellido,numeroDocumento,telefono,tipoUsuario,contrasenia):
        URL_API = self.url + "/registrar"
        headers = {'Content-Type': 'application/json'}
        data = {
            'nombre': nombre,
            'apellido': apellido,
            'numeroDocumento': numeroDocumento,
            'telefono': telefono,
            'tipoUsuario' : tipoUsuario,
            'email': email,
            'contrasenia': contrasenia
        }
        json_data = json.dumps(data)
        response = requests.post(URL_API, data=json_data, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
        
    def get_user_data():
        user_data = request.cookies.get('user-cookie')
        user_data_dict = None
        if user_data is not None:
            user_data_dict = json.loads(user_data)
        return user_data_dict
    

    def getDatosPerfil(self, id):
        response = requests.get(self.url + "/" + id)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None


    