# main.py — Simulador básico de Sistema Operativo

from process import Proceso
from memory_manager import GestorMemoria
from scheduler import Planificador
from system_clock import RelojSistema
from display import mostrar_tabla_procesos
from tabulate import tabulate
import time

def main():
    memoria = GestorMemoria(tamano_total=1024)
    planificador = Planificador(quantum=1)
    reloj = RelojSistema()

    # Crear procesos
    procesos = [
        Proceso(pid=1, tamanio=300, tiempo_cpu=4),
        Proceso(pid=2, tamanio=250, tiempo_cpu=3),
        Proceso(pid=3, tamanio=112, tiempo_cpu=5),
        Proceso(pid=4, tamanio=128, tiempo_cpu=2),
    ]

    # Asignar procesos a memoria y registrar tiempo de llegada
    for p in procesos:
        if memoria.asignar(p):
            print(f"✅ Proceso {p.pid} asignado a memoria.")
            p.tiempo_llegada = reloj.tiempo_actual()
            planificador.agregar_proceso(p)
        else:
            print(f"❌ Proceso {p.pid} NO pudo ser asignado (memoria insuficiente).")

    memoria.mostrar_memoria()
    print("\n🕒 Iniciando ejecución de procesos...\n")

    # Simulación de ejecución basada en ticks
    while not planificador.esta_vacio():
        print(reloj)  # Mostrar el tick actual

        proceso = planificador.siguiente_proceso()
        if proceso:
            proceso.ejecutar(quantum=planificador.quantum)
            print(proceso)

            if proceso.terminado():
                proceso.tiempo_finalizacion = reloj.tiempo_actual()
                memoria.liberar(proceso)
                print(f"🧹 Proceso {proceso.pid} finalizado y memoria liberada.")
            else:
                planificador.replanificar(proceso)

            memoria.mostrar_memoria()
        
        # Mostrar tabla de estado de procesos
        mostrar_tabla_procesos(procesos, reloj.tiempo_actual())

        # Avanzar el reloj
        reloj.avanzar()
        time.sleep(1)

    # Mostrar métricas finales
    print("\n📈 Métricas de rendimiento por proceso:\n")

    tabla_metricas = []
    for p in procesos:
        turnaround = (
            p.tiempo_finalizacion - p.tiempo_llegada
            if p.tiempo_finalizacion is not None else "-"
        )
        tabla_metricas.append([
            p.pid,
            p.tiempo_llegada,
            p.tiempo_finalizacion,
            p.tiempo_espera,
            turnaround
        ])

    headers = ["PID", "Llegada", "Finalización", "Espera", "Turnaround"]
    print(tabulate(tabla_metricas, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
