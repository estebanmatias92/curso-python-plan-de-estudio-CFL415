
#
# Funcion que toma un numero ENTERO y devuelve la cantidad de digitos
#
# Parametros:
#   (int) num
#
# Retorno:
#   (int) count
#
def count_digits(num):

    count = 0

    while num:
        count += 1
        num //= 10

    return count


#
# Funcion que toma un numero, INT o FLOAT, comprueba si es par y retorna un booleano
#
# Parametros:
#   (int/float) num
#
# Retorno:
#   (bool) 
#
def is_even(num):
    return num % 2 == 0


#
# Funcion que toma un numero, INT o FLOAT, comprueba si es impar y retorna un booleano
#
# Parametros:
#   (int/float) num
#
# Retorno:
#   (bool) 
#
def is_odd(num):
    return num % 2 != 0


#
# Funcion que toma un STRING como parametro, comprueba si es vocal y devuelve un valor BOOLEANO
#
# Parametros:
#   (str) cadena
#
# Retorno:
#   (bool)
#
def is_vowel(cadena):
    minuscula = cadena.lower()
    return (minuscula in "aeiou") or (minuscula in "áéíóú")