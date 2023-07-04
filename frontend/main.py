from flask import Flask, render_template, request
from viviendas import viviendas
app = Flask(__name__,static_folder='templates')

#Rutas de la app
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/Viviendas')
def pageViviendas():
    url = "http://127.0.0.1:4000/api/viviendas"
    viviendasAPI = viviendas(url)
    data = viviendasAPI.getViviendas()

    if data is not None:
        return render_template('viviendas.html', viviendas=data)
    else:
        error_message = 'Error al consumir la API'
        return render_template('viviendas.html', error=error_message)

@app.route('/Vivienda')
def vivienda():
    id = request.args.get('id')
    url = "http://127.0.0.1:4000/api/viviendas"
    viviendasAPI = viviendas(url)
    data = viviendasAPI.getViviendaByID(id)

    return render_template('vivienda.html', vivienda=data)


if __name__ == '__main__':
    app.run(debug=True,port=4010)
