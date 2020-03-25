from app import app
from dbMySQL import DataBase
from flask import request, jsonify

@app.route("/api/almacenes")
def get_almacenes():
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT * FROM adm_almacen")
        resp = jsonify(rows)
        resp.status_code = 200
        #print(resp)
        return resp
    except Exception as error:
        print("Error:", error)
    finally:
        db.cerrarCnn()
        db = None

@app.route("/api/almacenes", methods=['POST'])
def wh():
    json_data = request.get_json(force=True)
    codAlmacen = json_data['codAlmacen']
    nombreAlmacen = json_data['nombreAlmacen']
    descripcion = json_data['descripcion']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("INSERT INTO adm_almacen (codAlmacen, nombreAlmacen, descripcion) VALUES (%s, %s, %s)", (codAlmacen, nombreAlmacen, descripcion))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return jsonify({"laastId": cursor.lastrowid})


@app.route("/api/almacenes2/<idAdmAlmacen>", methods=['PUT']) #esta api no la estoy usando
def update(idAdmAlmacen):
    _json = request.form.to_dict(flat=True)
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("UPDATE adm_almacen SET codAlmacen = %s, nombreAlmacen = %s WHERE idAdmAlmacen = %s", (_json['idAdmAlmacen'], _json['codAlmacen'], _json['nombreAlmacen']))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return jsonify({"LastId": cursor.lastrowid})

@app.route("/api/almacenes/<idAdmAlmacen>", methods=['PUT']) #esta si
def updateAlmacen(idAdmAlmacen):
    _json = request.form.to_dict(flat=True)
    codAlmacen = request.json['codAlmacen']
    nombreAlmacen = request.json['nombreAlmacen']
    descripcion = request.json['descripcion']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos(""" UPDATE adm_almacen 
        SET codAlmacen = %s, nombreAlmacen= %s, descripcion = %s 
        WHERE idAdmAlmacen = %s""", (codAlmacen, nombreAlmacen, descripcion, idAdmAlmacen))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'updated'}


@app.route("/api/almacenes/<idAdmAlmacen>", methods=['DELETE'])
def delete(idAdmAlmacen):
    try:

        db = DataBase()
        db.conectarDB()
        db.inmodDatos("DELETE FROM adm_almacen WHERE idAdmAlmacen = (%s)", (idAdmAlmacen))
        return{'status': 'updated'}
    except Exception as error:
        print("Error:", error)
    finally:
        cursor = db.getCursor()
        db.cerrarCnn()
        db = None
  

