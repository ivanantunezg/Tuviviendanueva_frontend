from flask import Blueprint, render_template, request,redirect, url_for,make_response
from repository.usuarios import usuarios
from http import cookies
import datetime,json


usuariosviews = Blueprint('usuariosviews', __name__)

# Definir variable estática para la URL
URL_API = "http://127.0.0.1:5001/api/usuarios"
repository = usuarios(URL_API)


@usuariosviews.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':
            email = request.form.get("email")
            contrasenia = request.form.get("contrasenia")
            
            response = repository.login(email, contrasenia)
            if response is not None: 
                if response['status'] == 'OK':
                    resp = make_response(redirect('/'))
                    resp.set_cookie('user-cookie', json.dumps(response),max_age=3600, expires=None, path='/')
                    return resp
                else:
                    return render_template('login.html', response=response)
            else:
                return render_template('login.html', error="error")
        else:
            return render_template('login.html')
    except Exception as ex:
        print("Error:", ex) 
        return render_template('login.html', error="Error interno del servidor.")

@usuariosviews.route('/registrarse', methods=['POST', 'GET'])
def registrarse():
    if request.method == 'POST':
        email = request.form.get("email")
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        numeroDocumento = request.form.get("numeroDocumento")
        telefono = request.form.get("telefono")
        tipoUsuario = request.form.get("tipoUsuario")
        contrasenia = request.form.get("contrasenia")
        response = repository.registrarse(email,nombre,apellido,numeroDocumento,telefono,tipoUsuario,contrasenia)
        if response != None: 
            return render_template('registrarse.html', response=response)
        else:
            return render_template('registrarse.html', error="error")
    else:
        return render_template('registrarse.html')
    
@usuariosviews.route('/perfil', methods=['POST', 'GET'])
def perfilusuario():
    user_data_dict = usuarios.get_user_data()
    if request.method == 'POST':
        return render_template('perfil.html', user_data = user_data_dict)
    else:
        idusuario = usuarios.get_user_data()['_id']
        datos_perfil = repository.getDatosPerfil(idusuario)
        if datos_perfil is not None:
            return render_template('perfil.html',datos_perfil=datos_perfil, user_data = user_data_dict)
        else:
            return render_template('perfil.html', user_data = user_data_dict)