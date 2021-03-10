from flask import Flask, render_template, request, jsonify
from data_articulos import data
from flask_cors import CORS #pip install -U flask-cors

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Bienvenidos a esta REST API Flask'

@app.route('/all')
def all():
    return jsonify(data)

@app.route('/all/<string:articulo>')
def obtener(articulo):
    lista_articulos = []
    for elemento in data:
        if (elemento['art'] == articulo):
            lista_articulos.append(elemento)
    if (len(lista_articulos) > 0):
        return jsonify(lista_articulos)
    
    return jsonify({'mensaje': 'No se ha encontrado infomacion'})

@app.route('/send', methods = ['POST'])
def send():
    if request.method == 'POST':
        nuevo = {
            'art': request.json['art'],
            'precio': request.json['precio'],
            'color': request.json['color']
        }
        print(nuevo)
        data.append(nuevo)
        return jsonify(data)
    return jsonify({'Mensaje': 'Ocurrio un error'})

if __name__ == '__main__':
    app.run(debug = True, port = 5000)