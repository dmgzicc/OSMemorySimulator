class Proceso:
    def __init__(self, pid, tamanio, tiempo_cpu):
        self.pid = pid
        self.tamanio = tamanio
        self.tiempo_cpu = tiempo_cpu
        self.tiempo_restante = tiempo_cpu
        self.estado = "Nuevo"
        self.tiempo_llegada = None
        self.tiempo_finalizacion = None
        self.tiempo_espera = 0

    def ejecutar(self, quantum=1):
        self.tiempo_restante -= quantum
        if self.tiempo_restante <= 0:
            self.tiempo_restante = 0
            self.estado = "Terminado"
        else:
            self.estado = "Ejecutando"

    def cambiar_estado(self, nuevo_estado):
        if self.estado == "Listo" and nuevo_estado == "Listo":
            self.tiempo_espera += 1
        self.estado = nuevo_estado

    def terminado(self):
        return self.tiempo_restante <= 0

    def __str__(self):
        return f"🧾 Proceso {self.pid} | Estado: {self.estado} | Restante: {self.tiempo_restante}"
