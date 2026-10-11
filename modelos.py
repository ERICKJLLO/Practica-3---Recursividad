class SecuenciaADN:
    def __init__(self, identificador, nombre_muestra, secuencia, nivel_riesgo):
        self.identificador = identificador
        self.nombre_muestra = nombre_muestra
        self.secuencia = secuencia
        self.nivel_riesgo = nivel_riesgo

    def __str__(self):
        return (
            f"ID: {self.identificador} | Muestra: {self.nombre_muestra} | "
            f"ADN: {self.secuencia} | Riesgo: {self.nivel_riesgo}"
        )


class Nodo:
    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.siguiente = None


class ListaADN:
    def __init__(self):
        self.cabeza = None

    def agregar(self, secuencia):
        nuevo_nodo = Nodo(secuencia)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        self._agregar_al_final(self.cabeza, nuevo_nodo)

    def _agregar_al_final(self, nodo, nuevo_nodo):
        if nodo.siguiente is None:
            nodo.siguiente = nuevo_nodo
            return
        self._agregar_al_final(nodo.siguiente, nuevo_nodo)

    def esta_vacia(self):
        return self.cabeza is None
