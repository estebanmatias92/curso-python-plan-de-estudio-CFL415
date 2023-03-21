

print("\nPrograma con IF que comprueba que un dato sea solo alfabetico: ")
# If
mi_nombre = "Matias"

if mi_nombre.isalpha():                                     # .isalpha() comprueba que un string sea solo alfabetico
    print("El valor de mi_nombre es solo alfabetico\n")




print("\nPrograma con IF-ELSE que comprueba que un dato sea igual a otro: ")
# If - Else
otro_nombre = "Jorge"

if mi_nombre == otro_nombre:                                # Comprobar igualdad
    print("Ambos nombres son iguales\n")
else:
    print("Ambos nombres NO son iguales\n")





print("\nPrograma con IF-ELIF-ELSE que comprueba que dos datos numeros sean negativos o positivos: ")
# If - Elif - Else
one = 5
two = 10

if one > 0 and two > 0:                                     # Comprobar mayor que cero
    print("Ambos números son positivos\n")
elif one < 0 and two < 0:                                   # Comprobar menor que cero
    print("Ambos números son negativos\n")
else:
    print("Uno de los números es positivo y el otro es negativo\n")