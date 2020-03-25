from flask import jsonify, request
<<<<<<< HEAD
from app import app, db

=======
#from app import DataBase
from dbMySQL import ..DataBase
>>>>>>> master
import json

@app.route("/api/users")
def all_users():
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT * FROM adm_tipo_medidas")
        temp = {[1]}
        #print(rows)
        #rows_no = OrderedDict(rows)
        #temp = rows
        resp = jsonify(temp)
        #resp = json.dumps(rows, sort_keys=False)
        #print(resp)
        #resp = json.dumps(rows, sort_keys=False, indent=4, separators=(',', ': '))
        resp.status_code = 200
        return resp
    except Exception as error:
        print("Error: ", error)
    finally:
        db.cerrarCnn()
        db = ''

@app.route("/api/almacenes")
def almacenes():
    try:
        db.conectarDB()
        rows = db.leerDatos("SELECT * FROM adm_almacenes")
        resp = jsonify(rows)
        resp.status_code = 200
        #resp.headers = {'Access-Control-Allow-Origin': '*'}
        return resp
    except Exception as error:
        print("Error: ", error)
    finally:
        db.cerrarCnn()

@app.route("/nuevoTareas", methods=['POST'])
def add():
    _json = request.form.to_dict(flat=True)
    #print(_json)
    db.conectarDB()
    db.inmodDatos("INSERT INTO tb_tareas (nombre, descripcion) VALUES (%s, %s)", (_json['nombre'], _json['descripcion']))
    cursor = db.getCursor()
    db.cerrarCnn()
    return jsonify({"LastId": cursor.lastrowid})
    


