# Sistema de Gestión de Taller Mecánico
# Descripción
Aplicación desarrollada en Python para la administración básica de un taller mecánico.
El sistema permite registrar clientes, abrir órdenes de servicio, agregar servicios y repuestos, controlar inventario y generar reportes administrativos utilizando archivos locales .txt y .csv.
# Funcionalidades
# Módulo Cliente
•	Registro de usuarios
•	Inicio de sesión mediante cédula y placa
•	Creación automática de órdenes de servicio
# Módulo Mecánico
•	Visualización de órdenes abiertas
•	Consulta del detalle de una orden
•	Agregar servicios a una orden
•	Agregar repuestos a una orden
•	Actualización automática del stock de inventario
# Módulo Administrador
•	Cierre de órdenes
•	Generación de facturas
•	Reporte de inventario bajo
•	Reporte de servicios más frecuentes
•	Reporte de rentabilidad
-	Requisitos
# Para ejecutar el proyecto es necesario tener instalado:
•	Python 3.10 o superior
# Comprobar instalación:
python –version o python3 –version
-	Librerías utilizadas
# El proyecto utiliza únicamente librerías incluidas en Python:
import os
import datetime
# No es necesario instalar dependencias adicionales.
# Estructura del proyecto
El proyecto debe contener exactamente la siguiente estructura:
Proyecto_Taller/
│  
├── main.py
├── Repuestos.csv
├── Servicios.txt    
├── Listado_Ordenes.txt  
├── Listado_Ordenes_Cerradas.txt  
│  
├── Base_Usuarios/    
├── Ordenes_Abiertas/  
├── Ordenes_Cerradas/  
# Archivos necesarios
Repuestos.csv
Archivo encargado de almacenar el inventario de repuestos.
Formato obligatorio:
Codigo,Descripcion,Precio,Stock
R01,Filtro Aceite,25000,10
R02,Bujia,15000,8
R03,Bateria,180000,5
Campos
•	Codigo: identificador del repuesto
•	Descripcion: nombre del repuesto
•	Precio: valor unitario
•	Stock: cantidad disponible
Servicios.txt
Archivo encargado de almacenar los servicios disponibles.
Formato obligatorio:
Codigo,Descripcion,Gasolina,Diesel
S01,Cambio Aceite,50000,65000
S02,Alineacion,40000,40000
S03,Frenos,70000,80000
Campos
•	Codigo: identificador del servicio
•	Descripcion: nombre del servicio
•	Gasolina: costo para vehículos gasolina
•	Diesel: costo para vehículos diésel
-	Configuración inicial
# Antes de ejecutar el programa es obligatorio:
1. Crear las carpetas
Base_Usuarios
Ordenes_Abiertas
Ordenes_Cerradas
2. Crear los archivos
Repuestos.csv
Servicios.txt
Listado_Ordenes.txt
Listado_Ordenes_Cerradas.txt
3. Agregar información inicial
Los archivos Repuestos.csv y Servicios.txt deben contener datos válidos antes de iniciar el sistema.
# Ejecución del programa
1. Abrir terminal en la carpeta del proyecto
2. Ejecutar:
python main.py
o
python3 main.py
# Funcionamiento general
Registro de usuarios
El sistema almacena automáticamente la información de cada cliente en la carpeta:
Base_Usuarios/
Cada usuario se guarda en un archivo .txt identificado por la cédula.
Órdenes abiertas
Las órdenes activas se almacenan en:
Ordenes_Abiertas/
Cada archivo utiliza la placa del vehículo como nombre.
Órdenes cerradas
Cuando una orden es finalizada:
•	se genera la factura,
•	la orden se mueve automáticamente a:
Ordenes_Cerradas/
-	Validaciones implementadas
El sistema valida:
•	Formato de cédula
•	Nombre y apellido
•	Tipo de vehículo
•	Formato de placa
•	Tipo de combustible
•	Existencia de servicios
•	Existencia de repuestos
•	Disponibilidad de stock
•	Existencia de órdenes abiertas
•	Datos numéricos inválidos
# Notas importantes
•	El programa funciona completamente por consola.
•	El sistema utiliza almacenamiento local mediante archivos.
•	Si se eliminan archivos o carpetas requeridas, el programa puede generar errores.
•	El inventario de repuestos se actualiza automáticamente después de cada uso.
