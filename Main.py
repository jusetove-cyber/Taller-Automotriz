#Importaciones
import os #import os -> Permite trabajar con archivos y carpetas del sistema.
from datetime import datetime #from datetime import datetime -> Permite obtener y manipular fechas y horas.

# =========================================================
# FUNCIONES DE CARGA DE DATOS
# =========================================================

def cargarRepuestos():
    #Descripción:
    #Carga los repuestos desde el archivo "Repuestos.csv"
    #y los guarda en un diccionario.

    #Retorno:
    #Diccionario con código, descripción, precio y stock
    #de cada repuesto.

    #Excepciones:
    #Genera error si ocurre un problema al leer el archivo.
    try:
        repuestos = ""
        infoRepuestos = {}
        codigo = ""
        descripcion = ""
        precio = ""
        stock = ""

        repuestos = open("Repuestos.csv","r")
        repuestos.readline()
        

        for indice in repuestos:
            indice = indice.strip().split(",")
            codigo = indice[0]
            descripcion = indice[1]
            precio = int(indice[2])
            stock = int(indice[3])

            infoRepuestos[codigo] = {
                'Descripcion': descripcion,
                'Precio': precio,
                'Stock': stock 
            }
            
        repuestos.close()
        return infoRepuestos
        
    except Exception as e:
        raise e

def cargarServicios():
    #Descripción:
    #Carga los servicios desde el archivo "Servicios.txt"
    #y los guarda en un diccionario.

    #Retorno:
    #Diccionario con código, descripción y costos
    #para gasolina y diesel.

    #Excepciones:
    #Genera error si ocurre un problema al leer el archivo.
    try:
        servicios = {}
        archivoServicios = ""
        descripcion = ""
        costoGasolina = ""
        costoDiesel = ""    

        archivoServicios = open("Servicios.txt", "r")
        archivoServicios.readline()

        for indice in archivoServicios:
            indice = indice.strip().split(",")
            codigo = indice[0]
            descripcion = indice[1]
            costoGasolina = int(indice[2])
            costoDiesel = int(indice[3])
            
            servicios[codigo] = {
                'Descripcion':descripcion,
                'Gasolina':costoGasolina,
                'Diesel':costoDiesel
            }
        
        archivoServicios.close()
        return servicios

    except Exception as e:
        raise e

# =========================================================
# FUNCIONES DE CARGA DE MENUS
# =========================================================

def menu():
    #Descripción:
    #Genera y retorna el menú principal del sistema.
    menu_mostrar = ""
    menu_mostrar += ("\n" + "="*40 + "\n")
    menu_mostrar += ("              MENU PRINCIPAL"+"\n")
    menu_mostrar += ("="*40+"\n")
    menu_mostrar += ("1. Cliente"+"\n")
    menu_mostrar += ("2. Mecanico"+"\n")
    menu_mostrar += ("3. Administrador"+"\n")
    menu_mostrar += ("4. Salir"+"\n")
    menu_mostrar += ("="*40+"\n")

    return menu_mostrar

def menu_usuario():
    #Descripción:
    #Genera y retorna el menú de usuario o cliente.
    menu_us = ""
    menu_us += ("\n" + "="*40+ "\n")
    menu_us += ("              MENU CLIENTE" +"\n")
    menu_us += ("="*40+"\n")
    menu_us += ("1. Registrarse"+"\n")
    menu_us += ("2. Iniciar sesion"+"\n")
    menu_us += ("3. Salir"+"\n")
    menu_us += ("="*40+"\n")

    return menu_us        

def registrarUsuario(datoNombre : str, datoCedula : str, datoPlaca : str, datoMarca : str, datoTipo : str, datoCombustible : str):
    #Descripción:
    #Registra un nuevo usuario guardando sus datos
    #en un archivo de texto.
    try:
        try:
            archivo = ""

            archivo = open(f"Base_Usuarios/{datoCedula}.txt", "r")
            archivo.close()
            return ("El usuario ya existe")   
        
        except FileNotFoundError:

            archivo = open(f"Base_Usuarios/{datoCedula}.txt", "w")
            archivo.write(f"Nombre: {datoNombre}\n")
            archivo.write(f"Cedula: {datoCedula}\n")
            archivo.write(f"Placa: {datoPlaca}\n")
            archivo.write(f"Marca: {datoMarca}\n")
            archivo.write(f"Tipo: {datoTipo}\n")
            archivo.write(f"Combustible: {datoCombustible}\n")

            return ("Usuario Registrado")

    except Exception as e:
        raise e

def iniciarSesion(datoCedula : str, datoPlaca : str):
    #Descripción:
    #Busca un usuario por cédula y valida
    #que la placa ingresada sea correcta.
    try:
        archivo = ""
        datosUsuario = {}
        key = ""
        value = ""

        try:
            archivo = open(f"Base_Usuarios/{datoCedula}.txt", "r")

            for linea in archivo:
                linea = linea.strip().split(":")
                key = linea[0]
                value = linea[1].strip()
                datosUsuario[key] = value
            archivo.close()
            
            if datoPlaca.upper() == datosUsuario['Placa']:
                return datosUsuario
            else:
                return ("Placa incorrecta")
            
        except FileNotFoundError:
            return ("Usuario no encontrado")
            
    except Exception as e:
        raise e

