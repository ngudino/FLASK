from app import app
from dbMySQL import DataBase
from flask import request, jsonify

@app.route('/api/tree')
def tree():
    try:
        data = {}
        db = DataBase()
        db.conectarDB()
        almacenes = db.leerDatos("SELECT * FROM adm_almacen")
        for d in almacenes:
            data_almacen = {}
            nodoppal = {}
            nodo = []
            for almacen in almacenes:
                almacen_datos = {}
                almacen_datos['tabla'] = 'almacen'
                almacen_datos['label'] = almacen["nombreAlmacen"]
                almacen_datos['data'] = [almacen['idAdmAlmacen'], almacen['codAlmacen']]
                almacen_datos['expandedIcon'] = "fa fa-folder-open"
                almacen_datos['collapsedIcon'] = "fa fa-folder"
                almacen_datos['expanded'] = "boolean"
                almacen_datos['leaf'] = "boolean"
                almacen_datos['type'] = "string"
                almacen_datos['parent'] = "TreeNode"
                almacen_datos['partialSelected'] = "boolean"
                almacen_datos['styleClass'] = "string"
                almacen_datos['selectable'] = "boolean"
                
                pisos = db.leerDatos("select * from adm_almacen_piso where idAlmacen = %s", almacen['idAdmAlmacen'])
               
                data_piso = []
                nodoPiso = []                                        
                for piso in pisos:
                    piso_datos = {}
                    piso_datos['tabla'] = 'piso'
                    piso_datos['label'] = piso['nombre']
                    piso_datos['data'] = [piso['idAdmPisoAlmacen'], piso['codigo']]
                    piso_datos['expandedIcon'] = "fa fa-folder-open"
                    piso_datos['collapsedIcon'] = "fa fa-folder"
                    piso_datos['expanded'] = "true"
                    piso_datos['leaf'] = "boolean"
                    piso_datos['type'] = "string"
                    piso_datos['parent'] = "TreeNode"
                    piso_datos['partialSelected'] = "boolean"
                    piso_datos['styleClass'] = "string"
                    piso_datos['selectable'] = "boolean"
                    nodoPiso.append(piso_datos)
                #data_piso.extend(nodoPiso)
                #print(data_piso)

                    pasillos = db.leerDatos("select * from adm_almacen_pasillo where idPiso = %s", piso['idAdmPisoAlmacen'])
                    data_pasillo = []
                    nodoPasillo = []
                    for pasillo in pasillos:
                        pasillo_datos = {}
                        pasillo_datos['tabla'] = 'pasillo'
                        pasillo_datos['label'] = pasillo['nombre']
                        pasillo_datos['data'] = [pasillo['idPasillo'], pasillo['codPasillo']]
                        pasillo_datos['expandedIcon'] = "fa fa-folder-open"
                        pasillo_datos['collapsedIcon'] = "fa fa-folder"
                        pasillo_datos['expanded'] = "true"
                        pasillo_datos['leaf'] = "boolean"
                        pasillo_datos['type'] = "string"
                        pasillo_datos['parent'] = "TreeNode"
                        pasillo_datos['partialSelected'] = "boolean"
                        pasillo_datos['styleClass'] = "string"
                        pasillo_datos['selectable'] = "boolean"
                        nodoPasillo.append(pasillo_datos)
                    
                    estantes = db.leerDatos("select * from adm_almacen_estante where idPasillo = %s", pasillo['idPasillo'])
                    data_estante = []
                    nodoEstante = []
                    for estante in estantes:
                        estante_datos = {}
                        estante_datos['tabla'] = 'estante'
                        estante_datos['label'] = estante['nombre']
                        estante_datos['data'] = [estante['idAdmEstante'], estante['codigo']]
                        estante_datos['expandedIcon'] = "fa fa-folder-open"
                        estante_datos['collapsedIcon'] = "fa fa-folder"
                        estante_datos['expanded'] = "true"
                        estante_datos['leaf'] = "boolean"
                        estante_datos['type'] = "string"
                        estante_datos['parent'] = "TreeNode"
                        estante_datos['partialSelected'] = "boolean"
                        estante_datos['styleClass'] = "string"
                        estante_datos['selectable'] = "boolean"
                        nodoEstante.append(estante_datos)
                        
                        niveles = db.leerDatos("SELECT * FROM adm_almacen_nivel WHERE idAdmEstante = %s", estante['idAdmEstante'])
                        data_nivel = []
                        nodoNivel = []
                        for nivel in niveles:
                            nivel_datos = {}
                            nivel_datos['tabla'] = 'nivel'
                            nivel_datos['label'] = nivel['nombre']
                            nivel_datos['data'] = [nivel['idAdmNivel'], nivel['codigo']]
                            nivel_datos['expandedIcon'] = "fa fa-folder-open"
                            nivel_datos['collapsedIcon'] = "fa fa-folder"
                            nivel_datos['expanded'] = "true"
                            nivel_datos['leaf'] = "boolean"
                            nivel_datos['type'] = "string"
                            nivel_datos['parent'] = "TreeNode"
                            nivel_datos['partialSelected'] = "boolean"
                            nivel_datos['styleClass'] = "string"
                            nivel_datos['selectable'] = "boolean"
                            nodoNivel.append(nivel_datos)
                            
                            puestos = db.leerDatos("select * from adm_almacen_puesto where idAdmNivelEstante = %s", nivel['idAdmNivel'])
                            data_puesto = []
                            nodoPuesto = []
                            for puesto in puestos:
                                puesto_datos = {}
                                puesto_datos['tabla'] = 'puesto'
                                puesto_datos['label'] = puesto['nombre']
                                puesto_datos['data'] = puesto['idAdmPuesto'], puesto['idAdmProducto'], puesto['codigo']
                                puesto_datos['expandedIcon'] = "fa fa-folder-open"
                                puesto_datos['collapsedIcon'] = "fa fa-folder"
                                puesto_datos['leaf'] = "boolean"
                                puesto_datos['type'] = "DISPONIBLE"
                                puesto_datos['parent'] = "TreeNode"
                                puesto_datos['partialSelected'] = "boolean"
                                puesto_datos['styleClass'] = "string"
                                puesto_datos['selectable'] = "boolean"
                                nodoPuesto.append(puesto_datos)
                                data_puesto.extend(nodoPuesto)
                                nivel_datos['children'] = nodoPuesto
                                
                        data_nivel.extend(nodoNivel)
                        estante_datos['children'] = data_nivel
                        
                        data_estante.extend(nodoEstante)
                        pasillo_datos['children'] = data_estante

                    data_pasillo.extend(nodoPasillo)
                    piso_datos['children'] = data_pasillo

                data_piso.extend(nodoPiso)
                almacen_datos['children'] = data_piso
                nodo.extend([almacen_datos])
            nodoppal = nodo
        data['data'] = nodoppal
        #print(data)
        return jsonify(data)
    except Exception as error:
        print ("Error:", error)
    finally:
        db.cerrarCnn()
        db = None


