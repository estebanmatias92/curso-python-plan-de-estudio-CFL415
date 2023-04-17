

print("\nBucle FOR mostrando par o impar: ")
# Bucle for
for i in range(1, 6):               # Usar range para generar lista de numeros a recorrer, desde el 1 hasta el 5
    if i % 2 == 0:                  # Usar el modulo 2 de i para comprobar si es par o no
        print(f"{i} es par")
    else:
        print(f"{i} es impar")




print("\nBucle FOR saltando de a 2 numeros: ")                           
# Bucle for con inicio, final y paso
for i in range(1, 10, 2):           # El rango tiene un inicio, un final y un paso al que debe ir
    print(i)                        # Mostrar linea por linea cada numero




print("\nBucle FOR en reveresa: ")                           
# Bucle for en reversa
for i in range(-10, 1):         # El ultimo argumento asigna un valor negativo al paso
    print(i)                        # Mostrar linea por linea cada numero




# Este código calculará la suma de los números del 1 al 10 y la imprimirá en pantalla.
print("Suma acumulativa: ")
suma = 0

for i in range(1, 11):
    suma = suma + i
    
print(suma)




# Este código imprimirá cada carácter de la cadena "Hola mundo" en una línea separada.
cadena = "Hola mundo"

for i in cadena:
    print(caracter)