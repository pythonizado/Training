from flask import Flask, render_template, request
import sqlite3

#empiezo flask
app = Flask(__name__)

#index
@app.route("/")
def home(): 
    return render_template("index.html")

#rutas a los objetos
@app.route("/proveeInsert") 
def proveeInsert():
      return render_template("proveedor.html")

@app.route("/clienteInsert") 
def clienteInsert():
      #CREO MI CONEXION 
      mi_conexion = sqlite3.connect("C:/Users/leandro/Documents/python/flaskFormSQLPythoonHTML/BDsupermercado.db", timeout=10)
      cursor = mi_conexion.cursor()
      crud = cursor.execute("SELECT NOMBRE FROM CLIENTE WHERE NOMBRE != 'DESHABILITADO'") 
      return render_template("cliente.html", crud = crud)

@app.route("/productoInsert") 
def productoInsert():
      #CREO MI CONEXION 
      mi_conexion = sqlite3.connect("C:/Users/leandro/Documents/python/flaskFormSQLPythoonHTML/BDsupermercado.db", timeout=10)
      cursor = mi_conexion.cursor()
      crudProducto = cursor.execute("SELECT NOMBRE_PRODUCTO FROM PRODUCTO WHERE NOMBRE_PRODUCTO != 'DESHABILITADO'") 
      return render_template("producto.html", crudProducto = crudProducto)

@app.route("/ventaInsert") 
def ventaInsert():
      return render_template("venta.html")

#insert de proveedores
@app.route('/proeveedor', methods=["POST"])
def provee():
    #capturo la info del form
    nombreEmp = request.form.get("nombreEmpresa")
    celular = request.form.get("celular")
    telefono = request.form.get("telefono")
    personaContacto = request.form.get("personaContacto")
    razonSocial = request.form.get("razonSocial")
    rut = request.form.get("rut")

    try:
            #CREO MI CONEXION 
            mi_conexion = sqlite3.connect("C:/Users/leandro/Documents/python/flaskFormSQLPythoonHTML/BDsupermercado.db", timeout=10)
            cursor = mi_conexion.cursor()
            #convierto a string
            nombreSTR = str(nombreEmp)
            celularSTR = str(celular)
            telefonoSTR = str(telefono)
            personaContactoSTR = str(personaContacto)
            razonSocialSTR = str(razonSocial)
            rutSTR  = str(rut)
            cursor.execute("INSERT INTO PROVEEDORES (ID_PROVEEDOR, NOMBRE_EMPRESA, CELULAR, TELEFONO, CONTACTO, RAZON_SOCIAL,RUT) VALUES(NULL,'"+nombreSTR+"','"+celularSTR+"','"+ telefonoSTR +"','"+ personaContactoSTR +"','"+ razonSocialSTR +"','"+ rutSTR +"');")
            mi_conexion.commit()
            mi_conexion.close()
      
    except Exception as ex:
            print( ex )
            print("falla el insert de proveedor") 
     #la página contacto solo es para dar un aviso de que la operación fue exitosa        
    return render_template("contacto.html", nombre = nombreSTR)

#insert de cliente
@app.route('/cliente', methods=["POST"])
def cliente():
    nombre = request.form.get("nombre")
    celular = request.form.get("celular")
    fec_nac = request.form.get("fec_nac")

    try:
            #CREO MI CONEXION CON PONER EL NOMBRE DE LA BD YA ME LA CREA
            mi_conexion = sqlite3.connect("C:/Users/leandro/Documents/python/flaskFormSQLPythoonHTML/BDsupermercado.db", timeout=10)
            cursor = mi_conexion.cursor()
            nombreSTR = str(nombre)
            celularSTR = str(celular)
            cursor.execute("INSERT INTO CLIENTE (ID_CLIENTE, FEC_NAC, NOMBRE, CELULAR) VALUES(NULL,'"+nombreSTR+"','"+celularSTR+"','"+ fec_nac+"');")
            mi_conexion.commit()
            mi_conexion.close()
      
    except Exception as ex:
            print( ex ) 
            print("falló el insert de cliente")
     #la página contacto solo es para dar un aviso de que la operación fue exitosa
    return render_template("contacto.html", nombre = nombreSTR)


#Deshabilito cliente pero no lo borro para no llevarme con él sus compras (para nosotros ventas)
@app.route('/deleteCliente/<i>')
def deleteCliente(i):
        try:
            #CREO MI CONEXION 
            mi_conexion = sqlite3.connect("C:/Users/leandro/Documents/python/flaskFormSQLPythoonHTML/BDsupermercado.db", timeout=10)
            cursor = mi_conexion.cursor()
            #le borrro los caracteres raros que me devuelve al traerlos del html
            i = i[:-3]
            i = i[1:]
            i = i[1:]
            #aplico cambios
            cursor.execute("UPDATE CLIENTE SET NOMBRE = 'DESHABILITADO' WHERE NOMBRE = '"+ i +"'")
            mi_conexion.commit()
            mi_conexion.close()
      
        except Exception as ex:
            print( ex ) 
            print("fallo del delete de cliente")
     #la página contacto solo es para dar un aviso de que la operación fue exitosa
        return render_template("index.html")



