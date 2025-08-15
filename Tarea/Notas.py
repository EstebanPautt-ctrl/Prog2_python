nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingrese la nota 3: "))

notafinal = nota1 * 0.30 + nota2 * 0.30 + nota3 * 0.40

if notafinal >= 1 or notafinal <= 1.9:
    print("deficiente")
elif notafinal >= 2 or notafinal <= 2.9:
    print("Insuficiente")
elif notafinal >= 3 or notafinal <= 3.9:
    print("aceptable")
elif notafinal >= 4 or notafinal <= 5:
    print("Destacado")