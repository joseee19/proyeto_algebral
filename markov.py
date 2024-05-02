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

    print("\nIngrese los elementos de la matriz 3x1 como una lista de tres valores separados por espacios:")
    matriz2 = [float(x) for x in input().split()]

    matriz2 = [[matriz2[i]] for i in range(3)]

    veces = int(input("\nIngrese la cantidad de veces que desea multiplicar la matriz transpuesta por la matriz 3x1: "))

    resultado = matriz2
    for _ in range(veces):
        resultado = np.dot(transpuesta, resultado)

    print("\nResultado de la multiplicación acumulada:")
    for fila in resultado:
        print(round(fila[0], 2))


if __name__ == "__main__":
    main()