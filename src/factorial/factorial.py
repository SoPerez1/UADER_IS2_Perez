#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        return "No existe"
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

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

for n in range(start, end + 1):
    print(f"Factorial {n}! es {factorial(n)}")