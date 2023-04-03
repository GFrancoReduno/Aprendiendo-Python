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
print(3 >= 3) 
print(3 == 4)
print(3 != 4) 
print(3 < 4 > 5) #se pueden combinar

print("AAAA" > "aaaa") #ordenacion alfabetica por ASCII
print("Lola" < "Perro")
print("Lola" >= "Perro")
print("Lola" <= "Perro")
print("Lola" == "Perro")
print("Lola" != "Perro")

#Operadores logicos

print(3 > 4 and "Florencia" > "Lola") # el "AND" es un "y" en este caso falso y falso = falso
print(3 > 4 or "Florencia" > "Lola") # el "OR" es un "O" en este caso es falso o falso = falso
print(3 < 4 and "Florencia" < "Lola") #verdadero y falso = verdadero
print(3 < 4 or "Florencia" > "Lola") #verdadero o falso es = verdadero
print(3 < 4 or ("Florencia" > "Lola" and 4 == 4)) #combinadas primero se resuelve el parentesis entre falso o verdadero que da verdadero y despues se resuelve lo demas y queda verdadero o verdadero = verdadero
print(not(3 > 4)) #el "NOT" es una negacion en este caso seria falso pero lo convierte en verdadero xq esta negando


