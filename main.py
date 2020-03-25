from app import app

#Rutas Api -----------
#import seguridad.users
import almacenes.almacenes
import almacenes.pisos
import almacenes.pasillo
import almacenes.estante
import almacenes.nivel
import almacenes.puesto
import almacenes.nodetree
import almacenes.ft_almacen_producto
import almacenes.relacion_producto_puesto


if __name__ == "__main__":
    app.run(debug=True) 
    #app.run(debug=True, port=5005, host='10.1.1.32', ssl_context=('cert.pem', 'key.pem'))