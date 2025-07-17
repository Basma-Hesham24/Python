class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            arrival_time = Office.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if arrival_time > 0:
                print(f"{emp.name} is late by {arrival_time} hours. Deducting 10.")
                self.deduct(empId, 10)
            else:
                print(f"{emp.name} is on time. Rewarding 10.")
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity
        arrival_time = moveHour + time_needed
        return max(0, arrival_time - targetHour)

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num