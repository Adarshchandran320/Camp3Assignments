class animal:
    def eat(self):
        print("eat food")

class dog(animal):
    def bark(self):
        print("i bark")
  
class puppy(dog):
    def play(self):
        print("i need to play")

obj1=puppy()
obj1.eat()
obj1.bark()
obj1.play()