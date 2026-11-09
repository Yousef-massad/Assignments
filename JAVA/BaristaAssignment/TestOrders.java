
public class TestOrders {

    public static void main(String[] args) {

        // CREATE ITEMS
        Item item1 = new Item("drip coffee", 1.50);
        Item item2 = new Item("cappuccino", 3.50);
        Item item3 = new Item("latte", 4.00);
        Item item4 = new Item("mocha", 4.50);

        // CREATE TWO GUEST ORDERS
        Order order1 = new Order();
        Order order2 = new Order();

        // CREATE THREE NAMED ORDERS
        Order order3 = new Order("Cindhuri");
        Order order4 = new Order("Rami");
        Order order5 = new Order("Yousef");

        // ADD ITEMS TO ORDER 1
        order1.addItem(item1);
        order1.addItem(item2);

        // ADD ITEMS TO ORDER 2
        order2.addItem(item3);
        order2.addItem(item4);

        // ADD ITEMS TO ORDER 3
        order3.addItem(item1);
        order3.addItem(item2);

        // ADD ITEMS TO ORDER 4
        order4.addItem(item2);
        order4.addItem(item3);

        // ADD ITEMS TO ORDER 5
        order5.addItem(item3);
        order5.addItem(item4);

        // MARK SOME ORDERS AS READY
        order1.setReady(true);
        order3.setReady(true);
        order5.setReady(true);

        // TEST GET ORDER TOTAL
        System.out.println("Order 1 Total: $" + order1.getOrderTotal());
        System.out.println("Order 2 Total: $" + order2.getOrderTotal());

        // TEST STATUS MESSAGES
        System.out.println("\n===== ORDER STATUS =====");
        System.out.println(order1.getStatusMessage());
        System.out.println(order2.getStatusMessage());
        System.out.println(order3.getStatusMessage());
        System.out.println(order4.getStatusMessage());
        System.out.println(order5.getStatusMessage());

        // DISPLAY ALL ORDERS
        System.out.println("\n===== ORDER DETAILS =====");

        order1.display();

        System.out.println();

        order2.display();

        System.out.println();

        order3.display();

        System.out.println();

        order4.display();

        System.out.println();

        order5.display();
    }
}
