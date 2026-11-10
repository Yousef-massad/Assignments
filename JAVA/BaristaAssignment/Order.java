
import java.util.ArrayList;

public class Order {

    // MEMBER VARIABLES
    private String name;
    private boolean ready;
    private ArrayList<Item> items;

    // DEFAULT CONSTRUCTOR
    public Order() {
        this.name = "Guest";
        this.ready = false;
        this.items = new ArrayList<Item>();
    }

    // OVERLOADED CONSTRUCTOR
    public Order(String name) {
        this.name = name;
        this.ready = false;
        this.items = new ArrayList<Item>();
    }

    // GETTERS
    public String getName() {
        return name;
    }

    public boolean isReady() {
        return ready;
    }

    public ArrayList<Item> getItems() {
        return items;
    }

    // SETTERS
    public void setName(String name) {
        this.name = name;
    }

    public void setReady(boolean ready) {
        this.ready = ready;
    }

    public void setItems(ArrayList<Item> items) {
        this.items = items;
    }

    // ADD ITEM
    public void addItem(Item item) {
        items.add(item);
    }

    // GET STATUS MESSAGE
    public String getStatusMessage() {
        if (ready) {
            return "Your order is ready.";
        } else {
            return "Thank you for waiting. Your order will be ready soon.";
        }
    }

    // GET ORDER TOTAL
    public double getOrderTotal() {
        double total = 0;
        
        for (Item item : items) {
            total += item.getPrice();
        
        }

        return total;
    }

    public double getMaxPrice() {
    if (items.isEmpty()) {
        return 0.0;
    }

    double maxPrice = items.get(0).getPrice();

    for (Item item : items) {
        if (item.getPrice() > maxPrice) {
            maxPrice = item.getPrice();
        }
    }

    return maxPrice;
}

    // DISPLAY ORDER INFORMATION
    public void display() {
        System.out.println("Customer Name: " + name);

        for (Item item : items) {

            System.out.println(
                item.getName() + " - $" +
                String.format("%.2f", item.getPrice())
            );
        }

        System.out.printf("Total: $%.2f%n", getOrderTotal());
        System.out.printf("Max: $%.2f%n", getMaxPrice());

    }
}