#### manjear vinculacion de almacenes con el producto

@app.route("/api/ftAlmacen/<idAdmProducto>", methods=['PUT'])
def PostPuestoAlmacen(idAdmProducto):
    json_data = request.get_json(force=True)
    idPuestoAlmacen = json_data['idAdmPuesto']
    #print(idAdmProducto)
    #print(idPuestoAlmacen)
    db = DataBase()
    db.conectarDB()
    if not idPuestoAlmacen:
        idPuestoAlmacen = "0"
    db.inmodDatos("UPDATE adm_productos SET idPuestoAlmacen = %s WHERE idAdmProducto = %s", (idPuestoAlmacen, idAdmProducto))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return{'status': 'updated'}

@app.route("/api/ftAlmacen/<idAdmProducto>", methods=['GET'])
def getPuestoProducto(idAdmProducto):
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT idPuestoAlmacen FROM adm_productos WHERE idAdmProducto = (%s)", (idAdmProducto))
        resp = jsonify(rows)
        resp.status_code = 200
        return(resp)
    except Exception as error:
        print("error:", error)
    finally:
        #cursor = db.getcursor()
        db.cerrarCnn()
        db = None


############### Manejo de Tabla Hija ######################

@app.route("/api/puesto-producto", methods=['POST'])
def PostPuestoProducto():
    json_data = request.get_json(force=True)
    idAdmPuesto = json_data['idAdmPuesto']
    idAdmProducto = json_data['idAdmProducto']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("INSERT INTO adm_almacen_puesto_producto (idAdmPuesto, idAdmProducto) VALUES (%s, %s)", (idAdmPuesto, idAdmProducto))
    cursor = db.getCursor()
    db.cerrarCnn()
    db = None
    return jsonify({"LastId": cursor.lastrowid})

@app.route("/api/puesto-producto/<idAdmProducto>", methods=['PUT'])
def PutPuestoProducto(idAdmProducto):
    json_data = request.get_json(force=True)
    idAdmPuesto = json_data['idAdmPuesto']
    #idAdmProducto = json_data['idAdmProducto']
    db = DataBase()
    db.conectarDB()
    db.inmodDatos("UPDATE adm_almacen_puesto_producto SET idAdmPuesto = %s WHERE idAdmProducto = %s", (idAdmPuesto, idAdmProducto))
    cursor = db.getCursor()
    db.cerrarCnn
    db = None
    return {'status': 'updated'}


#para mostrar los puestos que ocupa un producto
@app.route("/api/puesto-producto/<idAdmProducto>", methods=['GET'])
def getByPuestoProducto(idAdmProducto):
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT idAdmPuesto FROM adm_almacen_puesto_producto WHERE idAdmProducto = %s", (idAdmProducto))
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as error:
        print("Error", error)
    finally:
        db.cerrarCnn()
        db = None

#para mostrar todos los puesto ocupados independientemente del producto
@app.route("/api/puesto-producto", methods=['GET'])
def getPuestosOcupados():
    try:
        db = DataBase()
        db.conectarDB()
        rows = db.leerDatos("SELECT idAdmPuesto FROM adm_almacen_puesto_producto")
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as error:
        print("Error", error)
    finally:
        db.cerrarCnn()
        db = None
