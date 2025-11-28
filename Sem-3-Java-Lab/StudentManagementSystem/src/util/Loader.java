package StudentManagementSystem.src.util;

public class Loader implements Runnable {
    @Override
    public void run() {
        try {
            System.out.print("Loading");
            // Simulate a delay with a visual indicator
            for (int i = 0; i < 5; i++) {
                System.out.print(".");
                Thread.sleep(150); // 150ms delay per dot
            }
            System.out.println(); // New line after loading finishes
        } catch (InterruptedException e) {
            System.out.println("\nLoading interrupted.");
        }
    }
}