class Dog:
    
    # class attribute
    species = 'mammal'

    # initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_eat = False
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)
    
    def speak(self, sound):
        return "{} speaks {}".format(self.name, sound)
    
    def eat(self):
        self.is_eat = True
        


philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
print(philo.description())
print(mikey.speak("meaw!"))
philo.eat()
philo.is_eat

# print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

# if philo.species == "mammal":
#     print("{} is a {}.".format(philo.name, philo.species))
    
barg0 = Dog("Bargo", 10)
tracy = Dog("Tracy", 12)
stormy = Dog("Stormy", 4)


def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(
    get_biggest_number(barg0.age, tracy.age, stormy.age)))