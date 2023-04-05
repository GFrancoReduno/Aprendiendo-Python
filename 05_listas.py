#Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [13, 3, 7, 7, 69, 37, 23]

print(len(my_list))

my_other_list = [23, 1.81, "Parka"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
# print(my_other_list[-4]) #index error out of range
# print(my_other_list[3]) #index error out of range
print(my_list.count(7)) #cuenta la cantidad de veces que se repite el valor en una lista

age, height, name = my_other_list #tiene que tener la misma cantidad de variables que datos dentro de la lista si o si, ni uno mas ni uno menos sino da error
print(age)

print(my_list + my_other_list) #las listas solo se pueden sumar

my_other_list.append("Florencia") #agrega un objeto al final de la lista
print(my_other_list)

my_other_list.insert(1, "Lola") #agrega un objeto en la posicion que le indiques
print(my_other_list)

my_other_list[1] = "Perro"
print(my_other_list)

my_other_list.remove("Perro") #remueve un objeto que le indiques
print(my_other_list)

my_list.remove(7) #si los objetos se repiten al eliminar elimina al primero solamente
print(my_list)

print(my_list.pop()) #saca el ultimo de la lista
print(my_list)

del my_list[2] #elimina un elemento por indice
print(my_list)

my_new_list = my_list.copy() #copia la lista en una nueva

my_list.clear() #borra todos los elementos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #da vuelta el orden de los indices en la lista
print(my_new_list)

my_new_list.sort() #ordena de menor a mayor
print(my_new_list)

print(my_new_list[1:3]) 

my_list = "Florencia" #cambiar de lista a string
print(my_list)
print(type(my_list))




