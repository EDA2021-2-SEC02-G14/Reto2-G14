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
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadObras(catalog)
    loadArtistas(catalog)
    loadNacionalidades(catalog)

def loadObras(catalog):
    archivo_obras = cf.data_dir + 'Artworks-utf8-small.csv'

    input_file = csv.DictReader(open(archivo_obras, encoding='utf-8'))

    for obra in input_file:
        model.addObra(catalog,obra)

def loadArtistas(catalog):
    archivo_Artistas = cf.data_dir + 'Artists-utf8-small.csv'

    input_file = csv.DictReader(open(archivo_Artistas, encoding='utf-8'))

    for artista in input_file:
        model.addArtistas(catalog,artista)

def loadNacionalidades(catalog):
    archivo_naciones = cf.data_dir + 'Artworks-utf8-small.csv'

    input_file = csv.DictReader(open(archivo_naciones, rncoding = 'utf-8'))

    for nacion in input_file:
        model.addnacion(catalog,nacion)
        




# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def obrasSize (catalog):

    return model.obrasSize(catalog)

def artistaSize (catalog):
    
    return model.artistaSize(catalog)