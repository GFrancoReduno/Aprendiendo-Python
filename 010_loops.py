#Loops / Bucles #

# While

my_condition = 0

while my_condition < 10: #es un if pero infinito
    print(my_condition)
    my_condition += 2
else: #es opcional
    print("mi condicion es mayor o igual que 10")

print("la ejecucion continua")

while my_condition < 20:
    my_condition += 2
    if  my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)


print("la ejecucion continua")

#FOR

my_list = ["Pedro", "Carlos", "FLorencia", "Franco","Lola", "Teodore"]

for element in my_list:
    print(element)

my_tuple = (23, 1.81, "Parka", "Parka")

for element in my_tuple:
    print(element)

my_set = {"Lola", "Florencia", "Parka", 23}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Parka", "Apellido":"Violeta", "Edad":23, 1:"Python"}

for element in my_dict:
    print(element)

for element in my_dict.values():
    print(element)
    if element == "Edad":    
        break #frena el for
    print("se ejecuta")
else:
    print("el bucle for ha terminado")

print("La ejecucion continua")

for element in my_dict.values():
    print(element)
    if element == "Edad":    
        continue #continua el for
    print("se ejecuta")
else:
    print("el bucle for ha terminado")
