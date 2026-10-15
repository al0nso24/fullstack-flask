#request = lee los datos que envía la petición
#jsonfy = convierte los datos a formato JSON
from flask import Flask, request, jsonify

#Crea la aplicación
app = Flask(__name__)

alumnos = [
            {'id': 1, 'nombre': 'Ana Torres'},
            {'id': 2, 'nombre': 'Alonso Zegarra'}
           ]

#Recibe la lista de los alumnos
@app.get('/alumnos')
def listar():
 return jsonify(alumnos) #devuelve la lista en formato JSON

#Añadir nuevos alumnos a la lista
@app.post('/alumnos')
def crear():
 datos = request.get_json()
 nuevo = {'id': len(alumnos) + 1, 'nombre': datos['nombre']}
 alumnos.append(nuevo) #añade el nuevo alumno a la lista
 return jsonify(nuevo), 201 #creado correctamente