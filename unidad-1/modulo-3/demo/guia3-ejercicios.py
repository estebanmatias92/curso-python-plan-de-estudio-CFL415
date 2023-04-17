#
# Ejercicio 3
#
print("\n\n\nFuncion MAXIMO COMUN DIVISOR")

# Esta tomo dos argumentos, Calcula el MCD y devuelve un valor entero
def get_mcd(a, b):

    minimo = min(a, b)                                              # Obtengo el menor de ambos

    for i in range(minimo, 0, -1):                                  # Empiezo desde el menor y recorro hasta el 1
        if (a % i == 0) and (b % i == 0):                           # Compruebo si algun valor entre "minimo" y 1 es multiplo de ambos
            return i                                                # Si encuentro tal valor, lo retorno y salgo


# Pido por consola dos numeros
num1 = int(input("\nIngrese primer numero natural: "))
num2 = int(input("Ingrese segundo numero natural: "))

# Llamo a la funcion para que se ejecute y me devuelva el maximo comun divisor
MCD = get_mcd(num1, num2)

# Muestro los valores de esas variables en una oracion
print(f"El Maximo Comun Divisor entre {num1} y {num2} es: {MCD}")


"""
#
# Ejercicio 6
#
print("\n\n\nFuncion Comprobar Numero ARMSTRONG")

# Defino una funcion que toma un numero como parametro, verifica si es Armstrong y devuelve un valor booleano
def is_armstrong(num):

    if (num <= 0):                                                  # Primero que nada, compruebo que no sea cero o menor a cero
        return False                                                # Si es asi salgo

    i = num                                                         # Copio el valor en una variable nueva
    poweer = count_digits(num)                                      # Obtengo la cantidad de digitos en el numero
    suma = 0                                                        # Preparo la variable para la suma
    
    while i:                                                        # Itero mientras "i" no sea cero
        digit = (i % 10)                                            # Obtengo el digito 
        suma += (digit ** poweer)                                   # Suma el resultado del digito elevado a la cantidad de digitos   
        i //= 10                                                    # Actualizo el valor de "i" con los digitos restantes

    return (num == suma)                                            # Cuando el bucle termina, compruebo si el "num" original es igual a la suma de sus digitos y retorno el resultado booleano


# Pido por consola un numero entero
mi_numero = int(input("\nIngrese un numero entero: "))

# Llamo a la funcion para que se ejecute y me devuelva un valor booleano
es_armstrong = is_armstrong(mi_numero)

# Muestro los valores de esas variables
print(f"El numero {mi_numero} ", end="")
if (not es_armstrong):
    print(f"no ", end="")
print(f"es Armstrong")

"""