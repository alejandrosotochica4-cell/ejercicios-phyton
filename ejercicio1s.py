# ********************************************
# Programa: Determinar si un número es positivo, negativo o neutro
# Autor: Alejandro José Soto Chica
# Ficha: 3287148
# Centro de Formación: SENA
# ********************************************


print("===========================================")
print("   PROGRAMA PARA IDENTIFICAR UN NÚMERO   ")
print("===========================================\n")


numero = int(input("👉 Digite un número: "))


if numero > 0:
    resultado = "El número es POSITIVO ✅"
elif numero == 0:
    resultado = "El número es NEUTRO ⚪"
else: 
    resultado = "El número es NEGATIVO ❌"

# ====== SALIDA ======
print("\n-------------------------------------------")
print("RESULTADO DEL ANÁLISIS:")
print(resultado)
print("-------------------------------------------")
print("Fin del programa. ¡Gracias por usarlo!")