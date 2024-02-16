from flask import Blueprint, render_template, request
from repository.viviendas import viviendas
from repository.usuarios import usuarios

viviendasviews = Blueprint('viviendasviews', __name__)

# Definir variable estática para la URL
URL_API = "http://127.0.0.1:5001/api/viviendas"

@viviendasviews.route('/Viviendas')
def pageViviendas():
    viviendasAPI = viviendas(URL_API)

    user_data_dict = usuarios.get_user_data()

    if request.args:
        params = {
            "precio": {
                "$gte": int(request.args.get('precioMin', '')),
                "$lte": int(request.args.get('precioMax', ''))
            },
            "ubicacion.ciudad": {"$regex":  request.args.get('ciudad', ''), "$options": "i" },
            "caracteristicas.habitaciones": {
                '$gte': request.args.get('cantidadRecamaras', '')
            },
            "caracteristicas.banios": {
                '$gte': request.args.get('cantidadBanios', '')
            },
            "caracteristicas.estacionamientos": {
                '$gte': request.args.get('cantidadEstacionamientos', '')
            }
        }
        data = viviendasAPI.getViviendas(params)
    else:
        params = {}
        data = viviendasAPI.getViviendas(params)

    

    if data is not None:
        return render_template('viviendas.html', viviendas=data, user_data = user_data_dict)
    else:
        error_message = 'Error al consumir la API'
        return render_template('viviendas.html', error=error_message, user_data = user_data_dict)

@viviendasviews.route('/Vivienda')
def vivienda():
    user_data_dict = usuarios.get_user_data()
    id = request.args.get('id')
    viviendasAPI = viviendas(URL_API)
    data = viviendasAPI.getViviendaByID(id)

    return render_template('vivienda.html', vivienda=data, user_data = user_data_dict)


@viviendasviews.route('/MisViviendas')
def misViviendas():
    user_data_dict = usuarios.get_user_data()
    id = user_data_dict['_id']
    viviendasAPI = viviendas(URL_API)
    data =viviendasAPI.getViviendaByUserID(id)
    return render_template("misviviendas.html", viviendas=data, user_data = user_data_dict)

@viviendasviews.route('/AltaVivienda', methods=['GET', 'POST'])
def altaVivienda():
    user_data_dict = usuarios.get_user_data()
    id = user_data_dict['_id']
    if request.method == 'POST':
        viviendasAPI = viviendas(URL_API)
        
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        tipo = request.form.get('tipo')
        precio = request.form.get('precio')
        area = request.form.get('area')
        habitaciones = request.form.get('habitaciones')
        banios = request.form.get('banios')
        estacionamientos = request.form.get('estacionamientos')
        direccion = request.form.get('direccion')
        ciudad = request.form.get('ciudad')

        data =viviendasAPI.createViviendaByUserID(
            id, nombre, descripcion, tipo, precio, area, habitaciones, banios,
            estacionamientos, direccion, ciudad
        )
        return render_template("altavivienda.html", viviendas=data, user_data = user_data_dict )
    else:
        return render_template("altavivienda.html", user_data = user_data_dict)
    