import threading
import time
from unicodedata import name

class Fibonacci():

    def __init__(self):
        self.lock= threading.Lock()
        self.num1= 0
        self.num2=1
        self.suma=1
        print(self.num1)

    def step(self):
        self.lock.acquire()

        try:
            time.sleep(0.5)
            print(self.suma)
            self.suma = self.num1 + self.num2
            self.num1 = self.num2
            self.num2 = self.suma

        finally:
            self.lock.release()    

def funct_fibo(fibonacci, lenght):
    for x in range(lenght-1):
        fibonacci.step()

if __name__ == "__main__":
    size= input("Ingrese el tamaño de la Serie Fibonacci:  ")
    if(int(size)>0):
        fibonacci= Fibonacci()
        hilo= threading.Thread(target= funct_fibo, args=(fibonacci, int(size)))
        hilo.start()
    else:
        print("ingrese un dato entero mayor a 0")   