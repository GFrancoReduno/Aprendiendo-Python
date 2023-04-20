#Functions

def my_function ():
    print("Esto es una funcion")

my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(3,5)
sum_two_values("Lola","Pelada")
sum_two_values(3.5, 5.3)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_results = sum_two_values(11, 7)
print(my_results)

my_results = sum_two_values_with_return(9, 3)
print(my_results)


def print_name (name, surname):
    print(f"{name} {surname}")

print_name("Parka","Violeta")
print_name(surname = "Parka",name = "Violeta")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Parka", "Violeta", "Parkimetro")
print_name_with_default("Parka", "Violeta")

def print_upper_texts(*texts): #el * hace que se puedan poner infinitos parametros
    for text in texts:
        print(text.upper())

print_upper_texts("Hi","Hello","Hola")
print_upper_texts("Hi")