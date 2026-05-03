package StudentManagementSystem.src.model;

// Abstract class defining common attributes
public abstract class Person {
    protected String name;
    protected String email;

    public Person(String name, String email) {
        this.name = name;
        this.email = email;
    }

    // Abstract method to be implemented by child classes
    public abstract void displayInfo();

    // Getters
    public String getName() { return name; }
    public String getEmail() { return email; }
}