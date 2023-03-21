

# Bucle for
for i in range(1, 6):               # Usar range para generar lista de numeros a recorrer, desde el 1 hasta el 5
    if i % 2 == 0:                  # Usar el modulo 2 de i para comprobar si es par o no
        print(f"{i} es par")
    else:
        print(f"{i} es impar")




# Bucle while
i = 1
while i <= 5:                       # Iterar desde el numero 1 hasta el 5
    if i % 2 == 0:                  # Comprobar paridad en cada iteracion
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
    i +=1                           # Aumenta el contador, la proxima iteracion tendra el valor actualizado de "i"