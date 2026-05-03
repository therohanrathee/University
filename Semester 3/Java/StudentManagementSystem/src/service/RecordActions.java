package StudentManagementSystem.src.service;

public interface RecordActions {
    void addStudent();
    void deleteStudent();
    void searchStudent();
    void viewAllStudents();
    void sortStudentsByMarks(); 
    void saveToFile();          
    void loadFromFile();        
}