#Diccionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre":"Parka", "Apellido":"Violeta", "Edad":23, 1:"Python"}

my_dict = {
    "nombre":"Parka",
    "Apellido":"violeta",
    "Edad":23,
    "Lenguajes": {"Python","Javascript","html"},
    1:1.81
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["nombre"])

my_dict["nombre"] = "Torni"
print(my_dict["nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle falsa 123" #agregar nuevo campo al diccionario
print(my_dict)

del my_dict["Calle"] #Eliminar elementos del diccionario
print(my_dict)

print("Parka" in my_dict) #false xq busca por keys y no por valores
print("nombre" in my_dict) #true esta es la forma correcta

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["nombre", 1, "piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("nombre", 1, "piso")) #otra manera de crear un diccionario
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict) #crea nuevo diccionario copiando las claves antiguas
print((my_new_dict)) 
my_new_dict = dict.fromkeys(my_dict, "Parka") #mete un valor en todas las keys
print((my_new_dict)) 

my_values = my_new_dict.values() #diccionario de valores
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys())) #manera rebuscada de hacer un diccionario de valores
print(tuple(my_new_dict))
print(set(my_new_dict))











