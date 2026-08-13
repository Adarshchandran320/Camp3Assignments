#7
class movieticket:
    movie_name = ""
    total_seats=0
    booked_seats=0

    def book_seats(self, seats):
        available_seats = self.total_seats - self.booked_seats

        if seats <= available_seats:
            self.booked_seats = self.booked_seats + seats
            print("Seats booked successfully")
            print("Booked Seats :", self.booked_seats)
        else:
            print("Not enough seats available")

    def cancel_seats(self, seats):
        if seats<=self.booked_seats:
            self.booked_seats = self.booked_seats - seats
            print("Seats cancelled successfully")
            print("Booked Seats :", self.booked_seats)
        else:
            print("seats not booked")

    def display(self):
        print("Movie Name :", self.movie_name)
        print("Total Seats :", self.total_seats)
        print("Booked Seats :", self.booked_seats)

ticket=movieticket()
ticket.movie_name = "I"
ticket.total_seats=100
ticket.booked_seats=20

ticket.display()
ticket.book_seats(30)

ticket.display()
ticket.cancel_seats(10)

ticket.display()
