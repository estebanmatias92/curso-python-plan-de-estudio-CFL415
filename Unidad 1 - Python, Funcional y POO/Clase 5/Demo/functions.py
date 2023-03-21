
print("\nFuncion de suma con 3 parametros: ")
# Funcion que tiene 3 parametros, osea, que toma 3 argumentos y devuelve su suma
def sumar(num1, num2, num3):
    return num1 + num2 + num3

print("Resultado: ", sumar(3, 3, 3))                      # Sumando numeros
print("Resultado: ", sumar("Soy ", "un ", "String!"))     # Concatenando strings                 # Sumando numeros




print("\nFuncion que comprueba si un numero primo o no: ")
# Función con return
def es_primo(numero):               # Recibe como parametro "numero"
    if numero <= 1:                 # Comprueba que no sea menor o igual a 1
        return False                # En caso de ser asi retorna Falso
    for i in range(2, numero):      # Recorre de uno en uno, desde el numero 2 hasta "numero"
        if numero % i == 0:         # Usa el modulo contra cada i para comprobar que no sea divisible por ningun numero que le preceda
            return False            # Si es divisible retorna falso
    return True                     # Si no se pudo comprobar que NO fuera primo, retorna True


print(es_primo(2))      # Pasando como argumento el numero 2
print(es_primo(3))      # ...
print(es_primo(4))      # ...
print(es_primo(5))      # ...