# Tarea Semana 12: Reserva de un asiento en sala de cine
# Nombre: Juan José Quinto Chávez
# Objetivo: Registrar la reserva de un asiento y mostrar
# el estado completo de una sala de cine de 3 filas x 4 columnas.

# Crear una matriz de 3 filas y 4 columnas
# 0 representa un asiento libre
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar al usuario la fila del asiento
fila = int(input("Ingrese fila (0 a 2): "))

# Solicitar al usuario la columna del asiento
columna = int(input("Ingrese columna (0 a 3): "))

# Marcar el asiento seleccionado como reservado
asientos[fila][columna] = 1

# Mostrar el estado completo de la sala
print("\nEstado de la sala:")

# Recorrer las filas de la matriz
for i in range(3):

    # Recorrer las columnas de cada fila
    for j in range(4):
        print(asientos[i][j], end=" ")

    # Saltar de línea al terminar cada fila
    print()