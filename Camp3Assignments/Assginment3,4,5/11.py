
class Calling:
    def make_call(self, number):
        print(f"Calling {number}...")


class Camera:
    def take_photo(self):
        print("Photo captured.")


class SmartPhone(Calling, Camera):
    pass


phone = SmartPhone()
phone.make_call("9876543210")
phone.take_photo()