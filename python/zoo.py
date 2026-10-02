class Animal:
    def __init__(self,name,age,health = 100,happiness = 100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        
    
    def display_info(self):
        print(f"name is {self.name} age is {self.age} health is {self.health} happiness is {self.happiness}")
        return self
       
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self
    
class Lion(Animal):
    def __init__(self,name,age,health = 100,happiness = 100):
        super().__init__(name,age,health,happiness)
        
    def feed(self):
        self.health += 20
        self.happiness += 20
        return self
    
class Tiger(Animal):
    def __init__(self,name,age,health = 100,happiness = 100):
        super().__init__(name,age,health,happiness)
        
    def feed(self):
        self.health += 15
        self.happiness += 15
        return self
    

    
# lion = Lion("emil" , 30).feed().display_info()
# tiger = Tiger("simba" , 25).feed().display_info()

 
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add_lion(self, name, age):
        self.animals.append(Lion(name, age))
        return self
        
    def add_tiger(self, name, age):
        self.animals.append(Tiger(name, age))
        return self
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
             animal.display_info()
             
    def feed(self, animal):
        self.animals[animal].feed()
        return self
             
zoo1 = Zoo("John's Zoo")             
zoo1.add_lion("Nala" , 18).add_lion("Simba", 20).add_tiger("Rajah", 25).add_tiger("Shere Khan", 30).feed(0).print_all_info()

