import unittest

from models.Viaje import Viaje
from models.MetodoPago import MetodoPago
from models.TipoGasto import TipoGasto
import time

class TestViaje(unittest.TestCase):

    # Test para verificar que se pueda agregar un gasto local a un viaje
    def test_agregar_gasto_local(self):
        viaje = Viaje("COLOMBIA", "2021-01-01", "2021-01-10", 1000000)
        viaje.agregar_gasto("2021-01-01", 10000, MetodoPago.EFECTIVO, TipoGasto.ALIMENTACION)

        self.assertEqual(viaje.get_gastos()[0].get_valor(), 10000)

    # Test para verificar que se pueda agregar un gasto internacional a un viaje
    def test_agregar_gasto_internacional(self):
        viaje = Viaje("USA", "2021-01-01", "2021-01-10", 1000000)
        viaje.agregar_gasto("2021-01-01", 20, MetodoPago.EFECTIVO, TipoGasto.ALIMENTACION)

        self.assertNotEqual(viaje.get_gastos()[0].get_valor(), 20)

    # Test para verificar que se realice el reporte diario de un viaje local
    def test_reporte_diario(self):
        viaje = Viaje("COLOMBIA", "2021-01-01", "2021-01-10", 1000000)
        viaje.agregar_gasto("2021-01-01", 10000, MetodoPago.EFECTIVO, TipoGasto.ALIMENTACION)
        viaje.agregar_gasto("2021-01-01", 20000, MetodoPago.TARJETA, TipoGasto.ENTRETENIMIENTO)
        viaje.agregar_gasto("2021-01-02", 20000, MetodoPago.TARJETA, TipoGasto.ALOJAMIENTO)

        reporte = viaje.reporte_diario()
        self.assertEqual(reporte["2021-01-01"]["total"], 30000)

    # Test para verificar que se realice el reporte por tipo de gasto de un viaje local
    def test_reporte_por_tipo(self):
        viaje = Viaje("COLOMBIA", "2021-01-01", "2021-01-10", 1000000)
        viaje.agregar_gasto("2021-01-01", 10000, MetodoPago.EFECTIVO, TipoGasto.ALIMENTACION)
        viaje.agregar_gasto("2021-01-01", 20000, MetodoPago.TARJETA, TipoGasto.ENTRETENIMIENTO)
        viaje.agregar_gasto("2021-01-02", 20000, MetodoPago.TARJETA, TipoGasto.ALOJAMIENTO)

        reporte = viaje.reporte_por_tipo()
        self.assertEqual(reporte["ALIMENTACION"]["total"], 10000)
        self.assertEqual(reporte["ENTRETENIMIENTO"]["total"], 20000)
        self.assertEqual(reporte["ALOJAMIENTO"]["total"], 20000)

    # Test para verificar que se realice el reporte diario de un viaje internacional
    def test_reporte_diario_internacional(self):
        viaje = Viaje("USA", "2021-01-01", "2021-01-10", 1000000)
        viaje.agregar_gasto("2021-01-01", 10, MetodoPago.EFECTIVO, TipoGasto.ALIMENTACION)
        time.sleep(3)
        viaje.agregar_gasto("2021-01-01", 20, MetodoPago.TARJETA, TipoGasto.ENTRETENIMIENTO)
        time.sleep(3)
        viaje.agregar_gasto("2021-01-02", 20, MetodoPago.TARJETA, TipoGasto.ALOJAMIENTO)

        reporte = viaje.reporte_diario()
        self.assertNotEqual(reporte["2021-01-01"]["total"], 30)

    # Test para verificar que se realice el reporte por tipo de gasto de un viaje internacional
    def test_reporte_por_tipo_internacional(self):
        viaje = Viaje("USA", "2021-01-01", "2021-01-10", 1000000)
        viaje.agregar_gasto("2021-01-01", 10, MetodoPago.EFECTIVO, TipoGasto.ALIMENTACION)
        time.sleep(3)
        viaje.agregar_gasto("2021-01-01", 20, MetodoPago.TARJETA, TipoGasto.ENTRETENIMIENTO)
        time.sleep(3)
        viaje.agregar_gasto("2021-01-02", 20, MetodoPago.TARJETA, TipoGasto.ALOJAMIENTO)

        reporte = viaje.reporte_por_tipo()
        self.assertNotEqual(reporte["ALIMENTACION"]["total"], 10)
        self.assertNotEqual(reporte["ENTRETENIMIENTO"]["total"], 20)
        self.assertNotEqual(reporte["ALOJAMIENTO"]["total"], 20)