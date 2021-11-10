"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import controller
from DISClib.ADT import list as lt
import folium

assert cf

UFOfile = 'UFOS-utf8-large.csv'
cont = None

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def imprimirAvistamiento(lista):
    for avistamiento in lt.iterator(lista):
        print()
        print('fecha y hora: ', avistamiento['datetime'])
        print('ciudad: ', avistamiento['city'])
        print('estado: ', avistamiento['state'])
        print('país: ', avistamiento['country'])
        print('forma: ', avistamiento['shape'])
        print('duración en segundos : ', avistamiento['duration (seconds)'])
        print('duración en horas : ', avistamiento['duration (hours/min)'])
        print('comentarios : ', avistamiento['comments'])
        print('dia postead : ', avistamiento['date posted'])
        print('latitud: ', avistamiento['latitude'])
        print('longitud : ', avistamiento['longitude'])
    print()


def imprimirCiudades(lista):
    for avistamiento in lt.iterator(lista):
        print()
        print('fecha y hora: ', avistamiento['datetime'])
        print('ciudad: ', avistamiento['city'])
        print('país: ', avistamiento['country'])
        print('duración en segundos : ', avistamiento['duration (seconds)'])
        print('forma: ', avistamiento['shape'])
    print()


def imprimirFechas(lista):
    for avistamiento in lt.iterator(lista):
        print()
        print('fecha y hora: ', avistamiento['datetime'])
        print('ciudad: ', avistamiento['city'])
        print('país: ', avistamiento['country'])
        print('duración en segundos : ', avistamiento['duration (seconds)'])
        print('forma: ', avistamiento['shape'])
        print('longitud: ', avistamiento['longitude'])
        print('latitud: ', avistamiento['latitude'])
    print()


def imprimirLongitud(lista, imagenes):
    numero = 1
    if lt.size(lista) >= 10:
        lista = obtener10(lista)
    for avistamiento in lt.iterator(lista):
        print()
        print('fecha y hora: ', avistamiento['datetime'])
        print('ciudad: ', avistamiento['city'])
        print('país: ', avistamiento['country'])
        print('duración en segundos : ', avistamiento['duration (seconds)'])
        print('forma: ', avistamiento['shape'])
        if imagenes:
            mapa = folium.Map(location=[avistamiento['latitude'], avistamiento['longitude']], zoom_start=13)
            mapa.save("mapa" + str(numero) + ".html")
        numero += 1
    print()
def imprimirduracionS(lista):
    for avistamiento in lt.iterator(lista):
        print()
        print('fecha y hora: ',avistamiento['datetime'])
        print('ciudad: ',avistamiento['city'])
        print('estado: ' ,avistamiento['state'])
        print('país: '  ,avistamiento['country'])
        print('forma: '  ,avistamiento['shape'])
        print('duración en segundos : '  ,avistamiento['duration (seconds)'])
    print()


def obtener10(lista):
    final = lt.newList()
    lt.addLast(final, lt.getElement(lista, 1))
    lt.addLast(final, lt.getElement(lista, 2))
    lt.addLast(final, lt.getElement(lista, 3))
    lt.addLast(final, lt.getElement(lista, 4))
    lt.addLast(final, lt.getElement(lista, 5))
    lt.addLast(final, lt.getElement(lista, lt.size(final) - 4))
    lt.addLast(final, lt.getElement(lista, lt.size(final) - 3))
    lt.addLast(final, lt.getElement(lista, lt.size(final) - 2))
    lt.addLast(final, lt.getElement(lista, lt.size(final) - 1))
    lt.addLast(final, lt.getElement(lista, lt.size(final)))
    return final


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- Req1, Contar los avistamientos en una ciudad")
    print("4- Req2, Contar los avistamientos por duración")
    print("5- Req3, Contar avistamientos por Hora/Minutos del día")
    print("6- Req4. Contar los avistamientos en un rango de fechas")
    print("7- Req5, Contar los avistamientos de una Zona Geográfica")
    print("8- Req6, Visualizar los avistamientos de una zona geográfica")

def imprimirLongitud(lista):
    if lt.size(lista) >= 10:
        lista = obtener10(lista)
    for avistamiento in lt.iterator(lista):
        print()
        print('fecha y hora: ', avistamiento['datetime'])
        print('ciudad: ', avistamiento['city'])
        print('país: ', avistamiento['country'])
        print('duración en segundos : ', avistamiento['duration (seconds)'])
        print('forma: ', avistamiento['shape'])
    print()


