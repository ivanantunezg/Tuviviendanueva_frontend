from flask import Flask, render_template, request
from viviendas import viviendas

app = Flask(__name__, static_folder='templates')

# Definir variable estática para la URL
URL_API = "https://tuviviendanuevabackend-0cf776933a1f.herokuapp.com/api/viviendas"

# Rutas de la app
@app.route('/AltaViviendas')
def index():
    return render_template('index.html')

@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/Viviendas')
def pageViviendas():
    viviendasAPI = viviendas(URL_API)
    data = viviendasAPI.getViviendas()

    if data is not None:
        return render_template('viviendas.html', viviendas=data)
    else:
        error_message = 'Error al consumir la API'
        return render_template('viviendas.html', error=error_message)

@app.route('/Vivienda')
def vivienda():
    id = request.args.get('id')
    viviendasAPI = viviendas(URL_API)
    data = viviendasAPI.getViviendaByID(id)

    return render_template('vivienda.html', vivienda=data)

if __name__ == '__main__':
    app.run(debug=True, port=4010)