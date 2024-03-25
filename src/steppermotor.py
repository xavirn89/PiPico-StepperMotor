import machine
import utime

class StepperMotor:
    def __init__(self, steps_per_rev, pin1, pin2, pin3, pin4):
        self.steps_per_rev = steps_per_rev
        self.pins = [machine.Pin(pin, machine.Pin.OUT) for pin in [pin1, pin2, pin3, pin4]]
        self.step_sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]
        self.step_count = len(self.step_sequence)
        self.step_index = 0
        self.delay = 0

    def set_speed(self, speed):
        # Speed is given as a percentage of the maximum speed
        # We convert it to a delay in milliseconds between steps
        self.delay = (1 - speed / 100) * 0.01

    def step(self, steps):
        for _ in range(int(steps)):
            for pin, value in zip(self.pins, self.step_sequence[self.step_index]):
                pin.value(value)
            utime.sleep(self.delay)
            self.step_index += 1
            if self.step_index == self.step_count:
                self.step_index = 0