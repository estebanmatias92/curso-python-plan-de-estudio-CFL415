# Se puede dejar los valores en una variable, algo flexible pero mejorable
millas = 100
millas_hora = 60

# O se puede pedir los valores directamente al usuario, algo mucho mas flexible y mas general
#millas = float(input("Ingrese millas recorridas: "))               
#millas_hora = float(input("Ingrese velocidad en millas: "))


horas = round(millas / millas_hora, 2)          # Divido millas por velocidad, guardo el resultado decimal
minutos = (horas - int(horas) ) * 60            # A eso le resto el entero y multiplico la parte decimal por 60
segundos = (minutos - int(minutos)) * 60        # A eso le vuelvo a sacar el entero y multiplico la parte decimal por 60

horas = int(horas)                              # Ya que tengo las horas, minutos y segundos guardados
minutos = int(minutos)                          # convierto todo a enteros para mostrarlo por pantalla
segundos = int(segundos)

print(f"{horas}:{minutos}:{segundos}")          # Muestro el timer en formato hora:minuto:segundo