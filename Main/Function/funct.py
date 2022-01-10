import math, threading, sys
from time import sleep

class Tiempo():
    def __init__(self):
        for i in range(11):
            sleep(1)
            i = i + 1
            print(i)
            if i == 10:
                kill.kill(bools=True)
                
            pass
    
class kill():    
    def kill(bools, hilos):
        if bools == True:
            threading.Thread.setDaemon(hilos, daemonic=True)
            print("YA")
        pass

class p():
    def __init__(self, var):
        print("\n" + "{}".format(var))
        pass

class calc():
    def __init__(self, a, b, tipe):
        self.tipe = tipe
        if str(self.tipe) == str("suma"):
            Var = (a + b)
            p(Var)

        elif str(self.tipe)== str("resta"):
            Var =(a - b)
            p(Var)
            
        elif str(self.tipe) == str("division"):
            Var = str(input("tipo de division flotante o entero?: "))

            if Var == str("flotante"):
                Var=(a // b)
                p(Var)
                
            elif Var == str("entero"):
                Var = (a / b)
                p(Var)

            else:
                print("division no encontrada")
                pass

        elif str(self.tipe) == str("cos"):
            Var = math.cos(a)
            p(Var)
        
        elif str(self.tipe) == str("sen"):
            Var = math.sin(a)
            p(Var)

        elif str(self.tipe) == str("tan"):
            Var = math.tan(a)
            p(Var)
        
        elif str(self.tipe) == str("tan neg"):
            Var = math.atan(a)
            p(Var)

        elif str(self.tipe) == str("cos neg"):
            Var = math.acos(a)
            p(Var)

        elif str(self.tipe) == str("sen neg"):
            Var = math.asin(a)
            p(Var)


        else:
            print("no se encontro la funcion")
            pass

        print("\n Todos los datos: {}, {}, {}".format(a, b, tipe))
        
        pass
    
    