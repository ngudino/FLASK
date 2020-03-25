from app import app
from dbMySQL import DataBase
from flask import request, jsonify

@app.route("/api/almacenes_pasillo")
def get_pasillo():
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT * FROM adm_almacen_pasillo")
        resp = jsonify (rows)
        resp.status_code = 200
        return resp
    except Exception as error:
        print ("Error:", error)
    finally:
        db.cerrarCnn()
        db = None

@app.route("/api/almacenes_pasillo", methods=['POST'])
def add_pasillo():
   json_data = request.get_json(force=True)
   codPasillo = json_data['codPasillo']
   idPiso = json_data['idPiso']
   descripcion = json_data['descripcion']
   nombre = json_data['nombre']
   db = DataBase()
   db.conectarDB()
   db.inmodDatos("INSERT INTO adm_almacen_pasillo (codPasillo, idPiso, descripcion, nombre) VALUES (%s, %s, %s, %s)", (codPasillo, idPiso, descripcion, nombre))
   cursor = db.getCursor()
   db.cerrarCnn()
   db = None
   return jsonify({"laastId": cursor.lastrowid})

@app.route("/api/almacenes_pasillo/<idPasillo>", methods=['DELETE'])
def delete_pasillo(idPasillo):
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("DELETE FROM adm_almacen_pasillo WHERE idPasillo = (%s)", (idPasillo))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'STATUS': 'DELETED'}

@app.route("/api/almacenes_pasillo/<idPasillo>", methods=['PUT'])
def update_pasillo(idPasillo):
    _json = request.form.to_dict(flat=True)
    codPasillo = request.json['codPasillo']
    idPiso = request.json['idPiso']
    descripcion = request.json['descripcion']
    nombre = request.json['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("UPDATE adm_almacen_pasillo SET codPasillo = %s, idPiso = %s, descripcion = %s, nombre = %s WHERE idPasillo = %s", (codPasillo, idPiso, descripcion, nombre, idPasillo))
    cursor = db.getCursor()
    #print(cursor)
    db.cerrarCnn()
    #print('holaaa')
    return{'status': 'updated'}