public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (Prices for drinks following camelCase)
        double dripCoffeePrice = 3.0;
        double lattePrice = 4.5;
        double cappuccinoPrice = 5.0;
        double mochaPrice = 3.5;
        
        // Customer name variables
        String customer1 = "Shatha";
        String customerAhmad = "Ahmad";
        String customerSali = "Sali";
        String customerAdam = "Adam";
        
        // Order completions (Status flags: true or false)
        boolean isReadyOrder1 = false;
        boolean isReadyAhmad = true;
        boolean isReadySali = false;
        boolean isReadyAdam = true;
        
        // APP INTERACTION SIMULATION
        System.out.println(generalGreeting + customer1); // Displays "Welcome to Cafe Java, Shatha"
        
        // 4. Sali ordered a coffee. Check her order status.
        System.out.println(customerSali + pendingMessage); // بما إنها لسا مش جاهزة (false)
        
        // 5. Ahmad ordered a cappuccino. Use an if statement.
        if (isReadyAhmad) {
            System.out.println(customerAhmad + readyMessage);
            System.out.println(displayTotalMessage + cappuccinoPrice);
        } else {
            System.out.println(customerAhmad + pendingMessage);
        }
        
        // 6. Sali just ordered 2 lattes, print total and status.
        System.out.println(customerSali + ", " + displayTotalMessage + (lattePrice * 2));
        if (isReadySali) {
            System.out.println(customerSali + readyMessage);
        } else {
            System.out.println(customerSali + pendingMessage);
        }
        
        // 7. Adam was charged for coffee but ordered a latte. Calculate difference.
        double adamExtra = lattePrice - dripCoffeePrice;
        System.out.println(customerAdam + ", " + displayTotalMessage + adamExtra);
    }
} 
    

