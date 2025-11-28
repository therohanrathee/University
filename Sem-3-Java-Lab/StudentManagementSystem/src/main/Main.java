package StudentManagementSystem.src.main;

import service.StudentManager;
import java.util.Scanner;

import StudentManagementSystem.src.model.Student;

public class Main {
    public static void main(String[] args) {
        Student manager = new Student();
        Scanner scanner = new Scanner(System.in);

        // Load existing data immediately on startup (Lab 4/5)
        System.out.println("Initializing System...");
        manager.loadFromFile();

        while (true) {
            System.out.println("\n===== Capstone Student Menu =====");
            System.out.println("1. Add Student");
            System.out.println("2. View All Students");
            System.out.println("3. Search by Name");
            System.out.println("4. Delete by Name");
            System.out.println("5. Sort by Marks");
            System.out.println("6. Save and Exit");
            System.out.print("Enter choice: ");

            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    manager.addStudent();
                    break;
                case "2":
                    manager.viewAllStudents();
                    break;
                case "3":
                    manager.searchStudent();
                    break;
                case "4":
                    manager.deleteStudent();
                    break;
                case "5":
                    manager.sortStudentsByMarks();
                    break;
                case "6":
                    manager.saveToFile();
                    System.out.println("Exiting application. Goodbye!");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please enter 1-6.");
            }
        }
    }
}