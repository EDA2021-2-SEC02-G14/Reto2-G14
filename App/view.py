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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- inicializar el catálogo")
    print("2- Cargar informacion del catálogo")
    print("3- Numero de  obras por nacionalidad")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando wey perate toy chiquito... :3")
        controller.loadData(cont)

        print("Cargando información de los archivos ....")
        print('Obras cargadas: ' + str(controller.obrasSize(cont)))
        print('Autores cargados: ' + str(controller.artistaSize(cont)))
        
    elif int(inputs[0]) ==3:
        nacion = input("Buscando nacionalidades?: ")
        resultado = controller.getNacionality(cont, nacion)
        print(resultado)


    else:
        sys.exit(0)
sys.exit(0)
