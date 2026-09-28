# 8. Ejercicio integrador

# A partir de la clase Sensor definida anteriormente, desarrollar un programa que:

# - Represente mediante una matriz de NumPy las mediciones realizadas por tres sensores. Cada fila deberá corresponder a un sensor y cada columna, a una medición.
# - Recorra las filas de la matriz utilizando range().
# - Cree un objeto Sensor por cada fila y registre en él todas sus mediciones.
# - Almacene los objetos creados en una lista.
# - Recorra la lista de sensores y obtenga, para cada uno, su nombre, su promedio y su estado.

import numpy as np

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def registrar_medicion(self, valor):
        self.mediciones.append(float(valor))  # convierte np.float64 a float

    def calcular_promedio(self):
        if not self.mediciones:
            return None
        return sum(self.mediciones) / len(self.mediciones)

    def mostrar_estado(self):
        return self.nombre, self.mediciones, self.calcular_promedio()

mediciones = np.array([
    [24.0, 25.0, 24.5],
    [31.0, 32.5, 30.0],
    [27.0, 26.5, 28.0]
])

sensores = []

for i in range(mediciones.shape[0]):
    sensor = Sensor(f"Sensor {i+1}")

    for valor in mediciones[i]:
        sensor.registrar_medicion(valor)

    sensores.append(sensor)

for sensor in sensores:
    nombre, mediciones_registradas, promedio = sensor.mostrar_estado()
    print(f"Nombre: {nombre}, Promedio: {promedio:.2f}, Estado: {mediciones_registradas}")