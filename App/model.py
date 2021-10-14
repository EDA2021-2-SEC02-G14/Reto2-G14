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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = { 'obras' : None,
                'artistas' : None,
                'years' : None,
                'Nacionality' : None}

    catalog['obras'] = lt.newList()

    catalog['artistas'] = mp.newMap(100.000,
                                     maptype='PROBING', 
                                     loadfactor = 0.5,  
                                     comparefunction= compareArtistName)

    catalog['years'] = mp.newMap(100, 
                                maptype='CHAINING', 
                                loadfactor=4.0, 
                                comparefunction=compareMapYear)

    catalog ['Nacionality'] = mp.newMap(194,
                                        maptype='CHAINING',
                                        loadfactor= 4.0,
                                        comparefunction= compareNation)

    return catalog



# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    author = {'name': "",
              "books": None,
              "average": 0,
              "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('SINGLE_LINKED', compareArtistName)
    return author

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def addObra(catalog,obra):
    lt.addLast(catalog['obras'],obra)
    mp.put(catalog['obras'],obra['artworks'],obra)
    artistas = obra['obras'].split(",")


def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0

def compareArtistName(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareNation(nacionality,tag):
    tagentry = me.getKey(tag)
    if(nacionality == tagentry):
        return 0
    elif (nacionality > tagentry):
        return 1 
    else: 
        return -1 

def addDepartment(catalog, department):
    lt.addLast(catalog['Department'], department)
    mp.put(catalog['Department'], department)

def getDepartment(catalog, Department):
    Department = mp.get(catalog['Department'], Department)
    if Department:
        return me.getValue(Department)['Department']
    return None 

def getObraNacion(catalog, nacionality):
    nacion = mp.get(catalog['Nacionality'], nacionality)
    if nacion:
        return me.getValue(nacion)
    return None

def obrasSize(catalog):
    return mp.size(catalog['obras'])

def artistaSize (catalog):
    return mp.size(catalog['artistas'])
