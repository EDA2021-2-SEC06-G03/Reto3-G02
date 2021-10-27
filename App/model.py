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


from App.controller import AvistamientoSize
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
                'dateIndex': None
                }

    analyzer['avistamiento'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['dateIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    analyzer['City'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareCity)
    return analyzer

def addAvistamiento(analyzer, Avistamiento):
    """
    """
    lt.addLast(analyzer['avistamiento'], Avistamiento)
    updateDateIndex(analyzer['dateIndex'], Avistamiento)
    updatecity(Avistamiento,analyzer['City'])
    return analyzer

def updateDateIndex(map, avistamiento):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    datetimes = avistamiento['datetime']
    fechaAvistamiento = datetime.datetime.strptime(datetimes, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, fechaAvistamiento.date())
    if entry is None:
        datentry = newDataEntry(avistamiento)
        om.put(map, fechaAvistamiento.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, avistamiento)
    return map
def updatecity(avistamiento,cities):
    city = avistamiento['city']
    entry = om.get(cities,city )
    if entry is None:
        cityentry = newCityEntry()
        om.put(cities,city, cityentry)
    else:
        cityentry = me.getValue(entry)
    AddCity(cityentry, avistamiento)
    return city

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
def AddCity(cityentry,avistamiento):
    lst = cityentry['ltavistamiento']
    lt.addLast(lst, avistamiento)
    
    return cityentry

def newDataEntry(avistamiento):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'avistamientoUFOIndex': None, 'lstavistamiento': None}
    entry['avistamientoUFOIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareUFOS)
    entry['lstavistamiento'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry
def newCityEntry():
    entry = { 'lstavistamiento': None}
    entry['ltavistamiento'] = lt.newList('SINGLE_LINKED', compareCity)
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

def totalAvistamientosCiudad(analyzer,city):
    lst = om.values(analyzer['City'],om.minKey(analyzer['City']),om.maxKey(analyzer['City']))
    entry = om.get(analyzer['City'],city )
    cityentry = me.getValue(entry)
    cantidad=lt.size(cityentry["ltavistamiento"])
    listaordenada= ins.sort(cityentry["ltavistamiento"],cmpFechas)
    listas=lt.newList()
    primeros3= lt.subList(listaordenada,1,3)
    ultimos3=lt.subList(listaordenada,lt.size(listaordenada)-2,3)
    for avistamiento in lt.iterator(primeros3):
        lt.addLast(listas,avistamiento)
    for avistamiento in lt.iterator(ultimos3):
        lt.addLast(listas,avistamiento)

    #for avistamiento in lt.iterator(cityentry["lstavistamiento"]):
    return cantidad,listas



    

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
    lst = om.values(analyzer['dateIndex'],om.minKey(analyzer['dateIndex']),om.maxKey(analyzer['dateIndex']))
    listas=lt.newList()
    primeros5= lt.subList(lst,1,5)
    ultimos5=lt.subList(lst,lt.size(lst)-4,5)
    for lstdate in lt.iterator(primeros5):
        lt.addLast(listas,lt.getElement(lstdate['lstavistamiento'],1))
    for lstdate in lt.iterator(ultimos5):
        lt.addLast(listas,lt.getElement(lstdate['lstavistamiento'],1))
    return listas
def getCity(analyzer):
    """
    Retorna los avistamientos.
    """
    lst = om.values(analyzer['City'],om.minKey(analyzer['City']),om.maxKey(analyzer['City']))
    return lst

def getCrimesByRange(analyzer, initialDate, finalDate):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    lst = om.values(analyzer['dateIndex'], initialDate, finalDate)
    totufos = 0
    for lstdate in lt.iterator(lst):
        totufos += lt.size(lstdate['lstavistamientos'])
    return totufos


def getCrimesByRangeCode(analyzer, initialDate, offensecode):
    """
    Para una fecha determinada, retorna el numero de crimenes
    de un tipo especifico.
    """
    UFOdate = om.get(analyzer['dateIndex'], initialDate)
    if UFOdate['key'] is not None:
        offensemap = me.getValue(UFOdate)['avistamientoUFOIndex']
        numoffenses = m.get(offensemap, offensecode)
        if numoffenses is not None:
            return m.size(me.getValue(numoffenses)['lsttiempos'])
    return 0
# Funciones utilizadas para comparar elementos dentro de una lista

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


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
def compareCity(city1, city2):
    """
    Compara dos fechas
    """
    if (city1 == city2):
        return 0
    elif (city1 > city2):
        return 1
    else:
        return -1
    
def compareUFOS(ufo1, ufo2):
    """
    Compara dos tipos de crimenes
    """
    ufos = me.getKey(ufo2)
    if (ufo1 == ufos):
        return 0
    elif (ufo1 > ufos):
        return 1
    else:
        return -1
def cmpFechas(avistamiento1, avistamiento2):
    fecha1 = avistamiento1['datetime']
    fecha2 = avistamiento2['datetime']
    if fecha1 < fecha2:
        r=True 
    else:
        r = False
    return r

# Funciones de ordenamiento
