

# If
mi_nombre = "Matias"

if mi_nombre.isalpha():                                     # .isalpha() comprueba que un string sea solo alfabetico
    print("\nEl valor de mi_nombre es solo alfabetico\n")




# If - Else
otro_nombre = "Jorge"

if mi_nombre == otro_nombre:                                # Comprobar igualdad
    print("Ambos nombres son iguales\n")
else:
    print("Ambos nombres NO son iguales\n")





# If - Elif - Else
one = 5
two = 10

if one > 0 and two > 0:                                     # Comprobar mayor que cero
    print("Ambos números son positivos\n")
elif one < 0 and two < 0:                                   # Comprobar menor que cero
    print("Ambos números son negativos\n")
else:
    print("Uno de los números es positivo y el otro es negativo\n")