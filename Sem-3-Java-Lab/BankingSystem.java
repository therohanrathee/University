import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;
import java.util.regex.Pattern;

/**
 * A class representing a bank account with user details, password, and PIN.
 */
class Account {
    private String firstName;
    private String lastName;
    private String dob;
    private String gender;
    private String mobileNumber;
    private String password;
    private String pin;
    private double balance;

    public Account(String firstName, String lastName, String dob, String gender, String mobileNumber, String password, String pin) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.dob = dob;
        this.gender = gender;
        this.mobileNumber = mobileNumber;
        this.password = password;
        this.pin = pin;
        this.balance = 0.0;
    }

    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    public String getGender() { return gender; }
    public double getBalance() { return balance; }
    public void setBalance(double balance) { this.balance = balance; }
    public String getDob() { return dob; }
}

/**
 * This program uses a single class and a HashMap to manage accounts.
 */
public class BankingSystem {

    // A map to store account numbers and their balances
    private static Map<String, Account> accounts = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);
    private static Random random = new Random();

    public static void main(String[] args) {
        System.out.println("Welcome to the Multi-Account Banking System!");
        boolean running = true;
        while (running) {
            System.out.println("\n--- Main Menu ---");
            System.out.println("1. Create a New Account");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. Check Balance");
            System.out.println("5. Exit");
            System.out.print("Please enter your choice: ");

            String choice = scanner.nextLine();
            switch (choice) {
                case "1":
                    createAccount();
                    break;
                case "2":
                    deposit();
                    break;
                case "3":
                    withdraw();
                    break;
                case "4":
                    checkBalance();
                    break;
                case "5":
                    running = false;
                    System.out.println("Thank you for using our banking system. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
        scanner.close();
    }

    /**
     * Creates a new account with a starting balance of 0.0.
     */
    public static void createAccount() {
        System.out.println("--- Create New Account ---");
        System.out.print("Enter First Name: ");
        String firstName = scanner.nextLine();
        System.out.print("Enter Last Name: ");
        String lastName = scanner.nextLine();
        System.out.print("Enter Date of Birth (DDMMYYYY): ");
        String dob = scanner.nextLine();
        System.out.print("Enter Gender (e.g., Male, Female): ");
        String gender = scanner.nextLine();

        String mobileNumber = "";
        while (true) {
            System.out.print("Enter 10-digit mobile number: ");
            mobileNumber = scanner.nextLine();
            if (mobileNumber.matches("\\d{10}")) {
                break;
            } else {
                System.out.println("Invalid mobile number. Please enter a 10-digit number.");
            }
        }

        String password = "";
        while (true) {
            System.out.print("Create a password (min 8 chars, 1 capital, 1 small, 1 number, 1 special char, no spaces): ");
            password = scanner.nextLine();
            if (isValidPassword(password)) {
                break;
            } else {
                System.out.println("Password does not meet requirements. Please try again.");
            }
        }

        String pin = "";
        while (true) {
            System.out.print("Create a 4-digit PIN: ");
            pin = scanner.nextLine();
            if (isValidPin(pin, dob)) {
                break;
            } else {
                System.out.println("Invalid PIN. It must be 4 digits and cannot be your birth year.");
            }
        }

        // Generate a random two-digit number (10-99)
        int randomPrefix = 10 + random.nextInt(90);
        String newAccountId = String.valueOf(randomPrefix) + mobileNumber;
        accounts.put(newAccountId, new Account(firstName, lastName, dob, gender, mobileNumber, password, pin));

        // Welcome message based on gender and displaying the new account ID
        String salutation = gender.equalsIgnoreCase("female") ? "Ms." : "Mr.";
        System.out.println("\nWelcome, " + salutation + " " + firstName + "! Your new 12-digit account number is: " + newAccountId);
    }

    private static boolean isValidPassword(String password) {
        // Minimum length of 8, at least one uppercase, one lowercase, one digit, one special character, and no whitespace
        String pattern = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>/?])(?=\\S+$).{8,}$";
        return Pattern.compile(pattern).matcher(password).matches();
    }

    private static boolean isValidPin(String pin, String dob) {
        // Check if PIN is 4 digits and not equal to the birth year
        String birthYear = dob.substring(4, 8);
        return pin.matches("\\d{4}") && !pin.equals(birthYear);
    }

    /**
     * Deposits money into a specified account.
     */
    public static void deposit() {
        System.out.print("Enter account number: ");
        String accountId = scanner.nextLine();
        if (accounts.containsKey(accountId)) {
            System.out.print("Enter amount to deposit: ");
            try {
                double amount = Double.parseDouble(scanner.nextLine());
                if (amount > 0) {
                    Account account = accounts.get(accountId);
                    double currentBalance = account.getBalance();
                    double newBalance = currentBalance + amount;
                    account.setBalance(newBalance);
                    System.out.printf("Deposited $%.2f. Your new balance is $%.2f\n", amount, newBalance);
                } else {
                    System.out.println("Deposit amount must be positive.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid amount. Please enter a valid number.");
            }
        } else {
            System.out.println("Account not found.");
        }
    }

    /**
     * Withdraws money from a specified account.
     */
    public static void withdraw() {
        System.out.print("Enter account number: ");
        String accountId = scanner.nextLine();
        if (accounts.containsKey(accountId)) {
            System.out.print("Enter amount to withdraw: ");
            try {
                double amount = Double.parseDouble(scanner.nextLine());
                Account account = accounts.get(accountId);
                double currentBalance = account.getBalance();
                if (amount > 0 && amount <= currentBalance) {
                    double newBalance = currentBalance - amount;
                    account.setBalance(newBalance);
                    System.out.printf("Withdrew $%.2f. Your new balance is $%.2f\n", amount, newBalance);
                } else {
                    System.out.println("Withdrawal failed. Insufficient funds or invalid amount.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid amount. Please enter a valid number.");
            }
        } else {
            System.out.println("Account not found.");
        }
    }

    /**
     * Checks the balance of a specified account.
     */
    public static void checkBalance() {
        System.out.print("Enter account number: ");
        String accountId = scanner.nextLine();
        if (accounts.containsKey(accountId)) {
            Account account = accounts.get(accountId);
            double balance = account.getBalance();
            System.out.printf("The current balance for account %s is $%.2f\n", accountId, balance);
        } else {
            System.out.println("Account not found.");
        }
    }
}