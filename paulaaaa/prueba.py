import os
import random

vehiculos = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpiar_pantalla()
    print("=== Auto Seguro ===")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")
    seleccion = input("Seleccione una opción: ")
    return seleccion

def grabar_vehiculo():
    limpiar_pantalla()
    tipo = input("Ingrese el tipo de vehículo: ")
    patente = input("Ingrese la patente del vehículo: ")
    marca = input("Ingrese la marca del vehículo: ")
    precio = float(input("Ingrese el precio del vehículo: "))
    multas_monto = float(input("Ingrese el monto de las multas: "))
    multas_fecha = input("Ingrese la fecha de las multas: ")
    fecha_registro = input("Ingrese la fecha de registro del vehículo: ")
    nombre_dueño = input("Ingrese el nombre del dueño del vehículo: ")
    
    if len(patente) != 6:
        print("La patente debe tener 6 caracteres.")
        input("Presione una tecla para continuar")
        return
    if len(marca) < 2 or len(marca) > 15:
        print("La marca debe tener entre 2 y 15 caracteres.")
        input("Presione una tecla para continuar")
        return
    if precio <= 5000000:
        print("El precio debe ser mayor a $5.000.000.")
        input("Presione una tecla para continuar")
        return
    
    vehiculo = {
        "Tipo": tipo,
        "Patente": patente,
        "Marca": marca,
        "Precio": precio,
        "Multas": {
            "Monto": multas_monto,
            "Fecha": multas_fecha
        },
        "Fecha de Registro": fecha_registro,
        "Nombre del Dueño": nombre_dueño
    }
    
    vehiculos.append(vehiculo)
    print("Vehículo registrado con éxito.")
    input("Presione una tecla para continuar")

def buscar_vehiculo():
    limpiar_pantalla()
    patente_buscar = input("Ingrese la patente del vehículo a buscar: ")
    
    for vehiculo in vehiculos:
        if vehiculo["Patente"] == patente_buscar:
            print("Información del vehículo:")
            print("Tipo: ", vehiculo["Tipo"])
            print("Patente: ", vehiculo["Patente"])
            print("Marca: ", vehiculo["Marca"])
            print("Precio: ", vehiculo["Precio"])
            print("Multas: ", vehiculo["Multas"]["Monto"], "Fecha:", vehiculo["Multas"]["Fecha"])
            print("Fecha de Registro: ", vehiculo["Fecha de Registro"])
            print("Nombre del Dueño: ", vehiculo["Nombre del Dueño"])
            input("Presione una tecla para continuar")
            return
    
    print("No se encontró ningún vehículo con esa patente.")
    input("Presione una tecla para continuar")

def imprimir_certificados():
    limpiar_pantalla()
    
    for vehiculo in vehiculos:
        certificados = {
            "Emisión de contaminantes": random.uniform(1500, 3500),
            "Anotaciones vigentes": random.uniform(1500, 3500),
            "Multas": random.uniform(1500, 3500)
        }
        
        print("Certificado de Emisión de contaminantes:")
        print("Nombre del certificado: Emisión de contaminantes")
        print("Patente del auto: ", vehiculo["Patente"])
        print("Datos del dueño actual: ", vehiculo["Nombre del Dueño"])
        print("Valor del certificado: $", certificados["Emisión de contaminantes"])
        print()
        
        print("Certificado de Anotaciones vigentes:")
        print("Nombre del certificado: Anotaciones vigentes")
        print("Patente del auto: ", vehiculo["Patente"])
        print("Datos del dueño actual: ", vehiculo["Nombre del Dueño"])
        print("Valor del certificado: $", certificados["Anotaciones vigentes"])
        print()
        
        print("Certificado de Multas:")
        print("Nombre del certificado: Multas")
        print("Patente del auto: ", vehiculo["Patente"])
        print("Datos del dueño actual: ", vehiculo["Nombre del Dueño"])
        print("Valor del certificado: $", certificados["Multas"])
        print()
    
    input("Presione una tecla para continuar")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        grabar_vehiculo()
    elif opcion == "2":
        buscar_vehiculo()
    elif opcion == "3":
        imprimir_certificados()
    elif opcion == "4":
        limpiar_pantalla()
        print("Gracias por usar Auto Seguro. ¡Hasta luego!")
        break
    else:
        limpiar_pantalla()
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione una tecla para continuar")