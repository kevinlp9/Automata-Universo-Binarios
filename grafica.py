import matplotlib.pyplot as plt

# Ruta al archivo de texto de 8 GB con números binarios
archivo = "NumeroDigitos.txt"

# Inicializar un diccionario para contar la cantidad de unos en cada cadena binaria
contador_unos = {}

# Tamaño del bloque en bytes (ajusta según la capacidad de memoria disponible)
tamaño_bloque = 1024 * 1024  # 1 MB

# Leer el archivo en bloques y contar los unos en cada cadena binaria
with open(archivo, 'rb') as f:
    while True:
        bloque = f.read(tamaño_bloque)
        if not bloque:
            break  # Fin del archivo
        
        # Convertir el bloque en una cadena de bits
        cadena_binaria = ''.join(format(byte, '08b') for byte in bloque)
        
        # Contar los unos en la cadena binaria
        for bit in cadena_binaria:
            if bit == '1':
                if cadena_binaria in contador_unos:
                    contador_unos[cadena_binaria] += 1
                else:
                    contador_unos[cadena_binaria] = 1

# Preparar los datos para graficar
x = list(contador_unos.keys())
y = list(contador_unos.values())

# Graficar los datos (esto puede llevar tiempo si hay muchas cadenas únicas)
plt.figure(figsize=(10, 6))
plt.bar(x, y)
plt.xlabel('Cadena Binaria')
plt.ylabel('Cantidad de unos en la cadena')
plt.title('Distribución de unos en el archivo binario')
plt.show()
