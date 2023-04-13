#Conditionals

my_condition = False 

if my_condition: #es lo mismo que if my_condition == True:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

    
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: #condicion extra (else if)
    print("Es igual a 25")
else: #si no se cumple la condicion
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")



print("La ejecucion continua")


my_string = ""

if not my_string: #niega la condicion 
    print("my cadena de texto esta vacia")

if my_string == "mi cadena de textoooo":
    print("estas cadenas de texto coinciden")












