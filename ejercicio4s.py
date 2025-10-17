# **************************************************************
# *       ESTRUCTURA DEL FOR - CÓDIGO PRINCIPAL DE PYTHON      *
# ------------------------------------------------------------
# *  Crear un programa que solicite la cantidad de números     *
# *  que el usuario va a digitar y calcule el acumulado (suma) *
# *  de todos ellos.                                           *
# **************************************************************

# *************** INICIO DEL PROGRAMA *************************

# Entrada
suma = 0  # Se crea la variable global para acumular los valores
print("*")
print("*     PROGRAMA QUE SUMA VARIOS NÚMEROS (FOR)     *")
print("*")

cantidad = int(input("Digite la cantidad de números para sumar: "))

# Proceso / Ciclo FOR
# range(cantidad) repite desde 0 hasta cantidad - 1
for i in range(cantidad):
    print("\nDigite el número " + str(i + 1) + ": ")
    numero = int(input())
    suma = suma + numero

# Salida
print("\n*")
print("La sumatoria total es: " + str(suma))
print("*\n")

# ******************** FIN DEL PROGRAMA ************************