def abrirOrden(datoNombre : str, datoCedula : str, datoPlaca : str, datoMarca : str, datoTipo : str, datoCombustible : str):
    #Descripción:
    #Crea una nueva orden de servicio para un vehículo
    #y guarda la información en un archivo.
    try:
        ordenNueva = open(f"Ordenes_Abiertas/{datoPlaca}.txt","x")

        ordenNueva.write("="*60 + "\n")
        ordenNueva.write("                    ORDEN ABIERTA\n")
        ordenNueva.write("="*60 + "\n\n")

        ordenNueva.write("DATOS DEL CLIENTE\n")
        ordenNueva.write("-"*60 + "\n")

        ordenNueva.write(f"Nombre: {datoNombre}\n")
        ordenNueva.write(f"Cedula: {datoCedula}\n\n")

        ordenNueva.write("DATOS DEL VEHICULO\n")
        ordenNueva.write("-"*60 + "\n")

        ordenNueva.write(f"Placa: {datoPlaca}\n")
        ordenNueva.write(f"Marca: {datoMarca}\n")
        ordenNueva.write(f"Tipo: {datoTipo}\n")
        ordenNueva.write(f"Combustible: {datoCombustible}\n")

        ordenNueva.close()

        archivoListado = open("Listado_Ordenes.txt","a")

        archivoListado.write(f"{datoPlaca}\n")

        archivoListado.close()

        return "Orden creada exitosamente"

    except Exception as e:
        raise e

def actualizarStock(datoRepuestos):
    #Descripción:
    #Actualiza el archivo "Repuestos.csv"
    #con la información actual del stock.
    archivo = open("Repuestos.csv","w")

    archivo.write("Codigo,Descripcion,Precio,Stock\n")

    for codigo in datoRepuestos:

        descripcion = datoRepuestos[codigo]['Descripcion']
        precio = datoRepuestos[codigo]['Precio']
        stock = datoRepuestos[codigo]['Stock']

        archivo.write(f"{codigo},{descripcion},{precio},{stock}\n")

    archivo.close()

def mostrarServicios(datoDespliegueServicio):
    #Descripción:
    #Genera y retorna una tabla con todos
    #los servicios disponibles del taller.
    menuServicios = ""
    infoDescripcion = ""
    infoGasolina  = ""
    infoDiesel = ""

    menuServicios += "="*75 + "\n"
    menuServicios += " "*30 + "SERVICIOS"
    menuServicios += "\n" + "="*75 + "\n\n"
    menuServicios += (f"{'Codigo':<10}{'Descripcion':<30}{'Gasolina':>15}{'Diesel':>15}")
    menuServicios += ("\n" + "-"*75)

    for codigo in datoDespliegueServicio:

        infoDescripcion = datoDespliegueServicio[codigo]['Descripcion']
        infoGasolina = datoDespliegueServicio[codigo]['Gasolina']
        infoDiesel = datoDespliegueServicio[codigo]['Diesel']

        menuServicios += (f"\n{codigo:<10}{infoDescripcion:<30}{infoGasolina:>15}{infoDiesel:>15}")

    return menuServicios
    
def mostrarRepuestos(datoDespliegueRepuestos):
    #Descripción:
    #Genera y retorna una tabla con todos
    #los repuestos disponibles del taller.
    menuRepuestos = ""
    infoDescripcion = ""
    infoPrecio = ""
    infoStock = ""

    menuRepuestos += "="*75 + "\n"
    menuRepuestos += " "*30 + "REPUESTOS"
    menuRepuestos += "\n" + "="*75 + "\n\n"
    menuRepuestos += (f"{'Codigo':<10}{'Descripcion':<30}{'Precio':>15}{'Stock':>15}")
    menuRepuestos += ("\n" + "-"*75)

    for codigo in datoDespliegueRepuestos:

        infoDescripcion = datoDespliegueRepuestos[codigo]['Descripcion']
        infoPrecio = datoDespliegueRepuestos[codigo]['Precio']
        infoStock = datoDespliegueRepuestos[codigo]['Stock']

        menuRepuestos += (f"\n{codigo:<10}{infoDescripcion:<30}{infoPrecio:>15}{infoStock:>15}")
    
    return menuRepuestos

def consultarServicio (datoDespliegueServicio, datoServicioCliente : str, datoCombustibleVehiculo : str):
    #Descripción:
    #Consulta un servicio y retorna su descripción
    #y costo según el tipo de combustible.
    try:
        
        descripcionServicio = "" 
        costoServicio = ""

        if datoServicioCliente in datoDespliegueServicio:
            descripcionServicio = datoDespliegueServicio[datoServicioCliente]['Descripcion']
            costoServicio = datoDespliegueServicio[datoServicioCliente][datoCombustibleVehiculo]

            return descripcionServicio, costoServicio
        else:
            raise KeyError("Servicio no encontrado")

    except KeyError as ke:
        raise ke
    
def consultarRepuesto (datoDespliegueRepuesto, datoRepuestoCliente : str, datoCantidadRepuestos : int):
    #Descripción:
    #Consulta un repuesto y valida si la cantidad
    #solicitada está disponible en stock.
    try:

        descripcionRepuesto = ""
        precioRepuesto = ""
        cantidadRepuestos = datoCantidadRepuestos

        if datoRepuestoCliente in datoDespliegueRepuesto:
            descripcionRepuesto = datoDespliegueRepuesto[datoRepuestoCliente]['Descripcion']
            precioRepuesto = datoDespliegueRepuesto[datoRepuestoCliente]['Precio']

            if cantidadRepuestos > datoDespliegueRepuesto[datoRepuestoCliente]['Stock']:
                
                raise ValueError(f"Solo hay {datoDespliegueRepuesto[datoRepuestoCliente]['Stock']} unidades disponibles")
            else:
                return descripcionRepuesto, precioRepuesto, cantidadRepuestos 
        else:
            raise KeyError("Repuesto no encontrado")
    
    except KeyError as ke:
        raise ke
 
