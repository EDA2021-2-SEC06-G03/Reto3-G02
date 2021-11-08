"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from DISClib.Algorithms.Sorting.mergesort import sort
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m
import datetime


assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos
def newAnalyzer():
    """ Inicializa el analizador
    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas
    Retorna el analizador inicializado.
    """
    analyzer = {'avistamiento': None,
                'dateIndex': None,
                'dateIndex': None,
                'duracionS': None,
                'duracionHM': None}

    analyzer['avistamiento'] = lt.newList('SINGLE_LINKED', compare)

    analyzer['dateIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    analyzer['city'] = om.newMap(omaptype='RBT',
                                 comparefunction=compare)

    analyzer['longitude'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    analyzer['duracionS'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    analyzer['duracionHM'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    return analyzer


def addAvistamiento(analyzer, avistamiento):
    """
    """
    lt.addLast(analyzer['avistamiento'], avistamiento)
    updateDateIndex(analyzer['dateIndex'], avistamiento)
    updateCity(analyzer['city'], avistamiento)
    updateLongitude(analyzer['longitude'], avistamiento)
    updateDuracion(analyzer['duracionS'],avistamiento)
    updateDuracionHM(analyzer['duracionHM'],avistamiento)
    return analyzer
def addDuracionIndex(datentry, avistamiento):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstavistamiento']
    lt.addLast(lst, avistamiento)
    return datentry


def updateDateIndex(map, avistamiento):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    datetimes = avistamiento['datetime']
    fechaavistamiento = datetime.datetime.strptime(datetimes, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, fechaavistamiento.date())
    if entry is None:
        datentry = newDataEntry(avistamiento)
        om.put(map, fechaavistamiento.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, avistamiento)
    return map


def updateCity(cities, avistamiento):
    city = avistamiento['city']
    entry = om.get(cities, city)
    if entry is None:
        cityentry = newCityEntry()
        om.put(cities, city, cityentry)
    else:
        cityentry = me.getValue(entry)
    AddCity(cityentry, avistamiento)
    return city


def updateLongitude(longitudes, avistamiento):
    longitud = round(float(avistamiento['longitude']), 2)
    entry = om.get(longitudes, longitud)
    if entry is None:
        longitudentry = newLongitudeEntry(longitud)
        om.put(longitudes, longitud, longitudentry)
    else:
        longitudentry = me.getValue(entry)
    AddLongitude(longitudentry, avistamiento)
    return longitud
def updateDuracion(map, avistamiento):
    duracion = float(avistamiento['duration (seconds)'])
    entry = om.get(map, duracion)
    if entry is None:
        datentry = newDataFechaS()
        om.put(map, duracion, datentry)
    else:
        datentry = me.getValue(entry)
    addDuracionIndex(datentry, avistamiento)
    return map

def updateDuracionHM(map, avistamiento):
    fechashoras = datetime.datetime.strptime(avistamiento['datetime'], '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, fechashoras.time())
    if entry is None:
        datentry = newDataFechaHM()
        om.put(map, fechashoras.time(), datentry)
    else:
        datentry = me.getValue(entry)
    addDuracionIndex(datentry, avistamiento)
    return map


def addDateIndex(datentry, avistamiento):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstavistamiento']
    lt.addLast(lst, avistamiento)
    avistamientoUFOIndex = datentry['avistamientoUFOIndex']
    offentry = m.get(avistamientoUFOIndex, avistamiento['datetime'])
    if (offentry is None):
        entry = nuevosavistamientosUFOS(avistamiento['datetime'], avistamiento)
        lt.addLast(entry['lsttiempos'], avistamiento)
        m.put(avistamientoUFOIndex, avistamiento['datetime'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lsttiempos'], avistamiento)
    return datentry


def AddCity(cityentry, avistamiento):
    lst = cityentry['ltavistamiento']
    lt.addLast(lst, avistamiento)

    return cityentry


def AddLongitude(longitudeEntry, avistamiento):
    latitudes = longitudeEntry['latitudes']
    latitude = round(float(avistamiento["latitude"]), 2)
    offentry = m.get(latitudes, latitude)
    if (offentry is None):
        entry = newLatitudeEntry(latitude)
        lt.addLast(entry['avistamientos'], avistamiento)
        m.put(latitudes, latitude, entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['avistamientos'], avistamiento)
    return longitudeEntry


def newDataEntry(avistamiento):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'avistamientoUFOIndex': None, 'lstavistamiento': None}
    entry['avistamientoUFOIndex'] = m.newMap(numelements=30,
                                             maptype='PROBING',
                                             comparefunction=compareUFOS)
    entry['lstavistamiento'] = lt.newList('SINGLE_LINKED', compare)
    return entry


def newCityEntry():
    entry = {'lstavistamiento': None}
    entry['ltavistamiento'] = lt.newList('SINGLE_LINKED', compare)
    return entry


def newLongitudeEntry(longitud):
    longitudEntry = {'longitud': longitud, 'latitudes': None}
    longitudEntry['latitudes'] = m.newMap(numelements=1000,
                                          maptype='PROBING',
                                          comparefunction=compareUFOS)
    return longitudEntry


def newLatitudeEntry(latitude):
    latitudeEntry = {'latitud': latitude, 'avistamientos': None}
    latitudeEntry['avistamientos'] = lt.newList('SINGLE_LINKED', compare)
    return latitudeEntry
def newDataFechaS():

    entry = {'lstavistamiento': None}
    entry['lstavistamiento'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def newDataFechaHM():

    entry = {'lstavistamiento': None}
    entry['lstavistamiento'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def nuevosavistamientosUFOS(nuevosUFO, avistamiento):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    UFO = {'avistamientoUFO': None, 'lsttiempos': None}
    UFO['avistamientoUFO'] = nuevosUFO
    UFO['lsttiempos'] = lt.newList('SINGLELINKED', compareUFOS)
    UFO['ltcity'] = lt.newList('SINGLELINKED', compareUFOS)
    return UFO


def totalAvistamientosCiudad(analyzer, city):
    lst = om.values(analyzer['city'], om.minKey(analyzer['city']), om.maxKey(analyzer['city'])) # 1
    entry = om.get(analyzer['city'], city) # 1
    ciudades = lt.size(lst) # 1
    cityentry = me.getValue(entry)
    cantidad = lt.size(cityentry["ltavistamiento"])
    listaordenada = ins.sort(cityentry["ltavistamiento"], cmpFechas)
    listas = lt.newList()
    primeros3 = lt.subList(listaordenada, 1, 3)
    ultimos3 = lt.subList(listaordenada, lt.size(listaordenada) - 2, 3)
    for avistamiento in lt.iterator(primeros3): # n
        lt.addLast(listas, avistamiento)        # n
    for avistamiento in lt.iterator(ultimos3): # n
        lt.addLast(listas, avistamiento)        # n

    return cantidad, listas, ciudades


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta
def AvistamientoSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer['avistamiento'])


def getAvistamientos(analyzer):
    """
    Retorna los avistamientos.
    """
    lst = om.values(analyzer['dateIndex'], om.minKey(analyzer['dateIndex']), om.maxKey(analyzer['dateIndex']))
    listas = lt.newList()
    primeros5 = lt.subList(lst, 1, 5)
    ultimos5 = lt.subList(lst, lt.size(lst) - 4, 5)
    for lstdate in lt.iterator(primeros5):
        lt.addLast(listas, lt.getElement(lstdate['lstavistamiento'], 1))
    for lstdate in lt.iterator(ultimos5):
        lt.addLast(listas, lt.getElement(lstdate['lstavistamiento'], 1))
    return listas


def getCity(analyzer):
    """
    Retorna los avistamientos.
    """
    lst = om.values(analyzer['city'], om.minKey(analyzer['city']), om.maxKey(analyzer['city']))
    return lst
def getAvistamientosSegundos(analyzer, minSegundos, maxSegundos):
    maxSegundos=float(maxSegundos)
    minSegundos=float(minSegundos)
    lst = om.values(analyzer['duracionS'], minSegundos, maxSegundos)
    lt.size(lst)# -> 3
    cantidad = 0
    dur_max = 0

    listaNueva = lt.newList()
    for node in lt.iterator(lst):   # segundos 14 - 20
        for avistamiento in lt.iterator(node['lstavistamiento']):        # 1990 - 1990
            lt.addLast(listaNueva, avistamiento)
            if float(avistamiento['duration (seconds)']) > dur_max:
                dur_max = float(avistamiento['duration (seconds)'])
        cantidad += lt.size(node['lstavistamiento'])

    listaOrdenada = ins.sort(listaNueva, cmpFechas)
    primeros3 = lt.subList(listaOrdenada, 1, 3)
    ultimos3 = lt.subList(listaOrdenada, lt.size(listaOrdenada) - 2, 3)

    listas = lt.newList()
    for avistamiento in lt.iterator(primeros3):
        lt.addLast(listas, avistamiento)
    for avistamiento in lt.iterator(ultimos3):
        lt.addLast(listas, avistamiento)

    return cantidad, dur_max, listas

def getAvistamientosHoras(analyzer, minHoras, maxHoras):
    lst = om.values(analyzer['duracionHM'], minHoras, maxHoras)
    lt.size(lst)# -> 3
    cantidad = 0
    dur_max = 0
    lst2 = om.values(analyzer['duracionHM'], om.minKey(analyzer['duracionHM']),om.maxKey(analyzer['duracionHM']))
    cantidad2= lt.size(lst2)
    listaNueva = lt.newList()
    for node in lt.iterator(lst):   # segundos 14 - 20
        for avistamiento in lt.iterator(node['lstavistamiento']):        # 1990 - 1990
            lt.addLast(listaNueva, avistamiento)
        cantidad += lt.size(node['lstavistamiento'])

    listaOrdenada = ins.sort(listaNueva, cmpFechas)
    primeros3 = lt.subList(listaOrdenada, 1, 3)
    ultimos3 = lt.subList(listaOrdenada, lt.size(listaOrdenada) - 2, 3)

    listas = lt.newList()
    for avistamiento in lt.iterator(primeros3):
        lt.addLast(listas, avistamiento)
    for avistamiento in lt.iterator(ultimos3):
        lt.addLast(listas, avistamiento)

    return cantidad, dur_max, listas,cantidad2

def getAvistamientosByRange(analyzer, initialDate, finalDate):
    lst = om.values(analyzer['dateIndex'], initialDate, finalDate)
    listaFechas = om.values(analyzer['dateIndex'], om.minKey(analyzer['dateIndex']), om.maxKey(analyzer['dateIndex']))
    fechas = lt.size(listaFechas)
    totufos = 0
    listaavistamientos = lt.newList() #O(1)
    for fecha in lt.iterator(lst): #O(n)
        totufos += lt.size(fecha['lstavistamiento']) #O(n)
        for avistamiento in lt.iterator(fecha['lstavistamiento']): #O(n2)
            lt.addLast(listaavistamientos, avistamiento)           #O(n2)

    # n2
    listaavistamientos = ins.sort(listaavistamientos, cmpFechas)

    listas = lt.newList()
    primeros5 = lt.subList(listaavistamientos, 1, 3)
    ultimos5 = lt.subList(listaavistamientos, lt.size(listaavistamientos) - 2, 3)
    for avistamiento in lt.iterator(primeros5):
        lt.addLast(listas, avistamiento)
    for avistamiento in lt.iterator(ultimos5):
        lt.addLast(listas, avistamiento)
    return listas, totufos, fechas


def avistamientosPorCoordenada(analyzer, longitudMinima, longitudMaxima, latitudMinima, latitudMaxima):
    # longitudes= om.values(analyzer['longitude'], longitudMinima, longitudMaxima)
    # longitudes = om.values(analyzer['longitude'], om.maxKey(analyzer['longitude']), om.minKey(analyzer['longitude']))
    longitudes = om.values(analyzer['longitude'], longitudMaxima, longitudMinima)
    #print(longitudes)
    listaavistamientos = lt.newList()

    for longitud in lt.iterator(longitudes):   #O(n)

        latitudes = mp.valueSet(longitud["latitudes"])
        for latitud in lt.iterator(latitudes):  #O(n2)

            if latitudMinima < latitud['latitud'] < latitudMaxima: #O(n2)
                for avistamiento in lt.iterator(latitud['avistamientos']): #O(n3)
                    lt.addLast(listaavistamientos, avistamiento)#O(n3)
    listaavistamientos = ins.sort(listaavistamientos, cmpFechas)

    if lt.size(listaavistamientos) > 10:
        listas = lt.newList()
        primeros5 = lt.subList(listaavistamientos, 1, 5)
        ultimos5 = lt.subList(listaavistamientos, lt.size(listaavistamientos) - 4, 5)
        for avistamiento in lt.iterator(primeros5):
            lt.addLast(listas, avistamiento)
        for avistamiento in lt.iterator(ultimos5):
            lt.addLast(listas, avistamiento)
    else:
        listas = listaavistamientos
    return listas, lt.size(listaavistamientos)


# Funciones utilizadas para comparar elementos dentro de una lista
def compare(element1, element2):
    """
    Compara dos elementos
    """
    if (element1 == element2):
        return 0
    elif element1 > element2:
        return 1
    else:
        return -1


def compareUFOS(ufo1, ufo2):
    """
    Compara dos tipos de crimenes
    """
    ufos = me.getKey(ufo2)
    if ufo1 == ufos:
        return 0
    elif ufo1 > ufos:
        return 1
    else:
        return -1


def cmpFechas(avistamiento1, avistamiento2):
    fecha1 = avistamiento1['datetime']
    fecha2 = avistamiento2['datetime']
    if fecha1 < fecha2:
        r = True
    else:
        r = False
    return r
def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
