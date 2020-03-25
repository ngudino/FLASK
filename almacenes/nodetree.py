from app import app
from dbMySQL import DataBase
from flask import request, jsonify

@app.route('/api/estructura')
def estructura2():
    try:
        db = DataBase()
        db.conectarDB()
        data = {}
        almacenes = db.leerDatos("SELECT * FROM adm_almacen")
        for d in almacenes:
            data_almacen = {}
            resultado = []
            almacenes = db.leerDatos("SELECT * FROM adm_almacen")
            
            for almacen in almacenes:
                nodo = {}
                almacen_datos = {}
                almacen_datos['tabla'] = 'Almacen'
                almacen_datos['idPropio'] = almacen['idAdmAlmacen']
                almacen_datos['nombre'] = almacen['nombreAlmacen']
                almacen_datos['codigo'] = almacen['codAlmacen']
                almacen_datos['descripcion'] = almacen['descripcion']

                pisos = db.leerDatos("select * from adm_almacen_piso where idAlmacen = %s", almacen['idAdmAlmacen'])
                listaPisos = []
                for piso in pisos:#aqui almaceno el diccionario de cada piso
                    diccionarioPisos = {}
                    piso_datos = {}
                    piso_datos['tabla'] = 'Piso'
                    piso_datos['idPropio'] = piso['idAdmPisoAlmacen']
                    piso_datos['descripcion'] = piso['descripcion']
                    piso_datos['idPadre'] = piso['idAlmacen']
                    piso_datos['codigo'] = piso['codigo']
                    piso_datos['nombre'] = piso['nombre']

                    for p in pisos:#con este loop incluyo cada piso en un {} llamado data
                        diccionarioPisos['data'] = piso_datos#en este diccionario

                        pasillos = db.leerDatos("select * from adm_almacen_pasillo where idPiso = %s", piso['idAdmPisoAlmacen'])
                        listaPasillos = []
                        
                        for pasillo in pasillos:
                            diccionarioPasillos = {}
                            pasillo_datos = {}
                            pasillo_datos['tabla'] = 'Pasillo'
                            pasillo_datos['idPropio'] = pasillo['idPasillo']
                            pasillo_datos['codigo'] = pasillo['codPasillo']
                            pasillo_datos['idPadre'] = pasillo['idPiso']
                            pasillo_datos['descripcion'] = pasillo['descripcion']
                            pasillo_datos['nombre'] = pasillo['nombre']
                            
                            for pas in pasillos:
                                diccionarioPasillos['data'] = pasillo_datos
                            
                            
                            diccionarioPisos['children'] = listaPasillos

                            estantes = db.leerDatos("select * from adm_almacen_estante where idPasillo = %s", pasillo['idPasillo'])
                            listaEstantes = []
                            
                            for estante in estantes:
                                diccionario_estante = {}
                                estante_datos = {}
                                estante_datos['tabla'] = 'Estante'
                                estante_datos['idPropio'] = estante['idAdmEstante']
                                estante_datos['codigo'] = estante['codigo']
                                estante_datos['descripcion'] = estante['descripcion']
                                estante_datos['idPadre'] = estante['idPasillo']
                                estante_datos['nombre'] = estante['nombre']
                                
                                for est in estantes:
                                    diccionario_estante['data'] = estante_datos
                                                                                        
                                diccionarioPasillos['children'] = listaEstantes

                                niveles = db.leerDatos("SELECT * FROM adm_almacen_nivel WHERE idAdmEstante = %s", estante['idAdmEstante'])
                                listaNiveles = []
                                for nivel in niveles:
                                    diccionarioNiveles = {}
                                    nivel_datos = {}
                                    nivel_datos['tabla'] = 'Nivel'
                                    nivel_datos['idPropio'] = nivel['idAdmNivel']
                                    nivel_datos['codigo'] = nivel['codigo']
                                    nivel_datos['descripcion'] = nivel['descripcion']
                                    nivel_datos['idPadre'] = nivel['idAdmEstante']
                                    nivel_datos['nombre'] = nivel['nombre']

                                    for niv in niveles:
                                        diccionarioNiveles['data'] = nivel_datos

                                    diccionario_estante['children'] = listaNiveles

                                    puestos = db.leerDatos("select * from adm_almacen_puesto where idAdmNivelEstante = %s", nivel['idAdmNivel'])
                                    lista_puestos = []
                                    for puesto in puestos:
                                        diccionarioPuestos = {}
                                        puesto_datos = {}
                                        puesto_datos['tabla'] = 'Puesto'
                                        puesto_datos['idPropio'] = puesto['idAdmPuesto']
                                        puesto_datos['idPadre'] = puesto['idAdmNivelEstante']
                                        puesto_datos['descripcion'] = puesto['descripcion']
                                        puesto_datos['codigo'] = puesto['codigo']
                                        puesto_datos['nombre'] = puesto['nombre']
                                        for p in puestos:
                                            diccionarioPuestos['data'] = puesto_datos
                                            diccionarioPuestos['children'] = []
                                        
                                        lista_puestos.extend([diccionarioPuestos])
                                    diccionarioNiveles['children'] = lista_puestos
                                    #print(diccionarioNiveles)

                                    listaNiveles.extend([diccionarioNiveles])

                                listaEstantes.extend([diccionario_estante])

                            listaPasillos.extend([diccionarioPasillos])
                    
                    listaPisos.extend([diccionarioPisos])#agrego la "data" a nivelde children.
            
                nodo['data'] = almacen_datos
                nodo['children'] = listaPisos
                resultado.extend([nodo])
            #db.cerrarCnn()
            #db = None
        return jsonify(resultado)
    except Exception as error:
        print ("Error:", error)
    finally:
        db.cerrarCnn()
        db = None