
print("\nBucle WHILE mostrando par o impar: ")
# Bucle while
i = 1

while i <= 5:                       # Iterar desde el numero 1 hasta el 5
    if i % 2 == 0:                  # Comprobar paridad en cada iteracion
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
    i += 1                           # Aumenta el contador, la proxima iteracion tendra el valor actualizado de "i"




print("\nPrograma con bucle WHILE que ingresa nombres por teclado y espera un 0 para salir: ")
# Este codigo pedira por teclado el ingreso de nombres hasta que se ingrese 0, entonces sale
while True:                         # Este True siempre va a ser True por lo tanto siempre itera, a menos que lo corten
    nombre = input("Ingresa un nombre o 0 para salir: ")        
    if nombre == "0":               # Comprobar si es "0"
        break                       # Sentencia que permite cortar bucles y salir
    print(nombre)