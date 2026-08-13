class HotelRoom:
    room_number = ""
    room_type = ""
    total_rooms = 0
    booked_rooms = 0

    def book_room(self, rooms):
        available_rooms = self.total_rooms - self.booked_rooms

        if rooms <= available_rooms:
            self.booked_rooms = self.booked_rooms + rooms
            print(rooms, "room(s) booked successfully")
            print("Booked Rooms :", self.booked_rooms)
        else:
            print("Rooms are not available")

    def cancel_room(self, rooms):
        if rooms <= self.booked_rooms:
            self.booked_rooms = self.booked_rooms - rooms
            print(rooms, "room(s) cancelled successfully")
            print("Booked Rooms :", self.booked_rooms)
        else:
            print("Cannot cancel more rooms than booked")

    def display(self):
        print("Room Number :", self.room_number)
        print("Room Type :", self.room_type)
        print("Total Rooms :", self.total_rooms)
        print("Booked Rooms :", self.booked_rooms)
        print("Available Rooms :", self.total_rooms - self.booked_rooms)


# Create Object
room1 = HotelRoom()

# Assign Values Manually
room1.room_number = "101"
room1.room_type = "Deluxe"
room1.total_rooms = 20
room1.booked_rooms = 5

print("========== INITIAL DETAILS ==========")
room1.display()

print("\n========== BOOK ROOM ==========")
room1.book_room(8)

print("\n========== AFTER BOOKING ==========")
room1.display()

print("\n========== CANCEL ROOM ==========")
room1.cancel_room(3)

print("\n========== AFTER CANCELLATION ==========")
room1.display()