#insert de productos
@app.route('/producto', methods=["POST"])
def producto():
    #capturo los datos del form
    nombrePro = request.form.get("nombreProducto")
    marca = request.form.get("marca")
    precio = request.form.get("precio")
    stock = request.form.get("stock")
    descripcionStock = request.form.get("descripcionStock")
    peso = request.form.get("peso")
    volumen = request.form.get("volumen")
    envase = request.form.get("envase")
    vencimiento = request.form.get("vencimiento")
    promo = request.form.get("promo")
    proveedor = request.form.get("proveedor")
    #convierto el ON OFF de html a 1 o 0 de boolean
    if promo == 'on':
            promo = '1'
            print("soy promo en el if" + promo)
    else:
            promo = '0'
            print("soy promo en el else" + promo)
    try:
            #creo mi conexión 
            mi_conexion = sqlite3.connect("C:/Users/leandro/Documents/python/flaskFormSQLPythoonHTML/BDsupermercado.db", timeout=10)
            cursor = mi_conexion.cursor()
            #inserto un producto
            cursor.execute("INSERT INTO PRODUCTO (ID_PRODUCTO, NOMBRE_PRODUCTO, MARCA_PRODUCTO, PRECIO, STOCK, DESCRIPCION_STOCK, PESO, VOLUMEN, ENVASE, VENCIMIENTO, PROMO, PROVEEDOR_PRO ) VALUES(NULL,'"+nombrePro+"','"+marca+"','"+ precio +"','"+stock +"','"+descripcionStock+"','"+peso +"', '"+volumen+"', '"+envase+"', '"+vencimiento+"', '"+promo+"', '"+proveedor+"');")
            #guardo y cierro la conexión
            mi_conexion.commit()
            mi_conexion.close()
      
    except Exception as ex:
            print( ex ) 
    #la página contacto solo es para dar un aviso de que la operación fue exitosa         
    return render_template("contacto.html", nombre = nombrePro)

#Deshabilito producto pero no lo borro para no llevarme con él sus ventas
@app.route('/deleteProducto/<p>')
def deleteProducto(p):
        try:
            #CREO MI CONEXION 
            mi_conexion = sqlite3.connect("C:/Users/leandro/Documents/python/flaskFormSQLPythoonHTML/BDsupermercado.db", timeout=10)
            cursor = mi_conexion.cursor()
            #le borrro los caracteres raros que me devuelve al traerlos del html
            p = p[:-3]
            p = p[1:]
            p = p[1:]
            #aplico cambios
            cursor.execute("UPDATE PRODUCTO SET NOMBRE_PRODUCTO = 'DESHABILITADO' WHERE NOMBRE_PRODUCTO = '"+ p +"'")
            mi_conexion.commit()
            mi_conexion.close()
      
        except Exception as ex:
            print( ex ) 
            print("fallo del delete de PROCUTOS")
     #la página contacto solo es para dar un aviso de que la operación fue exitosa
        return render_template("index.html")

#insert de las ventas
@app.route('/venta', methods=["POST"])
def venta():
    #capturo los datos del form
    proA = request.form.get("productoA")
    cantA = request.form.get("cant_proA")
    proB = request.form.get("productoB")
    cantB = request.form.get("cant_proB")
    proC = request.form.get("productoC")
    cantC = request.form.get("cant_proC")
    proD = request.form.get("productoD")
    cantD = request.form.get("cant_proD")
    proE = request.form.get("productoE")
    cantE = request.form.get("cant_proE")
    proF = request.form.get("productoF")
    cantF = request.form.get("cant_proF")
    proG = request.form.get("productoG")
    cantG = request.form.get("cant_proG")
    proH = request.form.get("productoH")
    cantH = request.form.get("cant_proH")
    clienteCompra = request.form.get("cliente_compra")
    descripcion = request.form.get("descripcion")
    #convierto todo a numeros enteros
    proAint = int(proA)
    cantAint = int(cantA)
    proBint = int(proB)
    cantBint = int(cantB)
    proCint = int(proC)
    cantCint = int(cantC)
    proDint = int(proD)
    cantDint = int(cantD)
    proEint = int(proE)
    cantEint = int(cantE)
    proFint = int(proF)
    cantFint = int(cantF)
    proGint = int(proG)
    cantGint = int(cantG)
    proHint = int(proH)
    cantHint = int(cantH)
    #calculo el costo del total de la compra
    total= proAint*cantAint+proBint*cantBint+proCint*cantCint+proDint*cantDint+proEint*cantEint+proFint*cantFint+proGint*cantGint+proHint*cantHint 
    print('el total es: '+ str(total))

    try:
            #CREO MI CONEXION 
            mi_conexion = sqlite3.connect("C:/Users/leandro/Documents/python/flaskFormSQLPythoonHTML/BDsupermercado.db", timeout=10)
            cursor = mi_conexion.cursor()
            cursor.execute("INSERT INTO VENTA (ID_VENTA, PRODUCTO_A, CANTIDAD_PRO_A, PRODUCTO_B, CANTIDAD_PRO_B, PRODUCTO_C, CANTIDAD_PRO_C, PRODUCTO_D, CANTIDAD_PRO_D, PRODUCTO_E, CANTIDAD_PRO_E, PRODUCTO_F, CANTIDAD_PRO_F, PRODUCTO_G, CANTIDAD_PRO_G, PRODUCTO_H, CANTIDAD_PRO_H, CLIENTE_COMPRA, DESCRIPCION, COSTO_TOTAL) VALUES(NULL,'"+proA+"','"+cantA+"','"+proB+"','"+cantB+"','"+proC+"','"+cantC+"','"+proD+"','"+cantD+"','"+proE+"','"+cantE+"','"+proF+"','"+cantF+"','"+proG+"','"+cantG+"','"+proH+"','"+cantH+"','"+clienteCompra+"','"+descripcion+"','"+str(total)+"');")
            #Guardo y cierro mi conexión
            mi_conexion.commit()
            mi_conexion.close()
      
    except Exception as ex:
            print( ex ) 
            print("falla el insert de venta")
        #vuelvo a la página de venta para efectuar otra venta más
    return render_template("venta.html")

#pongo en marcha la app
if __name__ == "__main__":
    app.run(debug=True)