def validacionExistenciaPlacaAbierta(datoPlaca : str):
    #Descripción:
    #Verifica si una placa ya tiene
    #una orden abierta registrada.
    try:
        archivo = ""

        archivo = open(f"Ordenes_Abiertas/{datoPlaca}.txt", "r")
        archivo.close()
        return True
    except FileNotFoundError:
        pass
    return False

def validacionExistenciaPlaca(datoPlaca : str):
    #Descripción:
    #Verifica si una placa existe en las
    #órdenes abiertas o cerradas del sistema.
    try:
        try:
            archivo = ""

            archivo = open(f"Ordenes_Abiertas/{datoPlaca}.txt", "r")
            archivo.close()
            return True   
        except FileNotFoundError:
            pass

        try:
            archivo = ""

            archivo = open(f"Ordenes_Cerradas/{datoPlaca}.txt","r")
            archivo.close()
            return True
        except FileNotFoundError:
            pass
        return False

    except Exception as e:
        raise e

# =========================================================
# FUNCIONES DE VALIDACION
# =========================================================

def validarCedula(datoCedula : str):
    #Descripción:
    #Valida que la cédula solo tenga números
    #y una longitud entre 6 y 10 caracteres.
    if datoCedula.isdigit() == False:
        return False
    elif len(datoCedula) < 6 or len(datoCedula) > 10:
        return False
    return True

def validarNombre(datoNombre : str):
    #Descripción:
    #Valida que el nombre tenga al menos
    #dos palabras y solo contenga letras.
    partesNombre = datoNombre.split()
    if len(partesNombre) < 2:
        return False
    for linea in partesNombre:
        if linea.isalpha() == False or len(linea) < 3:
            return False
    return True

def validarTipoVehiculo(datoTipoVehiculo : str):
    #Descripción:
    #Valida que el tipo de vehículo sea
    #"Automovil" o "Motocicleta".
    if datoTipoVehiculo != "Automovil" and datoTipoVehiculo != "Motocicleta":
        return False
    else:
        return True

def validarPlaca(datoPlaca : str, datoTipoVehiculo : str):
    #Descripción:
    #Valida el formato de la placa según
    #el tipo de vehículo.
    if datoTipoVehiculo == 'Automovil':
        if len(datoPlaca) != 6 or datoPlaca[0:3].isalpha() == False or datoPlaca[3:6].isdigit() == False:
            return False
        else:
            return True
    elif datoTipoVehiculo == 'Motocicleta':
        if len(datoPlaca) != 6 or datoPlaca[0:3].isalpha() == False or datoPlaca[3:5].isdigit() == False or datoPlaca[5].isalpha() == False:
            return False
        else:
            return True
    else:
        if (len(datoPlaca) == 6 and datoPlaca[0:3].isalpha() == True and datoPlaca[3:5].isdigit() == True and datoPlaca[5].isalpha() == True) or (len(datoPlaca) == 6 and datoPlaca[0:3].isalpha() == True and datoPlaca[3:6].isdigit() == True):
            return True
        else:
            return False

def validarMarca(datoMarca : str):
    #Descripción:
    #Valida que la marca solo contenga letras.
    if datoMarca.isalpha() == False:
        return False
    else:
        return True

def validarCombustible(datoCombustible : str):
    #Descripción:
    #Valida que el combustible sea
    #"Gasolina" o "Diesel".
    if datoCombustible != "Gasolina" and datoCombustible != "Diesel":
        return False
    else:
        return True
    
def validarRepuesto(datoRepuesto : str):
    #Descripción:
    #Valida que el código del repuesto
    #tenga el formato correcto.
    if len(datoRepuesto)==3 and datoRepuesto[0] == "R" and datoRepuesto[1:].isnumeric() == True:
        return True
    else:
        return False
    
def validarServicio(datoServicio : str):
    #Descripción:
    #Valida que el código del servicio
    #tenga el formato correcto.
    if len(datoServicio)==3 and datoServicio[0] == "S" and datoServicio[1:].isnumeric() == True:
        return True
    else:
        return False

# =========================================================
# FUNCIONES DE REPORTES ADMINISTRATIVOS
# =========================================================

def reporteInventarioBajo():
    #Descripción:
    #Genera un reporte con los repuestos
    #que tienen un stock menor a 5 unidades.
    try:

        archivo = ""
        linea = []
        codigo = ""
        descripcion = ""
        precio = 0
        stock = 0

        hayInventarioBajo = False

        reporte = ""

        archivo = open("Repuestos.csv", "r")
        archivo.readline()

        reporte += ("\n" + "="*60 + "\n")
        reporte += ("           REPORTE DE INVENTARIO BAJO\n")
        reporte += ("="*60 + "\n")
        reporte += (f"{'CODIGO':<10}{'DESCRIPCION':<30}{'STOCK':>10}")
        reporte += ("\n" + "-"*60)

        for linea in archivo:

            linea = linea.strip().split(",")

            codigo = linea[0]
            descripcion = linea[1]
            precio = int(linea[2])
            stock = int(linea[3])

            if stock < 5:

                reporte += (f"\n{codigo:<10}{descripcion:<30}{stock:>10}")

                hayInventarioBajo = True

        archivo.close()

        if hayInventarioBajo == False:
            reporte += ("\nNo hay repuestos con inventario bajo.")

        return reporte

    except FileNotFoundError:
        return ("No se encontro el archivo Repuestos.csv.")

    except ValueError:
        return ("Hay un error en los datos numericos del archivo.")

    except Exception as e:
        raise e

