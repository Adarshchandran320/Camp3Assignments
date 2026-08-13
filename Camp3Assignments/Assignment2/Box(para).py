class Box:

    def __init__(self,width,height,depth):
        self.width=width
        self.height=height
        self.depth=depth

    def get_volume(self):
        print("Volume of Box \n")
        Volume=self.width*self.height*self.depth
        self.Volume=Volume
        print("Volume",self.Volume)

obj1=Box(5,8,4)
obj2=Box(6,9,5)
obj1.get_volume()
obj2.get_volume()