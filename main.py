import time

from models.MetodoPago import MetodoPago
from models.TipoGasto import TipoGasto
from models.Viaje import Viaje

# viaje = Viaje("USA", "2021-01-01", "2021-01-10", 1000000)

# viaje.agregar_gasto("2021-01-01", 10, MetodoPago.EFECTIVO, TipoGasto.ALIMENTACION)
# time.sleep(3)  # Espera de 3 segundos
# viaje.agregar_gasto("2021-01-01", 20, MetodoPago.TARJETA, TipoGasto.ENTRETENIMIENTO)
# time.sleep(3)  # Espera de 3 segundos
# viaje.agregar_gasto("2021-01-02", 20, MetodoPago.TARJETA, TipoGasto.ALOJAMIENTO)


# print("--- Reporte diario ---")
# for reporte in viaje.reporte_diario():
#     print(reporte + " Efectivo: " + str(viaje.reporte_diario()[reporte]["efectivo"]) + " Tarjeta: " + str(viaje.reporte_diario()[reporte]["tarjeta"]) + " Total: " + str(viaje.reporte_diario()[reporte]["total"]) + "\n")

# print("--- Reporte por tipo ---")
# for reporte in viaje.reporte_por_tipo():
#     print(reporte + " Efectivo: "  + str(viaje.reporte_por_tipo()[reporte]["efectivo"]) + " Tarjeta: " + str(viaje.reporte_por_tipo()[reporte]["tarjeta"]) + " Total: " + str(viaje.reporte_por_tipo()[reporte]["total"]) + "\n")

# Ingresar los datos del viaje

destino = input("Ingrese el destino (USA, EUROPA, COLOMBIA): ")

if destino not in ["USA", "EUROPA", "COLOMBIA"]:
    print("Destino no valido")
    exit()

fecha_inicio = input("Ingrese la fecha de inicio (año-mes-dia): ")
fecha_fin = input("Ingrese la fecha de fin (año-mes-dia): ")
presupuesto = int(input("Ingrese el presupuesto: "))
viaje = Viaje(destino, fecha_inicio, fecha_fin, presupuesto)

# Ingresar los gastos del viaje
while True:
    fecha = input("Ingrese la fecha del gasto (año-mes-dia): ")
    monto = int(input("Ingrese el monto del gasto: "))
    print("Seleccione el tipo de gasto: ")
    print("T - Transporte")
    print("A - Alimentacion")
    print("AL - Alojamiento")
    print("E - Entretenimiento")
    print("C - Compras")
    tipo_gasto = input("Ingrese el tipo de gasto: ").upper()

    if tipo_gasto not in ["T", "A", "AL", "E", "C"]:
        print("Tipo de gasto no valido")
        continue

    if tipo_gasto == "T":
        tipo_gasto = TipoGasto.TRANSPORTE
    elif tipo_gasto == "A":
        tipo_gasto = TipoGasto.ALIMENTACION
    elif tipo_gasto == "AL":
        tipo_gasto = TipoGasto.ALOJAMIENTO
    elif tipo_gasto == "E":
        tipo_gasto = TipoGasto.ENTRETENIMIENTO
    else:
        tipo_gasto = TipoGasto.COMPRAS

    print("Seleccione el metodo de pago: ")
    print("E - Efectivo")
    print("T - Tarjeta")
    metodo_pago = input("Ingrese el metodo de pago: ").upper()
    print(metodo_pago)

    if metodo_pago not in ["E", "T"]:
        print("Metodo de pago no valido")
        continue

    if metodo_pago == "E":
        metodo_pago = MetodoPago.EFECTIVO
    else:
        metodo_pago = MetodoPago.TARJETA

    

    viaje.agregar_gasto(fecha, monto, metodo_pago, tipo_gasto)
    continuar = input("Desea continuar? (s/n)")
    if continuar.upper() == "N":
        break

    

print("--- Reporte diario ---")
for reporte in viaje.reporte_diario():
    print(reporte + " Efectivo: " + str(viaje.reporte_diario()[reporte]["efectivo"]) + " Tarjeta: " + str(viaje.reporte_diario()[reporte]["tarjeta"]) + " Total: " + str(viaje.reporte_diario()[reporte]["total"]) + "\n")


print("--- Reporte por tipo ---")

for reporte in viaje.reporte_por_tipo():
    print(reporte + " Efectivo: "  + str(viaje.reporte_por_tipo()[reporte]["efectivo"]) + " Tarjeta: " + str(viaje.reporte_por_tipo()[reporte]["tarjeta"]) + " Total: " + str(viaje.reporte_por_tipo()[reporte]["total"]) + "\n")

