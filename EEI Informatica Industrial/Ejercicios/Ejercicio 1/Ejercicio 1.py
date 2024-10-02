
horas =  [530,682,258,662,310,405,118,684,473,829]
libres = [False,False,False,True,False,False,False,False,False,False]
minHoras = float('inf')
selMaquina = 0

for maquina in range(len(libres)):
    if libres[maquina] == True:
        if minHoras >= horas[maquina]:
            minHoras = horas[maquina]
            selMaquina = maquina + 1
if selMaquina == 0:
    print('No hay ninguna maquina libre')
else:
    print('Se seleccionara la maquina', selMaquina )

