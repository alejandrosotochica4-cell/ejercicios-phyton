# **************************************************************
# *        ESTRUCTURA DE WHILE - CÓDIGO PRINCIPAL DE PYTHON    *
# ------------------------------------------------------------
# *  Realizar un programa en el que la variable se ejecute     *
# *  mientras el número sea diferente de 0.                    *
# *  Se debe leer un número por consola y analizar si es par   *
# *  o impar hasta que el usuario digite 0.                    *
# **************************************************************

# *************** INICIO DEL PROGRAMA *************************

# Entrada / Inicialización
num = 1   # Se inicializa la variable con un valor diferente de 0

# Proceso / Ciclo WHILE
while num != 0:
    print("\n*")
    print("*              ANÁLISIS DE NÚMEROS                *")
    print("*")
    num = int(input("Digite un número (0 para salir): "))

    # Condicional para determinar si es par o impar
    if num == 0:
        print("\nHa digitado 0, se finalizará el programa.\n")
    elif num % 2 == 0:
        print("El número es PAR\n")
    else:
        print("El número es IMPAR\n")

# Salida
print("*")
print("*          FINALIZÓ EL PROGRAMA CON ÉXITO         *")
print("*\n")