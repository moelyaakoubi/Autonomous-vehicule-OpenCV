import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self, trig_pin):
        self.trig_pin = trig_pin
        GPIO.setup(self.trig_pin, GPIO.OUT)

    def measure_in_inches(self):
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)

        pulse_start = time.time()
        while GPIO.input(self.trig_pin) == 0:
            pulse_start = time.time()

        pulse_end = time.time()
        while GPIO.input(self.trig_pin) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 148.0  # Speed of sound in inches per second (in inches)
        return distance

    def measure_in_centimeters(self):
        distance_inches = self.measure_in_inches()
        distance_cm = distance_inches * 2.54  # Convert inches to centimeters
        return distance_cm

# Set GPIO mode (BCM numbering)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Define GPIO pins
TRIG_PIN = 7

if __name__ == '__main__':

    try:
        ultrasonic = Ultrasonic(TRIG_PIN)
        while True:
            range_inches = ultrasonic.measure_in_inches()
            print("The distance to obstacles in front is: %.2f inch" % range_inches)

            range_cm = ultrasonic.measure_in_centimeters()
            print("The distance to obstacles in front is: %.2f cm" % range_cm)

            time.sleep(0.1)  # Delay between measurements

    except KeyboardInterrupt:
        GPIO.cleanup()