def guardarOrdenCerrada(datoPlaca : str):
    #Descripción:
    #Guarda la placa de una orden cerrada
    #en el listado de órdenes finalizadas.
    try:
        archivoListado = ""
        linea = ""
        placaExiste = False

        try:
            archivoListado = open("Listado_Ordenes_Cerradas.txt", "r")

            for linea in archivoListado:
                if linea.strip() == datoPlaca:
                    placaExiste = True

            archivoListado.close()

        except FileNotFoundError:
            pass

        if placaExiste == False:
            archivoListado = open("Listado_Ordenes_Cerradas.txt", "a")
            archivoListado.write(f"{datoPlaca}\n")
            archivoListado.close()

    except Exception as e:
        raise e
    
def reporteServiciosFrecuentes():
    #Descripción:
    #Genera un reporte con la frecuencia
    #de los servicios realizados en órdenes cerradas.
    try:

        archivoListado = ""
        archivoOrden = ""

        linea = ""
        partes = []

        placa = ""
        codigoServicio = ""

        serviciosFrecuentes = {}
        reporte = ""

        archivoListado = open("Listado_Ordenes_Cerradas.txt", "r")

        for placa in archivoListado:

            placa = placa.strip()
            
            if placa == "":
                continue

            archivoOrden = open(f"Ordenes_Cerradas/{placa}.txt", "r")

            for linea in archivoOrden:

                if "Codigo Servicio:" in linea:

                    partes = linea.strip().split(":")
                    codigoServicio = partes[1].strip()

                    if codigoServicio in serviciosFrecuentes:
                        serviciosFrecuentes[codigoServicio] += 1
                    else:
                        serviciosFrecuentes[codigoServicio] = 1

            archivoOrden.close()

        archivoListado.close()

        reporte += ("\n" + "="*60 + "\n")
        reporte += ("        REPORTE DE SERVICIOS FRECUENTES\n")
        reporte += ("="*60 + "\n")
        reporte += (f"{'CODIGO SERVICIO':<25}{'FRECUENCIA':>15}\n")
        reporte += ("-"*60 + "\n")

        if len(serviciosFrecuentes) == 0:
            reporte += ("No hay servicios registrados en ordenes cerradas.\n")
        else:
            for codigoServicio in serviciosFrecuentes:
                reporte += (f"{codigoServicio:<25}{serviciosFrecuentes[codigoServicio]:>15}\n")

        return reporte

    except FileNotFoundError:
        return ("No hay ordenes cerradas para generar el reporte.")

    except Exception as e:
        raise e

def reporteRentabilidad():
    #Descripción:
    #Genera un reporte con el total facturado
    #por cada servicio en las órdenes cerradas.
    try:

        archivoListado = ""
        archivoOrden = ""

        linea = ""
        partes = []

        placa = ""
        codigoServicio = ""
        servicioActual = ""

        costoServicio = 0

        rentabilidadServicios = {}
        reporte = ""

        archivoListado = open("Listado_Ordenes_Cerradas.txt", "r")

        for placa in archivoListado:

            placa = placa.strip()

            if placa == "":
                continue

            archivoOrden = open(f"Ordenes_Cerradas/{placa}.txt", "r")

            for linea in archivoOrden:

                if "Codigo Servicio:" in linea:

                    partes = linea.strip().split(":")
                    codigoServicio = partes[1].strip()
                    servicioActual = codigoServicio

                    if servicioActual not in rentabilidadServicios:
                        rentabilidadServicios[servicioActual] = 0

                elif "Costo Mano Obra:" in linea:

                    partes = linea.strip().split(":")
                    costoServicio = int(partes[1].strip())

                    if servicioActual != "":
                        rentabilidadServicios[servicioActual] += costoServicio
                
                elif "Subtotal Repuesto:" in linea:

                    partes = linea.strip().split(":")

                    if len(partes) > 1 and partes[1].strip().isdigit() == True:
                        # Verifica que exista un valor numerico valido
                        # antes de convertirlo a entero

                        costoServicio = int(partes[1].strip())

                        if servicioActual != "":
                            rentabilidadServicios[servicioActual] += costoServicio

            archivoOrden.close()

        archivoListado.close()

        reporte += ("\n" + "="*60 + "\n")
        reporte += ("             REPORTE DE RENTABILIDAD\n")
        reporte += ("="*60 + "\n")
        reporte += (f"{'CODIGO SERVICIO':<25}{'TOTAL FACTURADO':>20}\n")
        reporte += ("-"*60 + "\n")

        if len(rentabilidadServicios) == 0:
            reporte += ("No hay servicios cerrados para calcular rentabilidad.\n")
        else:
            for codigoServicio in rentabilidadServicios:
                reporte += (f"{codigoServicio:<25}{rentabilidadServicios[codigoServicio]:>20}\n")

        return reporte

    except FileNotFoundError:
        return ("No hay ordenes cerradas para generar el reporte.")

    except ValueError:
        return ("Error. Hay costos mal escritos en las ordenes cerradas.")

    except Exception as e:
        raise e

