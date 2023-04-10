#sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario

my_other_set = {"Lola", "Florencia", "Parka", 23}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add(("Pelada")) #un set no es una estructura ordenada
print(my_other_set) 

my_other_set.add(("Lola")) #un set no admite repetidos
print(my_other_set)

print("Lola" in my_other_set)
print("Doly" in my_other_set)

my_other_set.remove ("Pelada")
print(my_other_set)

my_other_set.clear() #vacia los elementos dentro del set
print(len(my_other_set))

del my_other_set #borra el objeto
#print(my_other_set)

my_set = {"Lola","Florencia","Parka", 23}
my_list = list(my_set)

print(my_list)
print(my_list[0])

my_other_set = {"Cod", "Valorant", "Lol"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Música"}))

print(my_new_set.difference(my_set)) #muestra los elementos diferentes
