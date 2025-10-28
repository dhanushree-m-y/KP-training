
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.speak()
dog.bark()



#single inheritance

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.move()   # Inherited from Vehicle
c.drive()  # Own method
