class Box:
    def __init__(self):
    
        self.width = 0
        self.height = 0
        self.depth = 0

    def get_volume(self):
        return self.width * self.height * self.depth

box1 = Box()
box1.width = 5
box1.height = 3
box1.depth = 2
print(f"Volume of Box 1: {box1.get_volume()}")

box2 = Box()
box2.width = 10
box2.height = 4
box2.depth = 2
print(f"Volume of Box 2: {box2.get_volume()}")