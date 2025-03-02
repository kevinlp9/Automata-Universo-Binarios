import matplotlib.pyplot as plt

numeros_binarios = []
conteo_unos = []

with open('C:/Users/solod/OneDrive/Documents/CUARTO SEMESTRE/Teoría de la computación/Ejercicio 1/NumeroDigitos.txt', 'r') as archivo:
    for linea in archivo:
        numero_binario = linea.strip()
        numeros_binarios.append(numero_binario)
        conteo = numero_binario.count('1')
        conteo_unos.append(conteo)

numeros_decimales = [int(numero, 2) for numero in numeros_binarios]

plt.figure(figsize=(10, 6))
plt.plot(numeros_decimales, conteo_unos, marker='o', linestyle='-', color='b')
plt.xlabel('Número Decimal')
plt.ylabel('Cantidad de "1" en el Binario')
plt.title('Gráfica de Números Binarios')
plt.grid(True)

plt.show()
