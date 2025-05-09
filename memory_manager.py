class BloqueMemoria:
    def __init__(self, inicio, tamanio, pid=None):
        self.inicio = inicio
        self.tamanio = tamanio
        self.pid = pid  # None indica que está libre

    def esta_libre(self):
        return self.pid is None

    def __str__(self):
        estado = "Libre" if self.esta_libre() else f"Ocupado por PID {self.pid}"
        return f"[{estado} | Inicio: {self.inicio} | Tamaño: {self.tamanio}]"


class GestorMemoria:
    def __init__(self, tamano_total):
        self.tamano_total = tamano_total
        self.bloques = [BloqueMemoria(0, tamano_total)]  # Toda la memoria libre al inicio

    def asignar(self, proceso):
        for i, bloque in enumerate(self.bloques):
            if bloque.esta_libre() and bloque.tamanio >= proceso.tamanio:
                nuevo_bloque = BloqueMemoria(bloque.inicio, proceso.tamanio, proceso.pid)
                bloques_restantes = bloque.tamanio - proceso.tamanio

                if bloques_restantes > 0:
                    bloque_restante = BloqueMemoria(bloque.inicio + proceso.tamanio, bloques_restantes)
                    self.bloques[i:i+1] = [nuevo_bloque, bloque_restante]
                else:
                    self.bloques[i] = nuevo_bloque

                return True  # Asignación exitosa

        return False  # No hay espacio suficiente

    def liberar(self, proceso):
        for i, bloque in enumerate(self.bloques):
            if bloque.pid == proceso.pid:
                bloque.pid = None  # Liberar
                self._fusionar_bloques()
                return True
        return False

    def _fusionar_bloques(self):
        i = 0
        while i < len(self.bloques) - 1:
            actual = self.bloques[i]
            siguiente = self.bloques[i + 1]
            if actual.esta_libre() and siguiente.esta_libre():
                actual.tamanio += siguiente.tamanio
                del self.bloques[i + 1]
            else:
                i += 1

    def mostrar_memoria(self):
        print("\n📦 Estado actual de la memoria:")
        for bloque in self.bloques:
            print(" ", bloque)
