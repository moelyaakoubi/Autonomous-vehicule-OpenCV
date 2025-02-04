import RPi.GPIO as GPIO
import time

class ServoMotor:
    def __init__(self, pin_number, frequency=50):
        self.pin = pin_number
        self.frequency = frequency
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm.start(0)
    
    def set_angle(self, angle):
        duty_cycle = self._angle_to_duty_cycle(angle)
        self.pwm.ChangeDutyCycle(duty_cycle)
    
    def _angle_to_duty_cycle(self, angle):
        duty_cycle = ((angle / 180.0) * 10) + 2.5
        return duty_cycle
    
    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()
