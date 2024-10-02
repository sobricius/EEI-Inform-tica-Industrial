from datetime import *


#Clase
class Maquina:

    #Constructor
    def __init(self,identificador, horas)
        self.__identificador=identificador
        self.__horas=horas
        self.__libre=True
        self.__inicio=None


    #Metodo Marcha
    def Marcha(self):
        if self.__libre == True:
            raise exception('Error, ya esta en marcha la maquina', self.__identificador)
        self.__inicio= datetime.now()
        self.__libre=False



    #Metodo Paro
    def Paro(self):
        if self.__libre == False:
            raise Exception('Error, ya esta en marcha la maquina', self.__identificador)
        self.__horas= self.__horas + datetime.now()-self.__inicio
        self.__libre=True


    #getter de horas
    def getHoras(self):
        return self.__horas


    #getter de estado
    def getEstado(self):
        return self.__libre
