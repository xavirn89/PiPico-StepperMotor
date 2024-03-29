import utime
from src.steppermotor import StepperMotor

step_pin = 17
dir_pin = 16
stepper = StepperMotor(dir_pin, step_pin)
 
def loop():
    while True:
        stepper.move(600, 2000, 5)  # 2 revolutions forward
        utime.sleep(1)
        stepper.move(-600, 2000, 5)  # 2 revolutions backward
        utime.sleep(1)
 
if __name__ == '__main__':
    loop()