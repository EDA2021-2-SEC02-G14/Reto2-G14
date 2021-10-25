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
    catalog = { 'Artists' : None,
                'Artworks' : None,
                'years' : None,
                'ArtistasTipo':None,
                'Nacionality' : None,
                'ArtworksIds': None}

    catalog['Artworks'] = lt.newList('SINGLE_LINKED', compareObrasIds)
    
    
    catalog['Artists'] = lt.newList('SINGLE_LINKED', compareObrasIds)


    catalog['years'] = mp.newMap(150.000,
                                    maptype = 'CHAINING',
                                    loadfactor=0.3,
                                    comparefunction=compareObrasIds)

    catalog['ObrasDates'] = mp.newMap(16.000,
                                     maptype='PROBING', 
                                     loadfactor = 4.0,  
                                     comparefunction= compareArtistName)

    catalog['ArtistasTipo'] = mp.newMap(100, 
                                maptype='PROBING', 
                                loadfactor=4.0, 
                                comparefunction=compareMapYear)

    catalog ['Nacionality'] = mp.newMap(194,
                                        maptype='PROBING',
                                        loadfactor= 4.0,
                                        comparefunction= compareNation)

    catalog ['Departamentos'] = mp.newMap(200,
                                        maptype='PROBING',
                                        loadfactor= 4.0,
                                        comparefunction= compareNation)

    return catalog



#
# Crear
#

def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    author = {'name': "",
              "artworks": None,
              "average": 0,
              "average_rating": 0}
    author['name'] = name
    author['Artworks'] = lt.newList('SINGLE_LINKED', compareArtistName)
    return author

def newObraTag(name,  id):
    """
    crea relacion entre tag y obra
    """
    tag = {'name':'',
           'tag_id':'',
           'total_obras': 0,
           'Artworks': None,
           'count': 0.0}
    tag['name']= name
    tag['tag_id'] = id
    tag['Artworks'] = lt.newList()
    return tag

#
# Agregar
#

def addObra(catalog,obra):
    """
    Adiciona obra a la lista
    """
    lt.addLast(catalog['Artworks'], obra)
    mp.put(catalog['ObjectID'],obra['Title'],obra)
    artistas = obra['Artists'].split(",")
    for artista in artistas:
        addObraAutor(catalog, artista.strip(),obra)
    addObraAnio(catalog, obra)

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
def addObraAutor(catalog, artistName, obra):

    artistas = catalog['Artists']
    existe = mp.contains(artistas,artistName)
    if existe:
        entry = mp.get(artistas,  artistName)
        artista = me.getValue(entry)
    else: 
        artista = newAuthor(artistName)
        mp.put(artistas, artistName,  artista)
    lt.addLast(artistas['Artworks'],obra)
    artista['average'] += float (obra['Classification'])
    totObras = lt.size(artista['Artworks'])
    if(totObras > 0 ): 
        artista['Classification'] = artista ['average'] / totObras

def addObraAnio(catalog,  obra):
    try:
        years = catalog['years']
        if(obra['Date'] != ''):
            puYear = obra['Date']
            puYear = int(float(puYear))
        else:
            puYear = 2020
        existe = mp.contains(years, puYear)
        if existe:
            entry = mp.get(years,  puYear)
            year = me.getValue(entry)
        else: 
            year = newYear (puYear)
            mp.put(years, puYear, year)
        lt.addLast(year['Artworks'],  obra)
    except Exception:
        return None

def newYear(yearP):
    entry = {'year' : "", "obra": None}
    entry['year'] = yearP
    entry['Artworks']= lt.newList('SINGLE_LINKED',  compareYears)
    return entry

#
# Consulta
#

def getObraAutor (catalog, artistaName):
    artista = mp.get(catalog['Artists'], artistaName)
    if artista:
        return me.getValue(artista)
    return None


def getObraNacion(catalog, nacionality):
    nacion = mp.get(catalog['Nacionality'], nacionality)
    if nacion:
        return me.getValue(nacion)
    return None

def getObraAnio(catalog, year):
    year = mp.get(catalog['years'], year)
    if year:
        return me.getValue(year)['Artworks']
    return None 

def req3(catalog, name):
    nombre = catalog ['ConstituentID']
    if nombre == name:
        print("")
    return

#
# Tamaños
#

def obrasSize(catalog):
    return mp.size(catalog['Artworks'])

def artistaSize (catalog):
    return mp.size(catalog['Artists'])

def nacionalitySize(catalog):
    return mp.size(catalog['Nacionality'])

#
# Comparaciones
#

def compareNation(nacionality,tag):
    tagentry = me.getKey(tag)
    if(nacionality == tagentry):
        return 0
    elif (nacionality > tagentry):
        return 1 
    else: 
        return -1 

def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0

def compareObrasIds (id1,  id2):
    if (id1 == id2):
        return 0
    elif id1 > id2: 
        return 1
    else:
        return-1

def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0