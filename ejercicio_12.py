### Ejercicio 12 — Función de resumen reutilizable

# 1. Definir `resumir_pasajeros(datos)` para recibir un DataFrame y devolver una tupla con la cantidad de pasajeros, la edad promedio y la proporción de supervivencia.
# 2. Si el DataFrame está vacío, devolver `(0, None, None)`. Para la edad promedio, ignorar edades ausentes; si no hay ninguna edad conocida, devolver `None` en esa posición.
# 3. Aplicar la función al dataset completo y luego a cada clase usando un `for`.
# 4. Desempaquetar los resultados y mostrarlos con etiquetas claras; expresar la supervivencia como porcentaje.
# 5. Probar también con `df.iloc[0:0]`.

# **Pista:** usar `.empty` para comprobar si un DataFrame está vacío y `.notna().any()` para detectar si existen edades conocidas.

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

def resumir_pasajeros(datos):
    if datos.empty:
        return (0, None, None)
    
    cantidad = len(datos)
    
    edad_promedio = datos['age'].mean() if datos['age'].notna().any() else None
    
    proporcion_supervivencia = datos['survived'].mean()
    
    return (cantidad, edad_promedio, proporcion_supervivencia)

cantidad, edad_promedio, proporcion = resumir_pasajeros(df)
print(f"Total - Cantidad: {cantidad}, Edad promedio: {edad_promedio:.2f}, Supervivencia: {proporcion*100:.2f}%")

for clase in sorted(df['pclass'].unique()):
    datos_clase = df[df['pclass'] == clase]
    cantidad, edad_promedio, proporcion = resumir_pasajeros(datos_clase)
    print(f"Clase {clase} - Cantidad: {cantidad}, Edad promedio: {edad_promedio:.2f}, Supervivencia: {proporcion*100:.2f}%")

cantidad, edad_promedio, proporcion = resumir_pasajeros(df.iloc[0:0])
print(f"Vacío - Cantidad: {cantidad}, Edad promedio: {edad_promedio}, Supervivencia: {proporcion}")