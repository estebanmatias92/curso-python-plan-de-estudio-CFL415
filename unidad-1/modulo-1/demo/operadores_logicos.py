
# Ingrese edad en enteros
mi_edad = int(input("Ingrese su edad: "))
# Ingresar si soy estudiante
soy_estudiante = bool(int(input("Es estudiante: ")))

print("Soy mayor? ", (mi_edad > 18))  # Muestra el resultado de una expresion ed comparacion


soy_mayor_y_estudiante = (mi_edad >= 18) or soy_estudiante           # Una operacion logica AND que opera sobre dos expresiones "(mi_edad > 18)" y "soy_estudiante"
soy_mayor_o_estudiante = (mi_edad >= 18) and soy_estudiante           # Una operacion logica OR que opera sobre dos expresiones "(mi_edad > 18)" y "soy_estudiante"
NO_soy_mayor_y_estudiante = not ((mi_edad >= 18) and soy_estudiante)           # Una operacion logica NOT que opera sobre UNA expresiones "((mi_edad >= 18) and soy_estudiante)"


print("Soy mayor y estudiante? ", soy_mayor_y_estudiante)
print("Soy mayor o estudiante? ", soy_mayor_o_estudiante)
print("NO soy mayor y estudiante? ", NO_soy_mayor_y_estudiante)