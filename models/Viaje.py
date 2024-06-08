import json
from models.Gasto import Gasto
from models.MetodoPago import MetodoPago

class Viaje:

    def __init__(self, destino, fecha_inicio, fecha_fin, presupuesto_diario):
        self.__destino = destino
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__presupuesto_diario = presupuesto_diario
        self.__gastos = []

    def get_destino(self):
        return self.__destino

    def set_destino(self, destino):
        self.__destino = destino

    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_fecha_fin(self):
        self.__fecha_fin

    def set_fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin

    def get_presupuesto_diario(self):
        return self.__presupuesto_diario
    
    def set_presupuesto_diario(self, presupuesto_diario):
        self.__presupuesto_diario = presupuesto_diario

    def get_gastos(self):
        return self.__gastos

    def agregar_gasto(self, fecha, valor, metodo_pago, tipo_gasto):

        gasto = Gasto(fecha, valor, metodo_pago, tipo_gasto)
        gasto.realizar_conversion(self.__destino)
        self.__gastos.append(gasto)
        total_gastado = 0
        for gasto in self.__gastos:
            if fecha == gasto.get_fecha():
                total_gastado += gasto.get_valor()
        diferencia = self.__presupuesto_diario - total_gastado

        print(f"-- Gasto -- \nFecha: {fecha}\nValor: {gasto.get_valor()}\nMetodo de pago: {metodo_pago.name}\nTipo de gasto: {tipo_gasto.name}\n")
        print(f"Presupuesto diario: {self.__presupuesto_diario} COP")
        print(f"Total gastado a la fecha: {total_gastado} COP")
        print(f"Diferencia con el presupuesto diario: {diferencia} COP")
        print("\n")

        self.__guardar_informacion()
    
    def __guardar_informacion(self):
        datos_viaje = {
            'destino': self.__destino,
            'fecha_inicio': self.__fecha_inicio,
            'fecha_fin': self.__fecha_fin,
            'presupuesto_diario': self.__presupuesto_diario,
            'gastos': []
        }

        for gasto in self.__gastos:
            datos_viaje['gastos'].append({
                'fecha': gasto.get_fecha(),
                'tipo': str(gasto.get_tipo_gasto().name),
                'valor': gasto.get_valor(),
                'metodo_pago': str(gasto.get_metodo_pago().name)
            })

        with open(f'viaje_{self.__destino}_{self.__fecha_inicio}.json', 'w', encoding='utf-8') as archivo:
            json.dump(datos_viaje, archivo, ensure_ascii=False, indent=4)
    
    def reporte_diario(self):
        reporte = {}
        for gasto in self.__gastos:
            if gasto.get_fecha() not in reporte:
                reporte[gasto.get_fecha()] = {'efectivo': 0, 'tarjeta': 0, 'total': 0}
            if gasto.get_metodo_pago() == MetodoPago.EFECTIVO:
                reporte[gasto.get_fecha()]['efectivo'] += gasto.get_valor()
            else:
                reporte[gasto.get_fecha()]['tarjeta'] += gasto.get_valor()
            reporte[gasto.get_fecha()]['total'] += gasto.get_valor()
        return reporte

    def reporte_por_tipo(self):
        reporte = {}
        for gasto in self.__gastos:
            if gasto.get_tipo_gasto() not in reporte:
                reporte[gasto.get_tipo_gasto().name] = {'efectivo': 0, 'tarjeta': 0, 'total': 0}
            if gasto.get_metodo_pago() == 'efectivo':
                reporte[gasto.get_tipo_gasto().name]['efectivo'] += gasto.get_valor()
            else:
                reporte[gasto.get_tipo_gasto().name]['tarjeta'] += gasto.get_valor()
            reporte[gasto.get_tipo_gasto().name]['total'] += gasto.get_valor()
        return reporte

    