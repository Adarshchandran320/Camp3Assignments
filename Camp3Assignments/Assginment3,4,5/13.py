
class Logger:
    def log(self, message):
        print("LOG:", message)


class Database:
    def connect(self):
        print("Database connected.")


class Application(Logger, Database):
    pass


app = Application()
app.connect()
app.log("Application started.")