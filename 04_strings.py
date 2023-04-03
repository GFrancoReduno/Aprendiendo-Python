#Strings

my_string = "Mi string"
my_other_string = "Mi otra string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "este es un string\ncon salto de linea"  # "\n" salto de linea
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación" # "\t" tabulación
print(my_tab_string)

my_scape_string = "\\t este es un string \\n escapado" # "\\" escapado
print(my_scape_string)


#Formateo

name, surname, age = "Florencia", "Caponera", 22

print("Mi novia se llama {} {} y su edade es {}".format(name,surname, age)) #Manera formatear sos re capo
print("Mi novia se llama %s %s y su edade es %d" %(name, surname,age))
print("Mi novia se llama " + name + " " + surname + " y su edad es " + str(age)) #Manera incorrecta que sos pete 
print(f"Mi novia se llama {name} {surname} y su edade es {age}") #Otra manera correcta de formatear

"""
amor_de_mi_vida = "Florencia Caponera"
te_amo = "Tornillos <3"

"""

#Desempaquetado de caracteres

language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
