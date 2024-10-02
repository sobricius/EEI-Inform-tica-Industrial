import json

from maquina import Maquina

#Clase
class Instalacion:
    #Constructor
    def __init__(self,nombre,fichero):
        self.__nombre=nombre
        self.__fichero=fichero
        self.__maquinas= {}
        datos = json.load(open(fichero,encoding='utf8'))
        for maquina in datos['maquinas']:
            self.anademaquina(maquina,datos['maquinas'][maquina])


    def anademaquina(Maquina):
