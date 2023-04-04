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

 