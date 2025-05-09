# Main del sistema operativo

from process import Proceso
from memory_manager import GestorMemoria
from scheduler import Planificador
import time

def main():
    memoria = GestorMemoria(tamano_total=1024)
    planificador = Planificador(quantum=1)

    # Crear procesos
    procesos = [
        Proceso(pid=1, tamanio=300, tiempo_cpu=4),
        Proceso(pid=2, tamanio=250, tiempo_cpu=3),
        Proceso(pid=3, tamanio=512, tiempo_cpu=5),
        Proceso(pid=4, tamanio=128, tiempo_cpu=2),
    ]

    # Intentar asignarlos a memoria
    for p in procesos:
        if memoria.asignar(p):
            print(f"✅ Proceso {p.pid} asignado a memoria.")
            planificador.agregar_proceso(p)
        else:
            print(f"❌ Proceso {p.pid} NO pudo ser asignado.")

    memoria.mostrar_memoria()
    print("\n🕒 Iniciando ejecución de procesos...\n")

    # Simulación de ejecución
    while not planificador.esta_vacio():
        proceso = planificador.siguiente_proceso()
        if proceso:
            proceso.ejecutar(quantum=planificador.quantum)
            print(proceso)

            if proceso.terminado():
                memoria.liberar(proceso)
                print(f"🧹 Proceso {proceso.pid} finalizado y memoria liberada.")
            else:
                planificador.replanificar(proceso)

            memoria.mostrar_memoria()
            time.sleep(1)

if __name__ == "__main__":
    main()
