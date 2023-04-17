
# Ingresar texto con mi nombre
nombre_apellido = input("Ingrese su nombre: ")
# Ingresar si soy estudiante
soy_estudiante = bool(int(input("Es estudiante: ")))
# Ingrese edad en enteros
mi_edad = int(input("Ingrese su edad: "))
# Ingresar salario
mi_salario = float(input("Ingrese su salario: "))


print("Nombre: ", nombre_apellido)
print("Estudio?: ", soy_estudiante)
print("Edad: ", mi_edad)
print("Salario: ", mi_salario)

print(type(nombre_apellido))
print(type(soy_estudiante))
print(type(mi_edad))
print(type(mi_salario))


print("Soy mayor? ", (mi_edad > 18))


soy_mayor_y_estudiante = (mi_edad > 18) or soy_estudiante

print("Soy mayor y estudiante? ", soy_mayor_y_estudiante)