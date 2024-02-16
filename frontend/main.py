import json
from flask import Flask, jsonify, render_template, request, Blueprint
from repository.viviendas import viviendas
from repository.usuarios import usuarios
from views.viviendas import viviendasviews
from views.usuarios import usuariosviews

app = Flask(__name__, static_folder='templates')

# Rutas de la app
@app.route('/')
def index():
    user_data_dict = usuarios.get_user_data()
    return render_template('home.html', user_data=user_data_dict)
    

@app.route('/Home')
def home():
    user_data_dict = usuarios.get_user_data()
    return render_template('home.html', user_data=user_data_dict)

app.register_blueprint(usuariosviews, url_prefix='/')

app.register_blueprint(viviendasviews, url_prefix='/')



if __name__ == '__main__':
    app.run(debug=True, port=4010)