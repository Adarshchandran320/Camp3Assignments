
class Engine:
    def engine_details(self, engine_type):
        self.engine_type = engine_type


class Safety:
    def safety_features(self, airbags, abs_system):
        self.airbags = airbags
        self.abs_system = abs_system


class Car(Engine, Safety):
    def display(self):
        print("Engine Type:", self.engine_type)
        print("Airbags:", self.airbags)
        print("ABS:", self.abs_system)


car = Car()
car.engine_details("Petrol")
car.safety_features(6, "Available")
car.display()