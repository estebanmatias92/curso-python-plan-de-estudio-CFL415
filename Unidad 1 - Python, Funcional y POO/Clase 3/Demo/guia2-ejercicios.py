import math

# Comprobar si un numero es Primo

# Pasos

num = int(input("Ingrese un numero natural: "))
es_primo = True                                                 # Asumir que el numero puede ser primo, comprobar lo contrario

print("")

if (num < 2):                                                   # Si es menor a 2, entonces es primo
    es_primo = False
elif (num > 2 and num % 2 == 0):                                # Si es mayor a 2 y divisible por 2, entonces no es primo
    es_primo = False
else:
    raiz_num = math.ceil(math.sqrt(num))                        # Obtengo la raiz de "num" 

    for i in range(3, raiz_num, 2):                             # Desde 3 hasta la raiz cuadrada de "num", pasando por todos los impares
        if (num % i == 0):                                      # Comprobar si "num" es divisible por alguno de los impares
            es_primo = False                                    # Si lo es, entonces no era primo
            break

if (es_primo):                                                  # Si llegamos hasta aca, sin caer en las anteriores condiciones, entonces es primo
    print("El numero es primo!")
else:
    print("El numero no es primo :(")