def cerrarOrden(datoPlaca : str):
    #Descripción:
    #Cierra una orden abierta, genera la factura
    #y mueve la orden a órdenes cerradas.

    try:

        archivo = ""
        archivoCerrar = ""
        archivoFactura = ""
        archivoListado = ""

        linea = ""
        partes = []
        lineasListado = []

        subtotal = 0
        iva = 0
        total = 0

        reporte = ""
        fechaFactura = ""

        archivo = open(f"Ordenes_Abiertas/{datoPlaca}.txt", "r")

        archivo.readline()
        archivo.readline()
        archivo.readline()

        reporte += ("\n" + "="*60 + "\n")
        reporte += ("                     FACTURA\n")
        reporte += ("="*60 + "\n\n")

        for linea in archivo:

            reporte += linea

            if "Costo Mano Obra:" in linea:

                partes = linea.strip().split(":")

                if len(partes) > 1 and partes[1].strip().isdigit() == True:
                    subtotal += int(partes[1].strip())

            elif "Subtotal Repuesto:" in linea:

                partes = linea.strip().split(":")

                if len(partes) > 1 and partes[1].strip().isdigit() == True:
                    subtotal += int(partes[1].strip())

        archivo.close()

        if subtotal == 0:
            return("No se puede cerrar una orden sin servicios ni repuestos.")

        iva = int(subtotal * 0.19)

        total = subtotal + iva

        reporte += ("\n" + "-"*60 + "\n")
        reporte += (f"{'SUBTOTAL:':<30}{subtotal:>20}\n")
        reporte += (f"{'IVA 19%:':<30}{iva:>20}\n")
        reporte += (f"{'TOTAL:':<30}{total:>20}\n")
        reporte += ("="*60 + "\n")

        fechaFactura = datetime.now().strftime("%d-%m-%Y")

        archivoFactura = open(f"Factura_{datoPlaca}_{fechaFactura}.txt", "w")

        archivoFactura.write(reporte)

        archivoFactura.close()

        archivo = open(f"Ordenes_Abiertas/{datoPlaca}.txt", "r")

        archivoCerrar = open(f"Ordenes_Cerradas/{datoPlaca}.txt", "w")

        for linea in archivo:

            archivoCerrar.write(linea)

        archivo.close()

        archivoCerrar.close()

        archivoListado = open("Listado_Ordenes.txt", "r")

        for linea in archivoListado:

            if linea.strip() != datoPlaca:

                lineasListado.append(linea)

        archivoListado.close()

        archivoListado = open("Listado_Ordenes.txt", "w")

        for linea in lineasListado:

            archivoListado.write(linea)

        archivoListado.close()

        guardarOrdenCerrada(datoPlaca=datoPlaca)

        os.remove(f"Ordenes_Abiertas/{datoPlaca}.txt")

        return reporte

    except FileNotFoundError:
        return ("No existe una orden abierta con esa placa.")

    except ValueError:
        return ("Error. Hay costos mal escritos en la orden.")
    
    except Exception as e:
        raise e

