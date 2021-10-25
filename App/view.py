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
import sys
import controller
from DISClib.ADT import list as lt
assert cf

UFOfile = 'UFOS-utf8-small.csv'
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
        print('fecha y hora: ',avistamiento['datetime'])
        print('ciudad: ',avistamiento['city'])
        print('estado: ' ,avistamiento['state'])
        print('país: '  ,avistamiento['country'])
        print('forma: '  ,avistamiento['shape'])
        print('duración en segundos : '  ,avistamiento['duration (seconds)'])
        print('duración en horas : '  ,avistamiento['duration (hours/min)'])
        print('comentarios : '  ,avistamiento['comments'])
        print('dia postead : '  ,avistamiento['date posted'])
        print('latitud: '  ,avistamiento['latitude'])
        print('longitud : '  ,avistamiento['longitude'])
    print()

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- Req1, Contar los avistamientos en una ciudad")
    print("4- Req2, Contar los avistamientos por duración")
    print("5- Req3, Contar avistamientos por Hora/Minutos del día")
    print("6- Req4. Contar los avistamientos en un rango de fechas")
    print("7- Req5, Contar los avistamientos de una Zona Geográfica")

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
        listaAvistamientos=controller.getAvistamientos(cont)
        imprimirAvistamiento(listaAvistamientos)

    elif int(inputs[0]) == 3:
        pass

    else:
        sys.exit(0)
sys.exit(0)
