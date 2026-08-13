class Patient:
    hospital_name = "CityCare Hospital"

    def __init__(self, patient_id, name, age, admitted_days, daily_charge):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.admitted_days = admitted_days
        self.daily_charge = daily_charge

    def calculate_bill(self):
        return self.admitted_days * self.daily_charge

    @classmethod
    def change_hospital_name(cls, new_name):
        cls.hospital_name = new_name


    @staticmethod
    def is_senior(age):
        return age >= 60

    def __str__(self):
        return (f"[{Patient.hospital_name}] ID: {self.patient_id} | Name: {self.name} | "
                f"Age: {self.age} (Senior: {self.is_senior(self.age)}) | "
                f"Admitted Days: {self.admitted_days} | Total Bill: ${self.calculate_bill():.2f}")


p1 = Patient(101, "Alice Smith", 45, 5, 250.0)
p2 = Patient(102, "Robert Johnson", 68, 3, 300.0)

print(p1)
print(p2)

print("\n... Updating Hospital Name ...\n")
Patient.change_hospital_name("MetroHealth Medical Center")

print(p1)
print(p2)