from MotorModules import Motor
from ServoModules import ServoMotor
from UltrasonicSensorMod import UltrasonicSensor
from time import sleep

# Initialize motors and servo
motor1 = Motor(2,3,4)
motor2 = Motor(17,27,22)
servo = ServoMotor(18)
ultrasonic_sensor = UltrasonicSensor(trig_pin=23, echo_pin=24)  # Adjust pins as per your setup

# Define functions for movement and actions
def move_forward(speed=50):
    motor1.Forward(speed)
    motor2.Forward(speed)
    sleep(2)

def move_backward(speed=30):
    motor1.Backward(speed)
    motor2.Backward(speed)
    sleep(2)

def stop_all(duration=0):
    motor1.stop(duration)
    motor2.stop(duration)
    sleep(duration)

def turn_left():
    servo.set_angle(70)
    sleep(2)

def turn_right():
    servo.set_angle(110)
    sleep(2)
    
def check_distance_threshold(threshold=20):
    distance = ultrasonic_sensor.get_distance()
    if distance < threshold:
        return True
    else:
        return False

if __name__ == '__main__':
       
    try:
        # Reset servo position at the beginning
        servo.set_angle(90)
        
        #while not check_distance_threshold():
        while True:
            # Perform movements and actions
            move_forward()
            stop_all(2)

            turn_left()
            stop_all(2)
            move_backward()
            stop_all(2)
            turn_right()
             
        
            
    except KeyboardInterrupt:
        servo.cleanup()
        stop_all()
            