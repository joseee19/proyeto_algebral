import numpy as np

def main():
    print("Ingrese los elementos de la matriz 3x3:")
    matriz1 = [[float(input(f"Elemento [{i}][{j}]: ")) for j in range(3)] for i in range(3)]

    print("\nMatriz Original:")
    for fila in matriz1:
        print(fila)

    transpuesta = np.transpose(matriz1)

    print("\nTranspuesta de la matriz:")
    for fila in transpuesta:
        print(fila)