# **************************************************************
# *  ESTRUCTURA DEL SWITCH - MATCH / CÓDIGO PRINCIPAL PYTHON   *
# ------------------------------------------------------------
# *  Realizar un programa que, por medio del número del mes,   *
# *  indique el nombre del mes que le corresponde.             *
# **************************************************************

# *************** INICIO DEL PROGRAMA *************************

print("*")
print("*      PROGRAMA QUE MUESTRA EL MES DEL AÑO        *")
print("*")

# Entrada
num = int(input("Digite un número del 1 al 12: "))

# Proceso / Estructura MATCH - CASE
match num:
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4:
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Diciembre")
    case _:
        print("Número inválido. Debe estar entre 1 y 12.")

# Salida final
print("*")
print("*     FINALIZÓ EL PROGRAMA CON ÉXITO              *")
print("*\n")