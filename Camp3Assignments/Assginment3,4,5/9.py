class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class OfficeMachine(Printer, Scanner):
    pass


machine = OfficeMachine()
machine.print_document()
machine.scan_document()