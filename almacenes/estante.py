from app import app
from dbMySQL import DataBase 
from flask import request, jsonify 

@app.route("/api/almacenes_estante")
def get_estante():
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT * FROM adm_almacen_estante")
        resp = jsonify (rows)
        resp.status_code = 200
        return resp
    except Exception as error:
        print ("Error:", error)
    finally:
        db.cerrarCnn()
        db = None

@app.route("/api/almacenes_estante", methods=['POST'])
def add_estante():
    json_data = request.get_json(force=True)
    descripcion = json_data['descripcion']
    idPasillo = json_data['idPasillo']
    codigo = json_data['codigo']
    nombre = json_data['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("INSERT INTO adm_almacen_estante (descripcion, idPasillo, codigo, nombre) VALUES (%s, %s, %s, %s)", (descripcion, idPasillo, codigo, nombre))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return jsonify({"laastId": cursor.lastrowid})

   
@app.route("/api/almacenes_estante/<idAdmEstante>", methods=['PUT'])
def update_estante(idAdmEstante):
    _json = request.form.to_dict(flat=True)
    descripcion = request.json['descripcion']
    idPasillo = request.json['idPasillo']
    codigo = request.json['codigo']
    nombre = request.json['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("UPDATE adm_almacen_estante SET descripcion = %s, idPasillo = %s, codigo = %s, nombre = %s WHERE idAdmEstante = %s", (descripcion, idPasillo, codigo, nombre, idAdmEstante))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'updated'}

@app.route("/api/almacenes_estante/<idAdmEstante>", methods=['DELETE'])
def delete_estante(idAdmEstante):
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("DELETE FROM adm_almacen_estante WHERE idAdmEstante = (%s)", (idAdmEstante))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'deleted'}