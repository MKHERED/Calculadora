
from Function.funct import calc, Tiempo, kill
import time, threading

def __main__():
    global lista, hilo_tiempo
    lista = list()

    Var = str(input("\n introdusca la opercacion: "))
    lista.append(Var)

    Var = int(input("\n introdusca el primer numero: "))
    lista.append(Var)

    Var = int(input("\n introdusca el segunda numero: "))
    lista.append(Var)

    #print("que contiene la lista: {}, cuantos itens hay en la lista: {}".format(lista, len(lista)))

    calc(lista[1], lista[2], lista[0])
    
    hilo_tiempo = threading.Thread(target = Tiempo)
    hilo_tiempo.start()
    kill.kill(hilos=hilo_tiempo)
    __main__()        
    pass

__main__()