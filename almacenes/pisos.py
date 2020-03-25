from app import app
from flask import request, jsonify
from dbMySQL import DataBase

@app.route("/api/almacenes_piso")
def get_pisos():
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT * FROM adm_almacen_piso")
        resp = jsonify (rows)
        resp.status_code = 200
        return resp
    except Exception as error:
        print ("Error:", error)
    finally:
        db.cerrarCnn()
        db = None

@app.route("/api/almacenes_piso", methods=['POST'])
def add_pisos():
    json_data = request.get_json(force=True)
    descripcion = json_data['descripcion']
    idAlmacen = json_data['idAlmacen']
    codigo = json_data['codigo']
    nombre = json_data['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("INSERT INTO adm_almacen_piso (descripcion, idAlmacen, codigo, nombre) VALUES (%s, %s, %s, %s)", (descripcion, idAlmacen, codigo, nombre))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return jsonify({"laastId": cursor.lastrowid})

@app.route("/api/almacenes_piso/<idAdmPisoAlmacen>", methods=['DELETE'])
def eliminar(idAdmPisoAlmacen):
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("DELETE FROM adm_almacen_piso WHERE idAdmPisoAlmacen = (%s)", (idAdmPisoAlmacen))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'updated'}

@app.route("/api/almacenes_piso/<idAdmPisoAlmacen>", methods=['PUT'])
def update_piso(idAdmPisoAlmacen):
    _json = request.form.to_dict(flat=True)
    descripcion = request.json['descripcion']
    idAlmacen = request.json['idAlmacen']
    codigo = request.json['codigo']
    nombre = request.json['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("UPDATE adm_almacen_piso SET descripcion = %s, idAlmacen = %s, codigo = %s, nombre = %s WHERE idAdmPisoAlmacen = %s", (descripcion, idAlmacen, codigo, nombre, idAdmPisoAlmacen))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'updated'}