def guardarMapa(lista, longitudMinima, latitudMinima):
    mapa = folium.Map(location=[latitudMinima, longitudMinima], zoom_start=6)
    for avistamiento in lt.iterator(lista):
        html = "<table>" \
               "<tr>" \
               "<th> City </th>" \
               "<th> Datetime </th>" \
               "<th> Duration (s) </th>" \
               "<th> Shape </th>" \
               "<th> Comments </th>" \
               "</tr>"
        html = html + "<tr><td>" + str(avistamiento['city']) + "</td>" \
                                                               "<td>" + str(avistamiento['datetime']) + "</td>" \
                                                                                                        "<td>" + str(
            avistamiento['duration (seconds)']) + "</td>" \
                                                  "<td>" + str(avistamiento['shape']) + "</td>" \
                                                                                        "<td>" + str(
            avistamiento['comments']) + "</td></tr></table> "
        folium.Marker(
            location=[avistamiento['latitude'], avistamiento['longitude']],
            popup=folium.Popup(html, min_width=600, max_width=600),
            tooltip="Click para expandir"
        ).add_to(mapa)
    mapa.save("mapa.html")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos ....")
        controller.loadData(cont, UFOfile)
        print('Avistamientos cargados: ' + str(controller.AvistamientoSize(cont)))
        listaAvistamientos = controller.getAvistamientos(cont)
        imprimirAvistamiento(listaAvistamientos)

    elif int(inputs[0]) == 3:
        ciudad = input("Ingrese la ciudad a consultar: ")
        cantidad, listas, ciudades = controller.totalAvistamientosCiudad(cont, ciudad)
        print("============ Respuesta Requerimiento 1 ============")
        print("hay", ciudades, "diferentes con avistamientos de UFOS")
        print("Hay" + str(cantidad) + "avistamientos en:  " + ciudad)
        print("Los primeros 3 y los untimos 3 avistamientos en la ciudad" + ciudad + "son:")
        imprimirCiudades(listas)

    elif int(inputs[0]) == 4:
        entregarSmin = input("inserte una duración de segundos minima: ")
        entregarSmax = input("inserte una duración de segundos maxima: ")
        cantidad, dur_max, listas = controller.duracionSegundos(cont, entregarSmin, entregarSmax)
        print(" la cantidad total de avistamientos es: ", cantidad)
        print("la duracion maxima es de: ", dur_max)
        imprimirduracionS(listas)

    elif int(inputs[0]) == 5:
        entregarHmax = input("inserte una hora y minuto maxima del dia: ")
        entregarHmin = input("inserte una hora y minuto minima del dia: ")
        cantidad, dur_max, listas,cantidad2 = controller.duracionHM(cont, entregarHmin, entregarHmax)
        print(" hay ", cantidad2, "avistamientos en diferentes horas")
        print(" la cantidad total de avistamientos entre ",entregarHmin," y ",entregarHmax,"es de", cantidad)
        imprimirduracionS(listas)

    elif int(inputs[0]) == 6:
        fechainicial = input("ingrese la fecha inicial:  ")
        fechafinal = input("ingrese la fecha final:  ")
        listas, totufos, fecha = controller.getavistamientoByRange(cont, fechainicial, fechafinal)
        print("============ Respuesta Requerimiento 4 ============")
        print("Hay", fecha, "diferentes fechas de avistamiento de UFOS")
        print("Hay" + str(totufos) + "avistamientos entre" + fechainicial + "y" + fechafinal)
        print("Los primeros 3 y los untimos 3 avistamientos en estas fechas son :")
        imprimirFechas(listas)

    elif int(inputs[0]) == 7:
        longitudMinima = input("ingrese una longitud minima: ")
        longitudMaxima = input("ingrese una longitud maxima:  ")
        latitudMinima = input("ingrese una latitud minima:  ")
        latitudMaxima = input("ingrese una latitud maxima:  ")
        listas, cantidad = controller.coordenadas(cont, longitudMinima, longitudMaxima, latitudMinima, latitudMaxima)
        print("============ Respuesta Requerimiento 5 ============")
        print("Hay", cantidad, "diferentes avistamiento en esta  area")
        print("Los primeros 5 y los untimos 5 avistamientos en este tiempo son :")
        imprimirLongitud(listas)

    elif int(inputs[0]) == 8:
        longitudMinima = input("ingrese una longitud minima:  ")
        longitudMaxima = input("ingrese una longitud maxima. ")
        latitudMinima = input("ingrese una latitud minima:  ")
        latitudMaxima = input("ingrese una latitud maxima: ")
        listas, cantidad = controller.coordenadas(cont, longitudMinima, longitudMaxima, latitudMinima, latitudMaxima)
        print("============ Respuesta Requerimiento 6 ============")
        print("Hay ", cantidad, " diferentes avistamiento en esta  area")
        print("Los primeros 5 y los ultimos 5 avistamientos en este tiempo son :")
        imprimirLongitud(listas)
        guardarMapa(listas, longitudMinima, latitudMinima)