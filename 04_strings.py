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

language = "python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-3]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#reverse

reversed_language = language [::-1]
print(reversed_language)


#Funciones

print(language.capitalize()) #pone mayuscula la primera letra
print(language.upper()) #pone mayuscula toda la palabra
print(language.count("t")) #cuenta cuantas letras ("x") hay en la palabra
print(language.isnumeric()) #te dice si es un numero con true or false
print("7".isnumeric()) 
print(language.lower()) #pone todas las letras en minusculas
print(language.upper().isupper()) #te dice si la palabra esta en mayusculas
print(language.startswith("py")) #te dice si la palabra empieza con ("x")
print("Py" == "py") # py con la primera minuscula no es lo mismo que Py con la primera mayuscula


