from Class_car import Car
from Class_employee import Employee
from Class_office import Office

sami_car = Car(name="Fiat 128", fuelRate=50, velocity=60)

sami = Employee(
    name="Sami",
    money=3000,
    mood="neutral",
    healthRate=85,
    id=1,
    car=sami_car,
    email="sami@iti.org",
    salary=7000,
    distanceToWork=20
)

iti_office = Office(name="ITI Smart Village")
iti_office.hire(sami)
sami.eat(3)
sami.buy(7)
sami.work(9)
sami.sleep(6)
sami.send_mail("manager@iti.org", "Arrival", "I arrived at the office on time.")


print("\n sami's info ")
print(sami.name)
print(sami.mood)
print(sami.money)
print(sami.healthRate)
print(sami.salary)
