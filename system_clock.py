class RelojSistema:
    def __init__(self):
        self.tick = 0

    def avanzar(self):
        self.tick += 1

    def tiempo_actual(self):
        return self.tick

    def __str__(self):
        return f"🕒 Tick actual: {self.tick}"
