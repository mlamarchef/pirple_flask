import re
from flask import Flask, render_template  # 1 Import flask
 
app = Flask(__name__) # Inicializacion

@app.route('/' , methods = ['GET'] ) # Se define la ruta inicial
def home():  # Funcion para probar la ruta
    return render_template('index.html')

@app.route('/misc', methods=['GET'])
def misc():
    return render_template('misc.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000) 


