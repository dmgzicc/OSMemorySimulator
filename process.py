class Proceso:
    ESTADOS = ["Nuevo", "Listo", "Ejecutando", "Bloqueado", "Terminado"]

    def __init__(self, pid, tamanio, tiempo_cpu, prioridad=0):
        self.pid = pid
        self.tamanio = tamanio          # Memoria que necesita en MB
        self.tiempo_cpu = tiempo_cpu    # Tiempo que necesita en ticks
        self.prioridad = prioridad
        self.estado = "Nuevo"
        self.tiempo_restante = tiempo_cpu

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in Proceso.ESTADOS:
            self.estado = nuevo_estado

    def ejecutar(self, quantum=1):
        """Simula la ejecución del proceso por una unidad de tiempo."""
        if self.estado != "Ejecutando":
            self.estado = "Ejecutando"

        self.tiempo_restante -= quantum
        if self.tiempo_restante <= 0:
            self.estado = "Terminado"

    def terminado(self):
        return self.estado == "Terminado"

    def __str__(self):
        return (f"[PID: {self.pid} | Estado: {self.estado} | "
                f"Tamaño: {self.tamanio}MB | Tiempo restante: {self.tiempo_restante}]")
