### Ejercicio 17
# Crear una clase `Sensor` con los atributos `nombre` y `mediciones`. 
# Incorporar métodos para registrar una medición, calcular el promedio y devolver el estado del sensor.

# Ejercicio 17 --- Clase Sensor

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def registrar_medicion(self, valor):
        self.mediciones.append(valor)

    def calcular_promedio(self):
        if not self.mediciones:
            return None
        return sum(self.mediciones) / len(self.mediciones)

    def mostrar_estado(self):
        return self.nombre, self.mediciones, self.calcular_promedio()

sensor = Sensor("Sensor de temperatura")

sensor.registrar_medicion(24.0)
sensor.registrar_medicion(25.0)
sensor.registrar_medicion(24.5)

nombre, mediciones, promedio = sensor.mostrar_estado()
print(f"Nombre: {nombre}")
print(f"Mediciones: {mediciones}")
print(f"Promedio: {promedio:.2f}")