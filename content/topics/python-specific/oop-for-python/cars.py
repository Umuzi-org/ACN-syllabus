import random


class Wheel:
    def __init__(self):
        self.tread = 1000

    def still_ok(self):
        return self.tread > 0

    def use(self, speed):
        self.tread -= random.random() * 10 * speed


class Vehicle:
    # colour = "red"
    def __init__(self, color):
        self.color = color


class Helicopter(Vehicle):
    pass


class Car(Vehicle):
    has_fueltank = True

    def __init__(self, speed=1, wheels=4):
        print(f"entering constructor: {self} at address {id(self)}")
        # super(Car,self).__init__(color="red")
        self.position = 0
        self.speed = speed
        # self.wheels = [Wheel() for i in range(wheels)]
        self.wheels = []
        for _ in range(wheels):
            self.wheels.append(Wheel())
        print("exiting constructor")

    def drive_forward(self):
        print("driving forwards")
        self.position += self.speed
        for wheel in self.wheels:
            wheel.use(self.speed)

    def needs_service(self):
        if self.position >= 10000:
            return True
        for wheel in self.wheels:
            if not wheel.still_ok():
                return True
        return False
