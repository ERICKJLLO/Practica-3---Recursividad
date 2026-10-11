from modelos import ListaADN


def contar_patron_en_texto(texto, patron, posicion=0):
    if patron == "":
        return 0
    if posicion + len(patron) > len(texto):
        return 0
    ocurrencia = 1 if texto[posicion:posicion + len(patron)] == patron else 0
    return ocurrencia + contar_patron_en_texto(texto, patron, posicion + 1)


def contar_patron(lista, patron, nodo=None, resultados=None):
    if nodo is None:
        return _contar_patron_desde_nodo(lista.cabeza, patron, [])
    return _contar_patron_desde_nodo(nodo, patron, resultados)


def _contar_patron_desde_nodo(nodo, patron, resultados):
    if nodo is None:
        return resultados
    resultados.append(
        (
            nodo.secuencia.identificador,
            contar_patron_en_texto(nodo.secuencia.secuencia, patron),
        )
    )
    return _contar_patron_desde_nodo(nodo.siguiente, patron, resultados)


def promedio_riesgo(lista):
    total, cantidad = _sumar_riesgos(lista.cabeza, 0, 0)
    if cantidad == 0:
        return 0
    return total / cantidad


def _sumar_riesgos(nodo, total, cantidad):
    if nodo is None:
        return total, cantidad
    return _sumar_riesgos(
        nodo.siguiente,
        total + nodo.secuencia.nivel_riesgo,
        cantidad + 1,
    )


def generar_subcadenas(secuencia, longitud, posicion=0, resultado=None):
    if resultado is None:
        resultado = []
    if longitud <= 0 or posicion + longitud > len(secuencia):
        return resultado
    resultado.append(secuencia[posicion:posicion + longitud])
    return generar_subcadenas(secuencia, longitud, posicion + 1, resultado)


def comparar_a_y_t(secuencia, posicion=0):
    if posicion == len(secuencia):
        return 0, 0
    cantidad_a, cantidad_t = comparar_a_y_t(secuencia, posicion + 1)
    if secuencia[posicion] == "A":
        cantidad_a += 1
    elif secuencia[posicion] == "T":
        cantidad_t += 1
    return cantidad_a, cantidad_t


def resultado_comparacion_a_t(secuencia):
    cantidad_a, cantidad_t = comparar_a_y_t(secuencia)
    if cantidad_a > cantidad_t:
        return "Tiene más A que T."
    if cantidad_t > cantidad_a:
        return "Tiene más T que A."
    return "Tiene igual cantidad de A y T."


def mutar_secuencia(secuencia):
    if secuencia == "":
        return "", 0
    resto_mutado, mutaciones = mutar_secuencia(secuencia[1:])
    nucleotido = secuencia[0]
    if nucleotido == "A":
        return "T" + resto_mutado, mutaciones + 1
    if nucleotido == "T":
        return "A" + resto_mutado, mutaciones + 1
    return nucleotido + resto_mutado, mutaciones


def buscar_por_criterios(
    lista,
    riesgo_minimo,
    longitud_minima,
    patron,
    nodo=None,
):
    if nodo is None:
        return _buscar_desde_nodo(
            lista.cabeza,
            riesgo_minimo,
            longitud_minima,
            patron,
        )
    return _buscar_desde_nodo(
        nodo,
        riesgo_minimo,
        longitud_minima,
        patron,
    )


def _buscar_desde_nodo(nodo, riesgo_minimo, longitud_minima, patron):
    if nodo is None:
        return None
    secuencia = nodo.secuencia
    cumple_riesgo = secuencia.nivel_riesgo >= riesgo_minimo
    cumple_longitud = len(secuencia.secuencia) >= longitud_minima
    cumple_patron = contar_patron_en_texto(secuencia.secuencia, patron) > 0
    if cumple_riesgo and cumple_longitud and cumple_patron:
        return secuencia
    return _buscar_desde_nodo(
        nodo.siguiente,
        riesgo_minimo,
        longitud_minima,
        patron,
    )


def eliminar_bajo_riesgo(lista, riesgo_minimo, nodo=None, anterior=None):
    if nodo is None:
        if anterior is None:
            nodo = lista.cabeza
        else:
            return
    if nodo is None:
        return
    if nodo.secuencia.nivel_riesgo < riesgo_minimo:
        if anterior is None:
            lista.cabeza = nodo.siguiente
            return eliminar_bajo_riesgo(lista, riesgo_minimo)
        anterior.siguiente = nodo.siguiente
        return eliminar_bajo_riesgo(lista, riesgo_minimo, anterior.siguiente, anterior)
    return eliminar_bajo_riesgo(lista, riesgo_minimo, nodo.siguiente, nodo)
