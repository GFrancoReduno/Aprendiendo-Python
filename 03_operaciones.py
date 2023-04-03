# Operadores #

print(3 + 5) #suma
print(3 - 5) #resta
print(3 * 5) #multiplicación
print(3 / 5) #division
print(10 % 3) #resto de division
print(10 // 3) #flor division aproxima a un numero entero
print(2 ** 3) #eleva el primer numero por el segundo
print(2 * 3 + 5 / 10 ** 3 - 15) #operacion combinada

print("Lola" + " pelada pompín") #concatena palabras
# print("Lola" + 5) #no se puede concatenar strings con enteros
print("Lola" + str(5)) #cambiando el tipo a string ya se puede hacer
print("Lola" * 3) #se repite el string la cantidad de veces multiplicada
print("Lola" * (2 ** 3)) #se repite el string por la cantidad resultante de la potencia
# print("Lola" * 2.3) #no se puede multiplicar un string por un numero decimal

#si creamos una variable con la multiplicacion de un numero decimal dejandolo en entero y transformamos esa variable en int podriamos resolver usando decimales y enteros

decimal = 2.5 * 2
print("Lola" * int(decimal))

#Operadores comparativos

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4) 
print(3 == 4)
print(3 != 4)
