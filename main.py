from machine import Pin
import utime
from src.steppermotor import StepperMotor

def initialize_pins():
    # Initialize step and direction pins to low
    Pin(16, Pin.OUT).value(0)
    Pin(17, Pin.OUT).value(0)

if __name__ == '__main__':
    utime.sleep(1)  # Wait for 1 second to ensure system stability
    initialize_pins()
    utime.sleep(1)
    
    direction_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)
    onoff_pin = Pin(15, Pin.IN, Pin.PULL_DOWN)
    
    #dir_pin = 16, step_pin = 17
    stepper_motor = StepperMotor(16, 17, 200)
    
    while True:
        current_direction = direction_pin.value()
        motor_should_run = onoff_pin.value()
        print("On/Off: ", motor_should_run, "Direction: ", current_direction)
        if motor_should_run and not stepper_motor.running:
            stepper_motor.running = True
            stepper_motor.direction = current_direction
            stepper_motor.start_moving()
        elif not motor_should_run and stepper_motor.running:
            stepper_motor.running = False
            stepper_motor.stop()
        elif motor_should_run and (stepper_motor.direction != current_direction):
            stepper_motor.direction = current_direction
            stepper_motor.start_moving()
        
        utime.sleep(0.1)  # Short delay to debounce and reduce CPU usage
