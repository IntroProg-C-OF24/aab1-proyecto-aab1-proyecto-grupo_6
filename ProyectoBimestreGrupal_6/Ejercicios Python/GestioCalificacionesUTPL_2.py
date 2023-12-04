import random

estudiantes_aprobados = 0
estudiantes_reprobados = 0
estudiante = 1
total_estudiantes = 0

print("----------------GESTION DE CALIFICACIONES UTPL----------------")
materia = random.randint(1, 25)

while True:
    cedula = random.randint(1100000000, 1199999999)
    ACD = random.randint(0, 10)
    APE = random.randint(0, 10)
    AA = random.randint(0, 10)

    nota_ACD = ACD * (3.5 / 10)
    nota_APE = APE * (3.5 / 10)
    nota_AA = AA * (3 / 10)
    promedio = nota_ACD + nota_APE + nota_AA

    print("---------RESULTADOS---------")
    print(f"Nombre: Estudiante {estudiante}")
    print(f"Cedula: {cedula}")
    print(f"Materia: Materia {materia}")
    print(f"Nota ACD (3,5/10): {nota_ACD}")
    print(f"Nota APE (3,5/10): {nota_APE}")
    print(f"Nota AA (3/10): {nota_AA}")
    print(f"Promedio: {promedio}")
    print("=====================================================")

    if promedio >= 7.0:
        print("El estudiante ha APROBADO la materia")
        estudiantes_aprobados += 1
    else:
        print("El estudiante debe rendir un examen de recuperacion.")
        estudiantes_reprobados += 1

    notas = input("Desea ingresar otro estudiante? (Si/No): ")
    if notas[0].lower() != 's':
        break

total_estudiantes = estudiantes_aprobados + estudiantes_reprobados
print("--------->ESTADISTICA--DE--LA--MATERIA<-----------")
print(f"Estudiantes aprobados: {estudiantes_aprobados}") 
print(f"Estudiantes reprobados: {estudiantes_reprobados}") 
print(f"Porcentaje de aprobacion: {(estudiantes_aprobados / total_estudiantes) * 100}%")
print(f"Porcentaje de reprobacion: {(estudiantes_reprobados / total_estudiantes) * 100}%")
