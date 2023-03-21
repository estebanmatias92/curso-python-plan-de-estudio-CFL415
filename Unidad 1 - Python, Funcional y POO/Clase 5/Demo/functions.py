

# Funcion sin parametro ni retorno
def saludar():                      # Definiendo la funcion, No tiene parametros
    print("Salundo a todos!\n")     # No retorna nada, solo muestra por pantalla

saludar()                           # Usando la funcion, no necesita pasar argumentos


# Función sin return
def comprobar_paridad(numerito):    # Definicnedo la funcion, tiene un parametro
    if numerito %2 == 0:
        print(f"El numero {numerito} es par!\n")
    else:    
        print(f"El numero {numerito} es impar!\n")

comprobar_paridad(5)                # Usando la funcion, pasando el valor 5 como argumento



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