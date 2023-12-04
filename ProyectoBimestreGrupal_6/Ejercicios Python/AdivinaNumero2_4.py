import random

num_adivinar = random.randint(1, 100)
intentos_usados = 0
intentos = 10

print("BIENVENIDO A ADIVINAR EL NUMERO 2.0\nINSTRUCCIONES:")
print(" 1. El rango del numero que debes adivinar esta entre el 1 y el 100")
print(" 2. Tienes tan solo 10 intentos para adivinar")
print(" 3. Tendras la oportunidad de pedir pistas pero esto te restara un intento")
print(" 4. El numero a adivinar es un entero")
print(" 5. Si decides pedir una pista aleatoriamente se te dira una caracteristica del numero entre las pistas estaran")
print("    5.1 Si es mayor")
print("    5.2 Si es menor es par")
print("    5.2 impar")
print("    5.3 es primo")
print("    5.5 pertenece a la serie fibonacci")
print("    5.5 es multiplo de 5")
print("    5.6 es multiplo de 3")
print("Empecemos con el juego, te deseo suerte =D")
print("------------------------------------------")

while intentos > 0:
    print(f"Te quedan {intentos} intentos.")
    num_ingresado = int(input("------> Adivina el numero: "))
    intentos_usados += 1

    if num_ingresado == num_adivinar:
        print(f"FELICIDADES, has adivinado el numero en {intentos_usados} intentos")
        break
    else:
        quiere_pista = input("Numero equivocado, deseas una pista? (Si/No): ")

        if quiere_pista.lower() == "si":
            print("Se te resta un intento por pedir pista")
            intentos -= 1
            pista_aleatoria = random.randint(1, 8)

            if num_adivinar > num_ingresado and pista_aleatoria == 1:
                print("PISTA: Intenta con un numero mayor.   <---")
            elif num_adivinar < num_ingresado and pista_aleatoria == 2:
                print("PISTA: Intenta con un numero menor.   <---")
            elif num_adivinar % 2 == 0 and pista_aleatoria == 3:
                print("PISTA: El numero es par.   <---")
            elif num_adivinar % 2 != 0 and pista_aleatoria == 4:
                print("PISTA: El numero es impar.   <---")
            elif num_adivinar in [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and pista_aleatoria == 5:
                print("PISTA: El numero pertenece a la secuencia fibonacci   <---")
            elif num_adivinar % 5 == 0 and pista_aleatoria == 6:
                print("PISTA: El numero es multiplo de 5  <---")
            elif num_adivinar % 3 == 0 and pista_aleatoria == 7:
                print("PISTA: El numero es multiplo de 3  <---")
            else:
                print("*Elige cuidadosamente el proximo numero*")
                intentos -= 1
        elif quiere_pista.lower() == "no":
            print("*Elige cuidadosamente el proximo numero*")

    if intentos == 0:
        print(f"Lo siento, has agotado tus intentos. El numero era: {num_adivinar}")