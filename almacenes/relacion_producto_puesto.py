from app import app
from dbMySQL import DataBase
from flask import request, jsonify

@app.route("/api/puestoproducto/<idAdmPuesto>", methods=['PUT'])
def puestoproducto(idAdmPuesto):
    try:
        val = int
        json_data = request.get_json(force=True)
        idAdmProducto = json_data['idAdmProducto']
        if idAdmProducto == 0:
            val = None
            idAdmProducto = val
            
        db = DataBase()
        db.conectarDB()
        db.inmodDatos("UPDATE adm_almacen_puesto SET idAdmProducto = %s WHERE idAdmPuesto = %s", (idAdmProducto, idAdmPuesto))
        cursor = db.getCursor()
        return{'status': 'updated'}
    except Exception as error:
        print("error", error)
    db.cerrarCnn()
    db = None
    
