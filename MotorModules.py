import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, Ena, In1,In2):
        self.Ena=Ena
        self.In1=In1
        self.In2=In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwm=GPIO.PWM(self.Ena,100)
        self.pwm.start(0)

    def Forward(self,Speed):
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)
        self.pwm.ChangeDutyCycle(abs(Speed))

    def  Backward(self,Speed):
        GPIO.output(self.In2,GPIO.HIGH)
        GPIO.output(self.In1,GPIO.LOW)
        self.pwm.ChangeDutyCycle(abs(Speed))

    def stop(self,t=0):
        self.pwm.ChangeDutyCycle(0)
       
