from Class_person import Person
from Class_car import Car

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self):
        self.car.run(self.distanceToWork, self.car.velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)

    def send_mail(self, to, subject, body):
        print(f"Sending mail to: {to}\nSubject: {subject}\nBody: {body}")