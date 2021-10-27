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
 """

import config as cf
import model
import datetime
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

def loadData(analyzer, avistamientofile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    avistamientofile = cf.data_dir + avistamientofile
    input_file = csv.DictReader(open(avistamientofile, encoding="utf-8"),
                                delimiter=",")
    for avistamiento in input_file:
        model.addAvistamiento(analyzer, avistamiento)
    return analyzer

def AvistamientoSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.AvistamientoSize(analyzer)

# Funciones para la carga de datos
def getAvistamientos(analyzer):
    return model.getAvistamientos(analyzer)
def getcity(analyzer):
    return model.getCity(analyzer)
def updatecity(map,avistamiento,cities):
    return model.updatecity(map,avistamiento,cities)


def getCrimesByRange(analyzer, initialDate, finalDate):
    """
    Retorna el total de crimenes en un rango de fechas
    """
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    return model.getCrimesByRange(analyzer, initialDate.date(),
                                  finalDate.date())


def getCrimesByRangeCode(analyzer, initialDate,
                         offensecode):
    """
    Retorna el total de crimenes de un tipo especifico en una
    fecha determinada
    """
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    return model.getCrimesByRangeCode(analyzer, initialDate.date(),
                                      offensecode)
def totalAvistamientosCiudad(analyzer,city):
    return model.totalAvistamientosCiudad(analyzer,city)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
