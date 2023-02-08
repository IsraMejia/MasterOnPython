class Coche():
    def desplazamiento(self):
        print("Me desplazo utiliando mis 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utiliando mis 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo usando mis 6 ruedas")

#Haciendo uso del polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo  = Moto()
desplazamientoVehiculo(miVehiculo)

"""
miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()
"""
