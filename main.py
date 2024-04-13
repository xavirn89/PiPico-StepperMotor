from machine import Pin, ADC
import utime

# Configuration constants
DIRECTION_BUTTON_PIN = 14
ON_OFF_BUTTON_PIN = 15
DIR_PIN = 16
STEP_PIN = 17
POTENTIOMETER_PIN = 26
STEPS_PER_REVOLUTION = 200

# Initialize hardware interfaces
direction_button = Pin(DIRECTION_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)
onoff_button = Pin(ON_OFF_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)
dirPin = Pin(DIR_PIN, Pin.OUT)
stepPin = Pin(STEP_PIN, Pin.OUT)
potentiometer = ADC(POTENTIOMETER_PIN)

# Global variables
last_direction = None
speed = 0

def map_val(value, in_min, in_max, out_min, out_max):
    """Map a value from one range to another."""
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def initialize_pins():
    """Set motor control pins to a default low state at startup."""
    dirPin.low()
    stepPin.low()

def check_direction_change():
    """Check and update motor direction with change detection."""
    global last_direction
    current_direction = direction_button.value()
    
    # Check if direction has changed
    if last_direction is not None and last_direction != current_direction:
        print("Direction change detected, pausing...")
        utime.sleep(0.2)  # Pause for direction change handling
    
    # Update motor direction state
    dirPin.value(current_direction)
    print("Motor direction set to:", "CW" if current_direction else "CCW")
    last_direction = current_direction

def move_motor():
    """Rotate the motor based on the current speed setting."""
    for _ in range(STEPS_PER_REVOLUTION):
        stepPin.high()
        utime.sleep_us(int(speed))
        stepPin.low()
        utime.sleep_us(int(speed))

def update_motor_speed():
    """Read potentiometer value and update motor speed accordingly."""
    global speed
    potentiometer_reading = potentiometer.read_u16()
    speed = map_val(potentiometer_reading, 0, 65535, 4000, 750)
    print("Custom speed set to:", speed)

def main():
    """Main program execution loop."""
    utime.sleep(1)
    initialize_pins()

    while True:
        if onoff_button.value():
            update_motor_speed()
            check_direction_change()
            move_motor()

if __name__ == '__main__':
    main()
