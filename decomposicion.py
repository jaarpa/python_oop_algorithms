"""
This file contains the classes for the decompositon excersice where a
car is decomposed into more specialized classes.
"""


class Car:
    def __init__(self, name, model, color) -> None:
        self.name = name  # Model name
        self.model = model  # Model year
        self.color = color
        self.speed = 0  # [km/h]
        self._engine = Engine()
        if model <= 2010:
            self._transmission = Transmission("Standard")
        else:
            self._transmission = Transmission("Automatic", 6)

    def stop(self):
        self.speed = 0  # [km/h]
        self._engine.kill()

    def start(self):
        self._engine.ignition()

    def accelerate(self, acceleration):
        if self.speed <= self._transmission.gear * 37:
            self.speed = self._engine.inject_fuel(+acceleration) * 0.5
            return self.speed
        else:
            print("Change up the gear!!")
            self._engine._engine_fail()

    def slow_down(self, slowing_down):
        if self.speed >= (self._transmission.gear - 1) * 43:
            self.speed = self._engine.inject_fuel(-slowing_down) * 0.5
            return self.speed
        else:
            print("Change up the gear!!")
            self._engine._engine_fail()


class Transmission:
    def __init__(self, change_type, gears=5) -> None:
        self.change_type = change_type
        self.gears = gears
        self.gear = 1

    def change_up(self):
        if self.gear + 1 <= self.gears:
            self.gear += 1

    def change_down(self):
        if self.gear - 1 >= 1:
            self.gear -= 1


class Engine:

    def __init__(self) -> None:
        self._started = False
        self.fuel_injection_rate = 0  # ml/s
        self._krpm = 0

    def _engine_fail(self):
        print("CAsfaajsjf a faoooown")
        self.kill()
        print("The car is off, turn it on again!")

    def inject_fuel(self, diff_injection_rate):
        self.fuel_injection_rate += diff_injection_rate
        self._krpm = self.fuel_injection_rate*1.5
        return self._krpm

    def ignition(self):
        if not self._started:
            print(
                """
                Chigchig-chighi
                chigichiiigi
                Brooom!!!
                """
            )
            self._started = True
            self._krpm = 1
        else:
            print(
                """
                Chigchig-chighi
                WrAAAsgg ArrArAnArn!!!!
                chigichiiigi
                WrAAAsgg ArrArAnArn!!!!
                """
            )
            self._started = True

    def kill(self):
        self._started = False
        self.fuel_injection_rate = 0  # ml/s
        self._krpm = 0


if __name__ == "__main__":
    nova = Car("Nova", 1978, "White")
    nova.start()
    nova.accelerate(10)
    print(nova.speed)
    nova.accelerate(10)
    print(nova.speed)
    nova.accelerate(100)
    print(nova.speed)
    nova.accelerate(100)
    print(nova.speed)
