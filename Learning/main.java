import java.sql.SQLOutput;
import java.util.Scanner;
import java.util.Random;

public class main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Random random = new Random();


        System.out.print("Enter First Name Only : ");
        String firstName = sc.next();  // next : Reads only the First Word
        System.out.println("Hello " + firstName);

        sc.nextLine(); // This consumes the /n stored in the input buffer after pressing enter key

        System.out.print("Please enter your name: ");
        String name = sc.nextLine();   // nextLine : Reads the Complete Line
        System.out.println("Hello " + name);

        System.out.print("Enter Your Age : ");
        int age = sc.nextInt();        // nextInt : Takes input as Integers
        System.out.println("You are " + age + " years old");

        System.out.print("Enter your SGPA : ");
        double SGPA = sc.nextDouble(); // nextDouble : Takes input as Double
        System.out.println("Your SGPA is " + SGPA);


        // Conditional Statements

        if (age >= 18) {
            System.out.println("You are an Adult");
        }
        else if (age >= 12) {
            System.out.println("You are a Teen");
        }
        else {
            System.out.println("You are a Child");
        }

        // Random Number Generator

        int randomNumber = random.nextInt(1,6); // Range = [1,6) i.e. 1 : Inclusive, 6 : Exclusive
        System.out.println(randomNumber);

        System.out.println(Math.PI);
        System.out.println(Math.E);
        

        sc.close();

    }
}
