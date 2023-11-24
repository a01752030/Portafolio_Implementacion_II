import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ventas de gasolina
semana = list(range(1, 13))
ventas = [17, 21, 19, 23, 18, 16, 20, 18, 22, 20, 15, 22]

# Crear un DataFrame con los datos
data = pd.DataFrame({'Semana': semana, 'Ventas': ventas})

# Función para calcular el Error Cuadrático Medio (CME)
def calcular_cme(actual, pronosticado):
    return ((actual - pronosticado) ** 2).mean()

# Método de Promedios Móviles
def promedios_moviles(data, n):
    return data['Ventas'].rolling(window=n).mean()

# Método de Promedios Móviles Ponderados
def promedios_moviles_ponderados(data, pesos):
    return data['Ventas'].rolling(window=len(pesos)).apply(lambda x: (x * pesos).sum())

# Método de Suavizamiento Exponencial
def suavizamiento_exponencial(data,  ):
    ventas_suavizadas = [data['Ventas'][0]]
    for i in range(1, len(data)):
        ventas_suavizadas.append(alpha * data['Ventas'][i] + (1 - alpha) * ventas_suavizadas[i - 1])
    return ventas_suavizadas

# Evaluar varios valores de alpha para suavizamiento exponencial y encontrar el mínimo CME
alphas = np.arange(0.1, 1.1, 0.1)
cme_values = []

for alpha in alphas:
    ventas_suavizadas = suavizamiento_exponencial(data, alpha)
    cme = calcular_cme(data['Ventas'], ventas_suavizadas)
    cme_values.append(cme)

# Encontrar el valor de alpha que minimiza el CME
optimal_alpha = alphas[np.argmin(cme_values)]
print(f"El valor óptimo de alpha que minimiza el CME es: {optimal_alpha}")

# Graficar los resultados
plt.figure(figsize=(12, 6))
plt.plot(data['Semana'], data['Ventas'], label='Ventas reales', marker='o')
plt.plot(data['Semana'], suavizamiento_exponencial(data, optimal_alpha), label=f'Suavizamiento Exponencial (α={optimal_alpha})', linestyle='--')
plt.legend()
plt.xlabel('Semana')
plt.ylabel('Ventas de gasolina (miles)')
plt.title('Pronóstico de Ventas de Gasolina')
plt.show()