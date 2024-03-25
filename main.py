import machine
import utime
from src.steppermotor import StepperMotor

# Define constants
STEPS_PER_REV = 200

# The pins used are 1,2,3,4 
# Connected to L298N Motor Driver In1, In2, In3, In4 
# Pins entered in sequence 1-2-3-4 for proper step sequencing
stepper = StepperMotor(STEPS_PER_REV, 1, 2, 3, 4)

# Analog pin for the speed control potentiometer
speed_control = machine.ADC(26)  # ADC on GP26

def main():
    while True:
        # Read the sensor value
        sensor_reading = speed_control.read_u16()

        # Map it to a range from 0 to 100
        motor_speed = sensor_reading / 65535 * 100

        # Set the motor speed
        if motor_speed > 0:
            stepper.set_speed(motor_speed)
            # Step 1/100 of a revolution
            stepper.step(STEPS_PER_REV / 100)
        utime.sleep(0.01)  # Small delay to prevent overwhelming the CPU

if __name__ == "__main__":
    main()