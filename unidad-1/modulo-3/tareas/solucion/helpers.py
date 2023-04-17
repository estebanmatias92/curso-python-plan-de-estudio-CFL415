
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