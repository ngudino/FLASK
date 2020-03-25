from app import app
from dbMySQL import DataBase
from flask import request, jsonify 

@app.route("/api/puesto")
def get_puesto():
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT * FROM adm_almacen_puesto")
        resp = jsonify (rows)
        resp.status_code = 200
        return resp
    except Exception as error:
        print ("Error:", error)
    finally:
        db.cerrarCnn()
        db = None

@app.route("/api/puesto", methods=['POST'])
def add_puesto():
    json_data = request.get_json(force=True)
    idAdmNivelEstante = json_data['idAdmNivelEstante']
    descripcion = json_data['descripcion']
    codigo = json_data['codigo']
    nombre = json_data['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("INSERT INTO adm_almacen_puesto (idAdmNivelEstante, descripcion, codigo, nombre) VALUES (%s, %s, %s, %s)", (idAdmNivelEstante, descripcion, codigo, nombre))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return jsonify({"LastId": cursor.lastrowid})

@app.route("/api/puesto/<idAdmPuesto>", methods=['PUT'])
def update_puesto(idAdmPuesto):
    _json = request.form.to_dict(flat=True)
    idAdmNivelEstante = request.json['idAdmNivelEstante']
    descripcion = request.json['descripcion']
    codigo = request.json['codigo']
    nombre = request.json['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("UPDATE adm_almacen_puesto SET idAdmNivelEstante = %s, descripcion = %s, codigo = %s, nombre = %s WHERE idAdmPuesto = %s", (idAdmNivelEstante, descripcion, codigo, nombre, idAdmPuesto))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'updated'}

@app.route("/api/puesto/<idAdmPuesto>", methods=['DELETE'])
def delete_puesto(idAdmPuesto):
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("DELETE FROM adm_almacen_puesto WHERE idAdmPuesto = (%s)", (idAdmPuesto))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'deleted'}

