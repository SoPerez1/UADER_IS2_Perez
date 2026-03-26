#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial:OOP.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        pass

    def calcular_individual(self, n):
        if n < 0: 
            return "No existe"
        elif n == 0: 
            return 1
        else: 
            fact = 1
            while(n > 1): 
                fact *= n 
                n -= 1
            return fact 

    def run(self, min, max):
        for n in range(min, max + 1):
            resultado = self.calcular_individual(n)
            print(f"Factorial {n}! es {resultado}")


if len(sys.argv) < 2:
    firstNum = input("Ingrese el número o rango (ej: 4-8, -10, 5-): ")
else:
    firstNum = sys.argv[1]

if "-" in firstNum:
    part = firstNum.split("-")
    
    if part[0] == "":
        start = 1
        end = int(part[1])
    elif part[1] == "": 
        start = int(part[0])
        end = 60
    else: 
        start = int(part[0])
        end = int(part[1])
else:
    start = end = int(firstNum)

f = Factorial()
f.run(start, end)