import json
from flask import Flask, render_template, request, redirect, flash, jsonify
from markupsafe import escape
import math
import controladores.controlador_discos as controlador_discos
import controladores.controlador_usuarios as controlador_usuarios
from flask import url_for
from flask import make_response
import hashlib
import random

app = Flask(__name__)

@app.route("/pruebajson")
def pruebajson():
    #pruebadict = dict()
    #pruebadict['S1'] = 'Hugo'; pruebadict['S2'] = 'Paco'; pruebadict['S3'] = 'Luis';
    pruebadict = "{'S1': 'Hugo', 'S2': 'Paco', 'S3': 'Luis'}"
    return pruebadict;

@app.route("/pruebajsonreal")
def pruebajsonreal():
    #pruebadict = dict()
    #pruebadict['S1'] = 'Hugo'; pruebadict['S2'] = 'Paco'; pruebadict['S3'] = 'Luis';    
    #pruebadict = ""
    return jsonify({'S1': 'Hugo', 'S2': 'Paco', 'S3': 'Luis'});
    
@app.route("/agregar_disco")
def formulario_agregar_disco():
    token = request.cookies.get('token')
    if token == "abcdef":
        return render_template("agregar_disco.html", esSesionIniciada=True)
    return render_template("login.html")

@app.route("/api_guardar_disco")
def api_agregar_disco():
    token = request.cookies.get('token')
    codigo = request.json["codigo"]
    nombre = request.json["nombre"]
    artista = request.json["artista"]
    precio = request.json["precio"]
    genero = request.json["genero"]
    


@app.route("/guardar_disco", methods=["POST"])
def guardar_disco():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    artista = request.form["artista"]
    precio = request.form["precio"]
    genero = request.form["genero"]
    controlador_discos.insertar_disco(codigo, nombre, artista, precio, genero)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/discos")


@app.route("/discos")
def discos():
    username = request.cookies.get('username')
    token = request.cookies.get('token')
    usuario = controlador_usuarios.obtener_usuario_por_username(username)
    if token == usuario[3]:
        discos = controlador_discos.obtener_discos()
        return render_template("discos.html", discos=discos, esSesionIniciada=True)
    return render_template("login.html")

@app.route("/eliminar_disco", methods=["POST"])
def eliminar_disco():
    controlador_discos.eliminar_disco(request.form["id"])
    return redirect("/discos")


@app.route("/formulario_editar_disco/<int:id>")
def editar_disco(id):
    # Obtener el disco por ID
    disco = controlador_discos.obtener_disco_por_id(id)
    return render_template("editar_disco.html", disco=disco)


@app.route("/actualizar_disco", methods=["POST"])
def actualizar_disco():
    id = request.form["id"]
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    artista = request.form["artista"]
    precio = request.form["precio"]
    genero = request.form["genero"]
    controlador_discos.actualizar_disco(codigo, nombre, artista, precio, genero, id)
    return redirect("/discos")

# @app.route("/sumafactoriales/<nro1>/<nro2>")
# def hello(nro1, nro2):
#     # Suma de los factoriales resultantes de ambos números
#     return f"Suma de factoriales es: {math.factorial(int(escape(nro1))) + math.factorial(int(escape(nro2)))}!"

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    resp = make_response(redirect("/login"))
    resp.set_cookie('token', '', expires=0)
    return resp

@app.route("/procesar_login", methods=["POST"])
def procesar_login():
    username = request.form["username"]
    password = request.form["password"]
    usuario = controlador_usuarios.obtener_usuario_por_username(username)
    
    # Encriptar password ingresado por usuario
    h = hashlib.new('sha256')
    h.update(bytes(password,encoding='utf-8'))
    encpassword = h.hexdigest()
    if encpassword == usuario[2]:
        # Obteniendo token
        t = hashlib.new('sha256')
        entale = random.randint(1,1024)
        strEntale = str(entale)
        t.update(bytes(strEntale,encoding='utf-8'))
        token = t.hexdigest()
        # Acá se debe controlar con cookies
        resp = make_response(redirect("/discos"))
        resp.set_cookie('username', username)
        resp.set_cookie('token', token)
        controlador_usuarios.actualizar_token(username, token)
        return resp
        
    return render_template("login.html")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
