lola = "pelada"
patas = 4
pelada = True

print(lola)

#Variables en una sola linea

nombre, apellido, alias, edad = "Lola", "Reduno", "pelada pompín", 8
print("Mi perra se llama", nombre, apellido, "tiene", edad, "años y es mejor conocida como", alias)

"""
#input = datos para que uno complete

nombre = input("Cúal es el nombre de mi perra?")
edad = input("Cúal es la edad de mi perra?")

print(nombre)
print(edad)

"""

#Cambiamos el tipo de valor

nombre = 8
edad = "Lola"

print(nombre)
print(edad)

#¿Forzar tipo de dato?

dirección: str = "Mi dirección"
dirección = 32
dirección = False
dirección = 1.5 
print(type(dirección))