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

