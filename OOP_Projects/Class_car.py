class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = min(max(fuelRate, 0), 100)
        self.velocity = min(max(velocity, 0), 200)

    def run(self, velocity, distance):
        if 0 <= velocity <= 200:
            self.velocity = velocity
        else:
            raise ValueError("Velocity must be between 0 and 200")

        fuel_consumed = (distance / 10) * 10
        self.fuelRate -= fuel_consumed

        if self.fuelRate <= 0:
            remain_distance = distance - ((self.fuelRate + fuel_consumed) / 10 * 10)
            self.fuelRate = 0
            self.stop(remain_distance)
        else:
            self.stop(0)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"Stopped before arriving. Remaining distance: {remain_distance} km.")
        else:
            print("Arrived at destination.")
