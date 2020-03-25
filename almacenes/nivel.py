from app import app
from dbMySQL import DataBase
from flask import request, jsonify 

@app.route("/api/estante_nivel")
def get_nivel():
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT * FROM adm_almacen_nivel")
        resp = jsonify (rows)
        resp.status_code = 200
        return resp
    except Exception as error:
        print ("Error:", error)
    finally:
        db.cerrarCnn()
        db = None

@app.route("/api/estante_nivel", methods=['POST'])
def add_nivel():
    json_data = request.get_json(force=True)
    descripcion = json_data['descripcion']
    idAdmEstante = json_data['idAdmEstante']
    codigo = json_data['codigo']
    nombre = json_data['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("INSERT INTO adm_almacen_nivel (descripcion, idAdmEstante, codigo, nombre) VALUES (%s, %s, %s, %s)", (descripcion, idAdmEstante, codigo, nombre))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return jsonify({"laastId": cursor.lastrowid})


@app.route("/api/estante_nivel/<idAdmNivel>", methods=['PUT'])
def update_nivel(idAdmNivel):
    _json = request.form.to_dict(flat=True)
    descripcion = request.json['descripcion']
    idAdmEstante = request.json['idAdmEstante']
    codigo = request.json['codigo']
    nombre = request.json['nombre']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("UPDATE adm_almacen_nivel SET descripcion = %s, idAdmEstante = %s, codigo = %s, nombre = %s WHERE idAdmNivel = %s", (descripcion, idAdmEstante, codigo, nombre, idAdmNivel))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return jsonify({"Modificado": cursor.lastrowid})

@app.route("/api/estante_nivel/<idAdmNivel>", methods=['DELETE'])
def delete_nivel(idAdmNivel):
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("DELETE FROM adm_almacen_puesto WHERE idAdmNivelEstante = (%s)", (idAdmNivel))
    db.inmodDatos("DELETE FROM adm_almacen_nivel WHERE idAdmNivel = (%s)", (idAdmNivel))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'DELETED'}
