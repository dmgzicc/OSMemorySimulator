class Planificador:
    def __init__(self, quantum=1):
        self.cola_listos = []
        self.quantum = quantum

    def agregar_proceso(self, proceso):
        """Agrega un proceso a la cola de listos."""
        proceso.cambiar_estado("Listo")
        self.cola_listos.append(proceso)

    def siguiente_proceso(self):
        """Devuelve el siguiente proceso a ejecutar."""
        if self.cola_listos:
            proceso = self.cola_listos.pop(0)
            proceso.cambiar_estado("Ejecutando")
            return proceso
        return None

    def esta_vacio(self):
        return len(self.cola_listos) == 0

    def replanificar(self, proceso):
        """Devuelve el proceso a la cola si no ha terminado (como en Round Robin)."""
        if not proceso.terminado():
            proceso.cambiar_estado("Listo")
            self.cola_listos.append(proceso)
