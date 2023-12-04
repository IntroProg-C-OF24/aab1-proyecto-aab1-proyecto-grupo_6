package proyectobimestralgrupal;

import java.util.Random;
import java.util.Scanner;

public class SistemAcademicoDeLAUtpl_2 {

    public static void main(String[] args) {
        Random rand = new Random();
        Scanner tecla = new Scanner(System.in);
        int estudiantesAprobados = 0, estudiantesReprobados = 0, estudiante = 1, totalEstudiantes, cedula, materia;
        double ACD, APE, AA, notaACD, notaAPE, notaAA, promedio;
        String notas;
        materia = rand.nextInt(25) + 1;
        System.out.println("----------------GESTION DE CALIFICACIONES UTPL----------------");

        do {
            cedula = rand.nextInt(100000000) + 1100000000;
            
            ACD = rand.nextInt(11);
            APE = rand.nextInt(11);
            AA = rand.nextInt(11);

            notaACD = (ACD * (3.5 / 10));
            notaAPE = (APE * (3.5 / 10));
            notaAA = (AA * (3 / 10));
            promedio = (notaACD + notaAPE + notaAA);

            System.out.println("---------RESULTADOS---------");
            System.out.println("Nombre: Estudiante " + estudiante);
            System.out.println("Cedula: " + cedula);
            System.out.println("Materia: Materia " + materia);
            System.out.println("Nota ACD (3,5/10): " + notaACD);
            System.out.println("Nota APE (3,5/10): " + notaAPE);
            System.out.println("Nota AA (3/10): " + notaAA);
            System.out.println("Promedio: " + promedio);
            System.out.println("=====================================================");

            if (promedio >= 7.0) {
                System.out.println("El estudiante ha APROBADO la materia");
                estudiantesAprobados++;
            } else {
                System.out.println("El estudiante debe rendir un examen de recuperacion.");
                estudiantesReprobados++; // Y aqui tambien igual que arriba guarda es como un contador mas o menos
            }

            // Preguntar si desea ingresar otro estudiante
            System.out.println("======================================="); 
            System.out.println("Desea ingresar otro estudiante? (Si/No)");
            notas = tecla.next();
        } while (notas.charAt(0) == 'S' || notas.charAt(0) == 's');

        totalEstudiantes = estudiantesAprobados + estudiantesReprobados;
        System.out.println("--------->ESTADISTICA--DE--LA--MATERIA<-----------");
        System.out.println("Estudiantes aprobados: " + estudiantesAprobados); 
        System.out.println("Estudiantes reprobados: " + estudiantesReprobados); 
        // Calcular y mostrar el porcentaje de aprobación y reprobación
        System.out.println("Porcentaje de aprobacion: " + ((double) estudiantesAprobados / totalEstudiantes) * 100 + "%");
        System.out.println("Porcentaje de reprobacion: " + ((double) estudiantesReprobados / totalEstudiantes) * 100 + "%");
    }
}
