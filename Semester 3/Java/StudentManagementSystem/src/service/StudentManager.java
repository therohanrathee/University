package StudentManagementSystem.src.service;

import model.Student;
import util.Loader;
import util.StudentNotFoundException;

import java.io.*;
import java.util.*;

public class StudentManager implements RecordActions {
    // List to store student records (Lab 4/5 Collections)
    private List<Student> students = new ArrayList<>();
    private Scanner scanner = new Scanner(System.in);
    // File name for persistence (Saved in project root)
    private final String FILE_NAME = "students.txt";

    @Override
    public void addStudent() {
        try {
            System.out.print("Enter Roll No: ");
            int rollNo = Integer.parseInt(scanner.nextLine());

            // Check for duplicate Roll No (Lab 2/5 Requirement)
            for (Student s : students) {
                if (s.getRollNo() == rollNo) {
                    System.out.println("Error: Roll Number " + rollNo + " already exists!");
                    return;
                }
            }

            System.out.print("Enter Name: ");
            String name = scanner.nextLine();
            if (name.isEmpty()) throw new IllegalArgumentException("Name cannot be empty.");

            System.out.print("Enter Email: ");
            String email = scanner.nextLine();

            System.out.print("Enter Course: ");
            String course = scanner.nextLine();

            System.out.print("Enter Marks: ");
            double marks = Double.parseDouble(scanner.nextLine());
            
            // Validation (Lab 3/5 Requirement)
            if (marks < 0 || marks > 100) {
                throw new IllegalArgumentException("Marks must be between 0 and 100.");
            }

            // Simulate Loading Process (Lab 3 Requirement)
            runLoader();

            Student newStudent = new Student(rollNo, name, email, course, marks);
            students.add(newStudent);
            System.out.println("Student added successfully!");

        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format. Please enter digits.");
        } catch (IllegalArgumentException e) {
            System.out.println("Input Error: " + e.getMessage());
        }
    }

    @Override
    public void viewAllStudents() {
        if (students.isEmpty()) {
            System.out.println("No records found.");
            return;
        }
        System.out.println("\n=== All Student Records ===");
        // Using Iterator (Lab 4 Requirement)
        Iterator<Student> iterator = students.iterator();
        while (iterator.hasNext()) {
            iterator.next().displayInfo();
        }
    }

    @Override
    public void searchStudent() {
        System.out.print("Enter Name to search: ");
        String searchName = scanner.nextLine();
        boolean found = false;

        for (Student s : students) {
            if (s.getName().equalsIgnoreCase(searchName)) {
                System.out.println("\nStudent Found:");
                s.displayInfo();
                found = true;
            }
        }
        
        // Custom Exception usage (Lab 3/5 Requirement)
        if (!found) {
            try {
                throw new StudentNotFoundException("Student with name '" + searchName + "' not found.");
            } catch (StudentNotFoundException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    @Override
    public void deleteStudent() {
        System.out.print("Enter Name to delete: ");
        String deleteName = scanner.nextLine();
        
        // RemoveIf is a clean way to delete from ArrayList
        boolean removed = students.removeIf(s -> s.getName().equalsIgnoreCase(deleteName));

        if (removed) {
            System.out.println("Student record deleted.");
        } else {
            System.out.println("Student not found.");
        }
    }

    @Override
    public void sortStudentsByMarks() {
        if (students.isEmpty()) {
            System.out.println("No records to sort.");
            return;
        }
        // Sorting using Comparator (Lab 4/5 Requirement)
        // Descending order (Highest marks first)
        Collections.sort(students, new Comparator<Student>() {
            @Override
            public int compare(Student s1, Student s2) {
                return Double.compare(s2.getMarks(), s1.getMarks());
            }
        });
        System.out.println("Students sorted by marks (Descending).");
        viewAllStudents();
    }

    @Override
    public void saveToFile() {
        // Try-with-resources to automatically close writer
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME))) {
            runLoader(); // Simulate saving delay
            
            for (Student s : students) {
                writer.write(s.toCSV()); // Write comma-separated values
                writer.newLine();
            }
            System.out.println("Records saved to " + FILE_NAME);
        } catch (IOException e) {
            System.out.println("Error saving to file: " + e.getMessage());
        }
    }

    @Override
    public void loadFromFile() {
        File file = new File(FILE_NAME);
        if (!file.exists()) return; // If file doesn't exist, start with empty list

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] data = line.split(",");
                // Ensure data integrity before creating object
                if (data.length == 5) {
                    int roll = Integer.parseInt(data[0]);
                    String name = data[1];
                    String email = data[2];
                    String course = data[3];
                    double marks = Double.parseDouble(data[4]);
                    
                    students.add(new Student(roll, name, email, course, marks));
                }
            }
            System.out.println("Previous records loaded from file.");
        } catch (IOException | NumberFormatException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    // Helper method to run the Loader thread
    private void runLoader() {
        try {
            Thread loadThread = new Thread(new Loader());
            loadThread.start();
            loadThread.join(); // Wait for loader to finish before proceeding
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}