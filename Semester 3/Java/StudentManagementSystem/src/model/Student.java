package StudentManagementSystem.src.model;

public class Student extends Person {
    private int rollNo;
    private String course;
    private double marks;
    private char grade;

    // Constructor
    public Student(int rollNo, String name, String email, String course, double marks) {
        super(name, email); // Call parent (Person) constructor
        this.rollNo = rollNo;
        this.course = course;
        this.marks = marks;
        calculateGrade(); // Calculate grade immediately upon creation
    }

    // Method to calculate grade based on marks (Lab 1 logic)
    private void calculateGrade() {
        if (marks >= 90) grade = 'A';
        else if (marks >= 80) grade = 'B';
        else if (marks >= 70) grade = 'C';
        else if (marks >= 60) grade = 'D';
        else grade = 'F';
    }

    @Override
    public void displayInfo() {
        System.out.println("Roll No: " + rollNo);
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Course: " + course);
        System.out.println("Marks: " + marks);
        System.out.println("Grade: " + grade);
        System.out.println("---------------------------");
    }

    // Getters
    public int getRollNo() { return rollNo; }
    public double getMarks() { return marks; }
    public String getCourse() { return course; }

    // Helper to format data for saving to file (Lab 4/5)
    public String toCSV() {
        return rollNo + "," + name + "," + email + "," + course + "," + marks;
    }
}