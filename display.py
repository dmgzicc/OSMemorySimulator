from tabulate import tabulate

def mostrar_tabla_procesos(procesos, tick_actual):
    tabla = []
    for p in procesos:
        tabla.append([
            p.pid,
            p.estado,
            p.tamanio,
            p.tiempo_cpu,
            p.tiempo_restante
        ])

    headers = ["PID", "Estado", "Tamaño", "CPU Total", "CPU Restante"]
    print(f"\n📋 Estado de los procesos (Tick: {tick_actual})")
    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
