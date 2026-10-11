from modelos import ListaADN, SecuenciaADN
from operaciones import (
    buscar_por_criterios,
    contar_patron,
    eliminar_bajo_riesgo,
    generar_subcadenas,
    mutar_secuencia,
    promedio_riesgo,
    resultado_comparacion_a_t,
)


def pedir_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Debe ingresar un número entero.")
        return pedir_entero(mensaje)


def registrar_secuencia(lista):
    identificador = input("ID: ")
    nombre = input("Nombre de muestra: ")
    secuencia = input("Secuencia de ADN: ").upper()
    riesgo = pedir_entero("Nivel de riesgo: ")
    lista.agregar(SecuenciaADN(identificador, nombre, secuencia, riesgo))
    print("Secuencia registrada.")


def ejecutar_menu(lista):
    print("\n--- ANÁLISIS DE SECUENCIAS DE ADN ---")
    print("1. Registrar secuencia")
    print("2. Contar patrón")
    print("3. Promedio de riesgo")
    print("4. Generar subcadenas")
    print("5. Comparar A y T")
    print("6. Mutar secuencia")
    print("7. Buscar por criterios")
    print("8. Eliminar bajo riesgo")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "0":
        print("Programa finalizado.")
        return
    if opcion == "1":
        registrar_secuencia(lista)
    elif opcion == "2":
        patron = input("Patrón: ").upper()
        print(contar_patron(lista, patron))
    elif opcion == "3":
        print(f"Promedio de riesgo: {promedio_riesgo(lista)}")
    elif opcion == "4":
        secuencia = input("Secuencia: ").upper()
        longitud = pedir_entero("Longitud de las subcadenas: ")
        print(generar_subcadenas(secuencia, longitud))
    elif opcion == "5":
        secuencia = input("Secuencia: ").upper()
        print(resultado_comparacion_a_t(secuencia))
    elif opcion == "6":
        secuencia = input("Secuencia: ").upper()
        mutada, cantidad = mutar_secuencia(secuencia)
        print(f"Mutada: {mutada}")
        print(f"Mutaciones: {cantidad}")
    elif opcion == "7":
        riesgo = pedir_entero("Riesgo mínimo: ")
        longitud = pedir_entero("Longitud mínima: ")
        patron = input("Patrón: ").upper()
        resultado = buscar_por_criterios(lista, riesgo, longitud, patron)
        print(resultado if resultado is not None else "No se encontró una secuencia.")
    elif opcion == "8":
        riesgo = pedir_entero("Eliminar riesgos menores que: ")
        eliminar_bajo_riesgo(lista, riesgo)
        print("Eliminación completada.")
    else:
        print("Opción inválida.")
    ejecutar_menu(lista)


if __name__ == "__main__":
    ejecutar_menu(ListaADN())
