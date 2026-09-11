function pizzaOven(crust,sauce,cheese,toppings){
    var pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheese = cheese;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven("deep dish", "traditional", "mozzarella", ["peperoni", "sausage"])
console.log(pizza1);

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella","fata"], ["mushrooms", "olives", "onions"])
console.log(pizza2);

var pizza3 = pizzaOven("thin", "BBQ", "mozzarella", "chicken");
console.log(pizza3);

var pizza4 = pizzaOven("stuffed", "tomato", "cheese", "olives");
console.log(pizza4);



var crusts = ["thin", "thick", "stuffed"];
var sauces = ["tomato", "BBQ", "white"];
var cheeses = ["mozzarella", "cheddar", "parmesan"];
var toppings = ["mushrooms", "pepperoni", "chicken", "olives"];

function randomPizza() {
    var crust = crusts[Math.floor(Math.random() * crusts.length)];
    var sauce = sauces[Math.floor(Math.random() * sauces.length)];
    var cheese = cheeses[Math.floor(Math.random() * cheeses.length)];
    var topping = toppings[Math.floor(Math.random() * toppings.length)];

    return pizzaOven(crust, sauce, cheese, topping);
}