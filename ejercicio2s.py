# ******************************************************
# *              Código principal de Python            *
# *     Estructura simulada del ciclo DO - WHILE       *
# ******************************************************

# desarrollar un programa que permita seleccionar por consola una opción
# y se muestre una lista de opciones (menú)

while True:
    print("\n*")
    print("*                 MENÚ PRINCIPAL                 *")
    print("*")
    print("*   Digite la letra A para Actualizar Sistema     *")
    print("*   Digite la letra E para Eliminar Catálogo      *")
    print("*   Digite la letra C para Crear Productos        *")
    print("*   Digite la letra S para salir del programa     *")
    print("*")

    letra = input("\nDigite la letra: ").upper()

    if letra == "S":
        print("\nSe finalizó con éxito\n")
        break
    else:
        print("\nSigue dentro del proceso del DO WHILE\n")

print("\nEl DO WHILE ha finalizado\n")a
