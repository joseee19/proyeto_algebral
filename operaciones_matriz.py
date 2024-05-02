def suma_matrices():
    numeros = [[0] * 3 for i in range(3)]

    for i in range(3):
        for j in range(3):
            numeros[i][j] = int(input('Por favor, ingrese un numero: '))

    while True:
        for i in range(3):
            print(numeros[i])
        print("Menú de operaciones: ")
        print("1- Visualizar matriz")
        print("2- Suma")
        print("3- Resta")
        print("4- Multiplicación")
        print("5- Factorial")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            for i in range(3):
                print(numeros[i])
            input()
        elif opcion == 2:
            resultado_s = [[0] * 3 for i in range(3)]
            for i in range(3):
                for j in range(3):
                    resultado_s[i][j] = numeros[i][j] + numeros[i][j]
            print("La suma es: ")
            for i in range(3):
                print(resultado_s[i])
            input()
        elif opcion == 3:
            resultado_r = [[0] * 3 for i in range(3)]
            for i in range(3):
                for j in range(3):
                    resultado_r[i][j] = numeros[i][j] - numeros[i][j]
            print("La resta es: ")
            for i in range(3):
                print(resultado_r[i])
            input()
        elif opcion == 4:
            resultado = [[0] * 3 for i in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        resultado[i][j] += numeros[i][k] * numeros[k][j]
            print("La multiplicación es: ")
            for i in range(3):
                print(resultado[i])
            input()
        elif opcion == 5:
            resultado = 1
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna: "))
            numero = numeros[fila][columna]
            print(numero)
            for i in range(1, numero + 1):
                resultado = resultado * i
                print(numeros)
                print(resultado)
                input()
        elif opcion > 5:
            break

suma_matrices()