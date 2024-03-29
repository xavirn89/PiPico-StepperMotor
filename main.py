from machine import Pin
import utime
from src.steppermotor import StepperMotor

step_pin = 17
dir_pin = 16
stepper = StepperMotor(dir_pin, step_pin)
switch_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)
 
def loop():
    while True:
        switch_state = switch_pin.value()
        if switch_state:
            stepper.move(600, 2000, 5)  # 2 revolutions forward
        else:
            stepper.move(-600, 2000, 5)  # 2 revolutions backward
        utime.sleep(1)
 
if __name__ == '__main__':
    loop()