#Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (23, 1.81, "Parka", "Parka")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[-5]) index error
#print(my_tuple[5]) index error

print(my_tuple.count("Parka"))
print(my_tuple.index("Parka"))

#my_tuple[1] = 1.83 NO SE PUEDE MODIFICAR LOS OBJETOS DENTRO DE LA TUPLA

my_sum_tuple = my_tuple + my_other_tuple #se pueden sumar
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)  #se pueden realizar cambios en la tupla transformandola en lista
print(type(my_tuple))

my_tuple [2] = "Florencia"
my_tuple.insert(3, "Lola")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple)) #volvemos a transformar en tuple y se vuelve inmutable

#del my_tuple[2] #TypeError: 'tuple' object doesn't support item deletion

del my_tuple 
#print(my_tuple) #NameError: name 'my_tuple' is not defined


