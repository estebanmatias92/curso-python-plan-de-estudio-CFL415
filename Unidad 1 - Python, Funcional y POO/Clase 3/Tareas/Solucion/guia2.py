#
# Ejercicio 1
#
print("\nComprobar si un numero es PAR o IMPAR")
numero_del_usuario = input("Ingrese un numero: ")       # Pido primero al usuario un numero (es devuelto como string)
numero_del_usuario = int(numero_del_usuario)            # Convierto el valor alfanumerico que me dio el usuario, a numero

if ((numero_del_usuario % 2) == 0):                     # Primero compruebo SI es par
    print("El numero que ingresaste fue par")           # Si es par, entra aca
else:                                                   
    print("El numero que ingresaste no fue par")        # Si no es par, entra aca



#
# Ejercicio 2
#
print("\n\nEncontrar el mayor de DOS numeros")
numero1 = int(input("Te pido que me des un numero: "))
numero2 = int(input("Te pido que me des otro numero: "))

if (numero1 > numero2):
    print(f"El numero {numero1} es mayor al numero {numero2}")
elif (numero1 == numero2):
    print(f"El numero {numero1} es igual al numero {numero2}")
else:
    print(f"El numero {numero1} es menor al numero {numero2}")



#
# Ejercicio 3
#
print("\n\nEncontrar el mayor de TRES numeros")
numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))
numero3 = int(input("Ingrese el tercer numero entero: "))

mayor = numero1

if (numero1 > numero2 and numero1 > numero3):             # Si numero1 es mayor que el resto
    mayor = numero1
elif (numero2 > numero1 and numero2 > numero3):           # Sino, si el numero2 es mayor que el resto
    mayor = numero2
else:                                                   # Por descarte si ninguno de los anteriores es mayor, queda como mayor el numero3
    mayor = numero3

print(f"El numero mayor: {mayor}")



#
# Ejercicio 4
#



#
# Ejercicio 5
# 
print("\n\nComprobar vocales o consonantes")
caracter = input("Ingrese una vocal o consonante: ")    # Primero pido el dato


if (len(caracter) > 1):                                 # Compruebo que sea solo un caracter el ingresado
    print("Ingresaste mal, volve a intentar")
else:                                                   # Si esta bien, compruebo vocal y consonante
    if (caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"):
        print("El caracter ingresado es vocal!")
    elif (caracter.isalpha()):
        print("El caracter ingresado es consonante!")
    else:
        print("El caracter ingresado es simbolo o numero :(")



#
# Ejercicio 7
#
print("\n\nTabla Multiplicar (FOR)")
num = int(input("Ingrese el numero para generar la tabla: "))
for i in range(1, 11):
    multiplo = i * num 
    print(f"{num} x {i} = {multiplo}")


print("\nTabla Multiplicar (WHILE)")
num = int(input("Ingrese el numero para generar la tabla: "))
i = 1
while (i < 11):
    multiplo = i * num
    print(f"{num} x {i} = {multiplo}")
    i = i + 1



#
# Ejercicio 11
#
