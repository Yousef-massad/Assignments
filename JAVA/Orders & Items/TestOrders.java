
public class TestOrders {

    public static void main(String[] args) {

        // Menu Items

        Item item1 = new Item();
        item1.name = "mocha";
        item1.price = 4.50;

        Item item2 = new Item();
        item2.name = "latte";
        item2.price = 4.00;

        Item item3 = new Item();
        item3.name = "drip coffee";
        item3.price = 2.50;

        Item item4 = new Item();
        item4.name = "cappuccino";
        item4.price = 4.25;


        // Orders

        Order order1 = new Order();
        order1.name = "Rami";

        Order order2 = new Order();
        order2.name = "Jimmy";

        Order order3 = new Order();
        order3.name = "Noah";

        Order order4 = new Order();
        order4.name = "Sam";


        // Print order1

        System.out.println(order1);

        // Print order1 total

        System.out.println(order1.total);


        // Jimmy ordered a mocha

        order2.items.add(item1);
        order2.total += item1.price;


        // Noah ordered a cappuccino

        order3.items.add(item4);
        order3.total += item4.price;


        // Sam ordered a latte

        order4.items.add(item2);
        order4.total += item2.price;


        // Rami's order is ready

        order1.ready = true;


        // Sam ordered 2 more lattes

        order4.items.add(item2);
        order4.items.add(item2);

        order4.total += item2.price * 2;


        // Jimmy's order is ready

        order2.ready = true;


        // Display all orders

        System.out.println("\n===== ORDER DETAILS =====");

        System.out.println("Customer: " + order1.name);
        System.out.println("Total: " + order1.total);
        System.out.println("Ready: " + order1.ready);

        System.out.println("\nCustomer: " + order2.name);
        System.out.println("Total: " + order2.total);
        System.out.println("Ready: " + order2.ready);

        System.out.println("\nCustomer: " + order3.name);
        System.out.println("Total: " + order3.total);
        System.out.println("Ready: " + order3.ready);

        System.out.println("\nCustomer: " + order4.name);
        System.out.println("Total: " + order4.total);
        System.out.println("Ready: " + order4.ready);

    }
}
