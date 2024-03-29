from machine import Pin, Timer
import utime

class StepperMotor:
    def __init__(self, dir_pin, step_pin, steps_per_revolution=200):
        self.dir_pin = Pin(dir_pin, Pin.OUT)
        self.step_pin = Pin(step_pin, Pin.OUT)
        self.steps_per_revolution = steps_per_revolution
        self.running = False
        self.delay = 1000
        self.direction = 0
        self.step_count = 0
        self.timer = Timer()
    
    def step(self, t):
        if self.step_count < self.steps_per_revolution:
            self.step_pin.value(not self.step_pin.value())
            self.step_count += 1
        else:
            self.stop()
            if self.running:
                self.start_moving()
    
    def start_moving(self):
        self.step_count = 0
        self.dir_pin.value(self.direction)
        self.timer.init(freq=1000000/self.delay, mode=Timer.PERIODIC, callback=self.step) # type: ignore
    
    def stop(self):
        utime.sleep_ms(200)
        self.timer.deinit()
        self.step_count = 0