#Apartado principal
try:
    #----------------------#
    #======================#
       #Datos de entrada:
    #----------------------#
    #======================#

    #Controlan navegacion general
    opcionPrincipal = ""
    opcionCliente = ""
    opcionMecanico = ""
    opcionAdministrador = ""
    #-----------------#
    
    #Datos Personales
    nombreCliente = ""
    cedulaCliente = ""
    #-----------------#

    #Datos del vehiculo
    placaVehiculo = ""
    marcaVehiculo = ""
    tipoVehiculo = ""
    combustibleVehiculo = ""
    #-----------------#

    #Variables para pausas o repetir ciclos
    continuarCicloAdministrador = ""
    continuarCiclo = ""
    #-----------------#

    #Variables para buscar ordenes
    placaBuscar = ""
    #-----------------#

    #Gestion de servicios
    servicioCliente = ""
    agregarServicio = 0
    #-----------------#

    #Gestion de repuestos
    repuestoCliente = ""
    entradaCantidad = ""
    agregarRepuesto = 0

    #----------------------#
    #======================#
        #Datos de salida:
    #----------------------#
    #======================#
    
    #Menus mostrados
    invocar_menu = ""
    invocar_menuUsuario = ""
    mostrar_Repuestos = ""
    mostrar_Servicios = ""
    #-----------------#

    #Resultados de procesos
    registroUsuario = ""
    inicioSesionUsuario = ""    
    crearOrden = ""
    #-----------------#

    #Reportes y facturas
    reporteInventario = ""
    reporteServicios = ""
    reporteCerrarOrden = ""
    reporteFrecuentes = ""
    reporteRentabilidadTexto = ""

    #----------------------#
    #======================#
    #Variables adicionales:
    #======================#
    #----------------------#
    
    #Carga de datos
    despliegueServicios = cargarServicios()
    despliegueRepuestos = cargarRepuestos()
    #----------------------#

    #Manejo de archivos
    archivoOrden = ""
    #----------------------#

    #Variables para controlar la logica interna
    servicioExiste = False
    repuestoExiste = False
    existenciaPlaca = ""
    existenciaPlacaAbierta = ""
    #----------------------#

    #Variables para guardar selecciones temporales
    serviciosSeleccionados = []
    repuestosSeleccionados = []
    #----------------------#

    #Variables auxiliares para guardar retornos de funciones
    descripcionAux = ""
    costoAux = ""
    cantidadAux = 0
    #----------------------#

    #Control interno adicional
    agregar_S_R = ""
    #----------------------#

    #Variables numericas acomuladoras
    valorRepuestos = 0
    valorServicios = 0
    #----------------------#
    
    #Proceso:
    while True:        
        invocar_menu = menu()
        print(invocar_menu)

        opcionPrincipal = input("Seleccione una opcion: ")

        #MENU CLIENTE
        if opcionPrincipal == "1":
            
            while True:

                invocar_menuUsuario = menu_usuario()
                print(invocar_menuUsuario)
                opcionCliente = input("Seleccione una opcion: ")

                if opcionCliente == "1":

                    #Nombre Cliente
                    while True:
                        nombreCliente = input("Ingrese su nombre completo: ").strip().title()
                        if validarNombre(datoNombre=nombreCliente) == True : break
                        else: 
                            print("Escribe bien tu nombre y apellido.") 
                            continue
                    
                    #Cedula cliente
                    while True:
                        cedulaCliente = input("Ingrese su numero de cedula: ")
                        if validarCedula(datoCedula=cedulaCliente) == True: break
                        else: 
                            print("Escribe bien la cedula.")
                            continue

                    # Tipo vehiculo
                    while True:    
                        tipoVehiculo = input("Ingrese el tipo de vehiculo (automovil o motocicleta): ").capitalize()
                        if validarTipoVehiculo(datoTipoVehiculo=tipoVehiculo) == True: break
                        else:
                            print("Escribe bien el tipo de vehiculo.")
                            continue

                    # Solicita y valida la placa dependiendo del tipo de vehiculo:
                    # Automovil -> ABC123
                    # Motocicleta -> ABC12D
                    while True:
                        placaVehiculo = input("Ingrese la placa: ").upper()
                        if validarPlaca(datoPlaca=placaVehiculo, datoTipoVehiculo=tipoVehiculo) == True : break
                        else:
                            print("La placa no corresponde al tipo de vehiculo")
                            continue

                    #Validacion Existencia placa
                    existenciaPlaca = validacionExistenciaPlaca(datoPlaca=placaVehiculo)
                    if existenciaPlaca == True:
                        print("-"*45, "\nEsa placa ya se encuentra registrada.\nEn caso de que sea tuya, por favor inicia sesion.","\n", "-"*45)

                        continuarCiclo = input("\nPresione -> enter <- para continuar. ")
                        continue
                    else:
                        pass

                    # Marca
                    while True:
                        marcaVehiculo = input("Ingrese la marca del vehiculo: ").capitalize()
                        if validarMarca(datoMarca=marcaVehiculo) == True: break
                        else:
                            print("Una marca no puede contener numeros ni caracteres especiales.")
                            continue

                    # Combustible
                    while True:
                        combustibleVehiculo = input("Ingrese combustible (gasolina o diesel): ").capitalize()
                        if validarCombustible(datoCombustible=combustibleVehiculo) == True:
                            break
                        else:
                            print("Ingresa bien el combustible")
                            continue
                    
                    #Registro del usuario
                    registroUsuario = registrarUsuario(datoCedula=cedulaCliente, datoCombustible=combustibleVehiculo, datoMarca=marcaVehiculo, datoNombre=nombreCliente, datoPlaca=placaVehiculo, datoTipo=tipoVehiculo)
                    print("\n",f"{registroUsuario}", "\n") 

                    continuarCiclo = input("\nPresione -> enter <- para continuar. ")
                    
                    if registroUsuario == "El usuario ya existe":
                        continue
                    else:
                        serviciosSeleccionados = []
                        repuestosSeleccionados = []
                        pass

                    crearOrden = abrirOrden(datoNombre=nombreCliente,datoCedula=cedulaCliente,datoPlaca=placaVehiculo,datoMarca=marcaVehiculo,datoTipo=tipoVehiculo,datoCombustible=combustibleVehiculo)
                    serviciosSeleccionados = []

                elif opcionCliente == "2":

                    while True:
                        cedulaCliente = input("Ingrese su numero de cedula: ")
                        if validarCedula(datoCedula=cedulaCliente) == True: break
                        else: 
                            print("Escribe bien la cedula.")
                            continue

                    while True:    
                        placaVehiculo = input("Ingrese la placa: ").upper()
                        if validarPlaca(datoPlaca=placaVehiculo, datoTipoVehiculo="-") == True: break
                        else:
                            print("Escribe bien la placa")
                            continue

                    inicioSesionUsuario = iniciarSesion(datoCedula=cedulaCliente, datoPlaca=placaVehiculo)
                    if inicioSesionUsuario == "Placa incorrecta" or inicioSesionUsuario == "Usuario no encontrado":
                        print(inicioSesionUsuario)
                        continue
                    else:
                        print("Se inicio sesion correctamente")
                    
                    nombreCliente = inicioSesionUsuario['Nombre']
                    cedulaCliente = inicioSesionUsuario['Cedula']
                    placaVehiculo = inicioSesionUsuario['Placa']
                    marcaVehiculo = inicioSesionUsuario['Marca']
                    tipoVehiculo = inicioSesionUsuario['Tipo']
                    combustibleVehiculo = inicioSesionUsuario['Combustible']   

                    existenciaPlacaAbierta = validacionExistenciaPlacaAbierta(datoPlaca=placaVehiculo)
                    if existenciaPlacaAbierta == True:
                        print("Ya existe una orden abierta con esa placa, espera que un mecanico la cierre")
                        
                    else:
                        crearOrden = abrirOrden(datoNombre=nombreCliente,datoCedula=cedulaCliente,datoPlaca=placaVehiculo,datoMarca=marcaVehiculo,datoTipo=tipoVehiculo,datoCombustible=combustibleVehiculo)
                        serviciosSeleccionados = []

                elif opcionCliente == "3":
                    break

                else:
                    print("Opcion invalida.")
                    continue

                
        #MENU MECANICO
        elif opcionPrincipal == "2":

            while True:
                print("\n" + "="*40)
                print("              MENU MECANICO")
                print("="*40)
                print("1. Listar ordenes abiertas")
                print("2. Mostrar detalle de una orden")
                print("3. Agregar servicio a una orden")
                print("4. Agregar repuesto a una orden")
                print("5. Volver")
                print("="*40)

                opcionMecanico = input("Seleccione una opcion: ")

                if opcionMecanico == "1":
                    
                    try:

                        print("\n" + "="*40)
                        print("         ORDENES ABIERTAS")
                        print("="*40)

                        archivoListado = open("Listado_Ordenes.txt","r")

                        for linea in archivoListado:

                            print(linea.strip())

                        archivoListado.close()

                    except FileNotFoundError:

                        print("No hay ordenes abiertas.")

                    continuarCiclo = input("\nPresione -> enter <- para continuar. ")

                elif opcionMecanico == "2":
                    try:
                        placaBuscar = input("Ingrese la placa: ").upper()

                        archivoOrden = open(f"Ordenes_Abiertas/{placaBuscar}.txt","r")

                        print("\n" + "="*40)
                        print("         DETALLE ORDEN")
                        print("="*40)

                        for linea in archivoOrden:

                            print(linea.strip())

                        archivoOrden.close()

                    except FileNotFoundError:

                        print("La orden no existe.")

                    continuarCiclo = input("\nPresione -> enter <- para continuar. ")

                elif opcionMecanico == "3":

                    try:

                        placaBuscar = input("Ingrese la placa: ").upper()

                        archivoOrden = open(f"Ordenes_Abiertas/{placaBuscar}.txt","r")

                        combustibleVehiculo = ""

                        for linea in archivoOrden:

                            linea = linea.strip().split(":")

                            if len(linea) > 1:

                                if linea[0] == "Combustible":

                                    combustibleVehiculo = linea[1].strip()

                        archivoOrden.close()

                        mostrar_Servicios = mostrarServicios(datoDespliegueServicio=despliegueServicios)

                        print(f"\n{mostrar_Servicios}")

                        continuarCicloAdministrador = input("\nPresione -> enter <- para continuar. ")

                        archivoOrden = open(f"Ordenes_Abiertas/{placaBuscar}.txt","a")

                        while True:

                            print("-"*75)

                            # VALIDAR CODIGO
                            while True:

                                servicioCliente = input("Ingresa el servicio que requieres (S01, S02...)\n"+"Ingresa un 0 si quieres salir.\n" + "-"*75 + "\n").strip().capitalize()

                                if servicioCliente == "0":
                                    break

                                if validarServicio(datoServicio=servicioCliente) == True:

                                    if servicioCliente in despliegueServicios:
                                        
                                        if servicioCliente in serviciosSeleccionados:
                                            print("Ese servicio ya fue agregado a la orden")
                                            continue
                                        
                                        break

                                    else:
                                        print("El servicio no existe.")
                                        continue

                                else:
                                    print("Escribe correctamente el codigo")
                                    continue

                            if servicioCliente == "0":
                                break

                            try:

                                descripcionAux, costoAux = consultarServicio(datoDespliegueServicio=despliegueServicios,datoServicioCliente=servicioCliente,datoCombustibleVehiculo=combustibleVehiculo)

                            except KeyError:

                                print("El codigo seleccionado no existe")
                                continue

                            archivoOrden.write("\n")
                            archivoOrden.write("="*50 + "\n")
                            archivoOrden.write(f"Codigo Servicio: {servicioCliente}\n")
                            archivoOrden.write(f"Servicio: {descripcionAux}\n")
                            archivoOrden.write(f"Costo Mano Obra: {costoAux}\n")
                            archivoOrden.write("="*50 + "\n")

                            print("Servicio agregado correctamente.")
                            serviciosSeleccionados.append(servicioCliente)

                            try:

                                agregarServicio = int(input("Deseas agregar otro servicio?\n""1. Si\n""2. No\n" + "-"*30 + "\n"))

                                if agregarServicio == 1:
                                    continue
                                else:
                                    break

                            except ValueError:

                                print("Debes ingresar un numero.")
                                break

                        archivoOrden.close()

                    except FileNotFoundError:

                        print("La orden no existe.")


                elif opcionMecanico == "4":

                    try:

                        placaBuscar = input("Ingrese la placa: ").upper()

                        archivoOrden = open(f"Ordenes_Abiertas/{placaBuscar}.txt","a")

                        mostrar_Repuestos = mostrarRepuestos(datoDespliegueRepuestos=despliegueRepuestos)

                        print(f"\n{mostrar_Repuestos}")

                        continuarCicloAdministrador = input("\nPresione -> enter <- para continuar. ")

                        while True:

                            print("-"*75)

                            while True:

                                repuestoCliente = input("Ingresa el repuesto que requieres (R01, R02...)\n"+"Ingresa un 0 si quieres salir.\n"+ "-"*75 + "\n").strip().capitalize()

                                if repuestoCliente == "0":
                                    break

                                if validarRepuesto(datoRepuesto=repuestoCliente) == True:

                                    if repuestoCliente in despliegueRepuestos:

                                        if despliegueRepuestos[repuestoCliente]['Stock'] <= 0:
                                            print("Ese repuesto no tiene unidades disponibles.")
                                            continue

                                        break

                                    else:
                                        print("El repuesto no existe.")
                                        continue

                                else:
                                    print("Escribe correctamente el codigo")
                                    continue

                            if repuestoCliente == "0":
                                break

                            cancelarRepuesto = False

                            while True:

                                try:

                                    entradaCantidad = input("Ingrese la cantidad de repuestos.\n"+"Ingresa 0 para cancelar.\n"+ "-"*40 + "\n")

                                    cantidadRepuestos = int(entradaCantidad)

                                    if cantidadRepuestos == 0:
                                        cancelarRepuesto = True
                                        break

                                    if cantidadRepuestos < 0:
                                        print("Ingresa un numero mayor a 0.")
                                        continue

                                    descripcionAux, costoAux, cantidadAux = consultarRepuesto(
                                        datoDespliegueRepuesto=despliegueRepuestos,
                                        datoRepuestoCliente=repuestoCliente,
                                        datoCantidadRepuestos=cantidadRepuestos
                                    )

                                    break

                                except ValueError as ve:

                                    if "Solo hay" in str(ve):
                                        print(ve)
                                        continue

                                    elif "invalid literal" in str(ve):
                                        print("Debes ingresar un numero")
                                        continue

                                    else:
                                        print("Error inesperado")
                                        break

                            if cancelarRepuesto == True:
                                break

                            subtotalRep = costoAux * cantidadAux

                            despliegueRepuestos[repuestoCliente]['Stock'] -= cantidadAux

                            actualizarStock(despliegueRepuestos)

                            # GUARDAR EN LA ORDEN1
                            
                            archivoOrden.write("\n")
                            archivoOrden.write("="*50 + "\n")
                            archivoOrden.write(f"Codigo Repuesto: {repuestoCliente}\n")
                            archivoOrden.write(f"Repuesto: {descripcionAux}\n")
                            archivoOrden.write(f"Cantidad: {cantidadAux}\n")
                            archivoOrden.write(f"Subtotal Repuesto: {subtotalRep}\n")
                            archivoOrden.write("="*50 + "\n")

                            if cantidadRepuestos > 0:
                                print("Repuesto agregado correctamente.")

                            try:

                                agregarRepuesto = int(input("Deseas agregar otro repuesto?\n""1. Si\n"+"2. No\n"+ "-"*30 + "\n"))

                                if agregarRepuesto == 1:
                                    continue
                                else:
                                    break

                            except ValueError:

                                print("Debes ingresar un numero.")
                                break

                        archivoOrden.close()

                    except FileNotFoundError:

                        print("La orden no existe.")

                    except ValueError as e:

                        print(e)

                elif opcionMecanico == "5":
                    break

                else:
                    print("Opcion invalida.")

        #MENU ADMINISTRADOR
        elif opcionPrincipal == "3":

            while True:
                print("\n" + "="*40)
                print("           MENU ADMINISTRADOR")
                print("="*40)
                print("1. Cerrar orden")
                print("2. Reporte de inventario bajo")
                print("3. Reporte de servicios frecuentes")
                print("4. Reporte de rentabilidad")
                print("5. Volver")
                print("="*40)

                opcionAdministrador = input("Seleccione una opcion: ")

                if opcionAdministrador == "1":

                    while True:

                        placaBuscar = input("Ingrese la placa de la orden: ").upper()

                        if validarPlaca(datoPlaca=placaBuscar, datoTipoVehiculo="-") == True:
                            break
                        else:
                            print("Placa invalida.")

                    reporteCerrarOrden = cerrarOrden(datoPlaca=placaBuscar)
                    print(reporteCerrarOrden)

                    while True:

                        continuarCicloAdministrador = input("\nPresione -> enter <- para continuar. ")

                        if continuarCicloAdministrador == "":
                            break
                        else:
                            continue

                elif opcionAdministrador == "2":

                    reporteInventario = reporteInventarioBajo()
                    print(reporteInventario)

                    while True:

                        continuarCicloAdministrador = input("\nPresione -> enter <- para continuar. ")

                        if continuarCicloAdministrador == "":
                            break
                        else:
                            continue

                elif opcionAdministrador == "3":

                    reporteFrecuentes = reporteServiciosFrecuentes()
                    print(reporteFrecuentes)

                    while True:

                        continuarCicloAdministrador = input("\nPresione -> enter <- para continuar. ")

                        if continuarCicloAdministrador == "":
                            break
                        else:
                            continue

                elif opcionAdministrador == "4":

                    reporteRentabilidadTexto = reporteRentabilidad()
                    print(reporteRentabilidadTexto)

                    while True:

                        continuarCicloAdministrador = input("\nPresione -> enter <- para continuar. ")

                        if continuarCicloAdministrador == "":
                            break
                        else:
                            continue

                elif opcionAdministrador == "5":
                    break

                else:
                    print("Opcion invalida.")

        elif opcionPrincipal == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida.")

except Exception as e:
    print(f"Ha habido un error {e}")