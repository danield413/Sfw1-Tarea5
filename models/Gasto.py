import requests
from datetime import date
from models.MetodoPago import MetodoPago
from models.TipoGasto import TipoGasto

class Gasto:
    def __init__(self, fecha: date, valor: float, metodo_pago: MetodoPago, tipo_gasto: TipoGasto):
        self.__fecha = fecha
        self.__valor = valor
        self.__metodo_pago = metodo_pago
        self.__tipo_gasto = tipo_gasto

    def get_fecha(self):
        return self.__fecha
    
    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor

    def get_metodo_pago(self):
        return self.__metodo_pago
    
    def set_metodo_pago(self, metodo_pago: MetodoPago):
        self.__metodo_pago = metodo_pago

    def get_tipo_gasto(self):
        return self.__tipo_gasto
    
    def set_tipo_gasto(self, tipo: TipoGasto):
        self.__tipo_gasto = tipo

    def realizar_conversion(self, destino: str):
        if destino.upper() != "USA" and destino.upper() != "ESTADOS UNIDOS" and destino.upper() != "EUROPA":
            return

        response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500", timeout=5).json()
        if destino.upper() == "USA" or destino.upper() == "ESTADOS UNIDOS":
            self.set_valor(
                self.__valor * (response[0]["random"])
            )
        elif destino.upper() == "EUROPA":
            self.set_valor(
                self.__valor * (response[0]["random"] + 200)
            )
