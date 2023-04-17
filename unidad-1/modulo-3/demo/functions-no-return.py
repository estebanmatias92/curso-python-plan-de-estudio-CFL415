
print("\nFuncion que solo saluda por pantalla: ")
# Funcion sin parametro ni retorno
def saludar():                      # Definiendo la funcion, No tiene parametros
    print("Saludando a todos!\n")     # No retorna nada, solo muestra por pantalla

saludar()                           # Usando la funcion





print("\nFuncion que comprueba si un numero es par o impar: ")
# Función sin return
def comprobar_paridad(numerito):    # Definicnedo la funcion, tiene un parametro
    if numerito %2 == 0:
        print(f"El numero {numerito} es par!\n")
    else:    
        print(f"El numero {numerito} es impar!\n")

comprobar_paridad(5)                # Usando la funcion, pasando el valor 5 como argumento
