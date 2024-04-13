from machine import Pin
import utime

# Pin configuration
DIRECTION_BUTTON_PIN = 14
ON_OFF_BUTTON_PIN = 15
DIR_PIN = 16
STEP_PIN = 17

# Motor configuration
SPEED_MICROSECONDS = 1000
STEPS_PER_REVOLUTION = 200

# Initialize pins
direction_button = Pin(DIRECTION_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)
onoff_button = Pin(ON_OFF_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)
dirPin = Pin(DIR_PIN, Pin.OUT)
stepPin = Pin(STEP_PIN, Pin.OUT)

# Initialize last known direction, None means no previous direction yet
last_direction = None

def initialize_pins():
    """Set the motor control pins to a known low state."""
    dirPin.low()
    stepPin.low()

def check_direction():
    """Set the motor direction based on the state of the direction button and check for changes."""
    global last_direction
    current_direction = direction_button.value()
    
    if current_direction == 1:
        dirPin.high()
        print("Direction button in CW")
    else:
        dirPin.low()
        print("Direction button in CCW")

    # If the direction has changed, reset the step count
    if last_direction != current_direction:
        utime.sleep(0.2)

    # Update the last direction to the current
    last_direction = current_direction

def move_motor():
    """Rotate the motor one full revolution, depending on the direction."""
    for _ in range(STEPS_PER_REVOLUTION):
        stepPin.high()
        utime.sleep_us(SPEED_MICROSECONDS)
        stepPin.low()
        utime.sleep_us(SPEED_MICROSECONDS)

def main():
    """Main program loop."""
    utime.sleep(1)  # Allow system to stabilize after power-up
    initialize_pins()
    utime.sleep(1)  # Short delay after initializing pins

    while True:
        if onoff_button.value() == 1:  # Only act if the on-off button is pressed
            check_direction()
            move_motor()

if __name__ == '__main__':
    main()
