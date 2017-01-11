#!/usr/bin/env python
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import rospy
from std/msgs.msg import Int16
from servo.Adafruit_PWM_Servo_Driver import PWM
print "RIGHT SERVO_DRIVER successful import"
Rpwm = PWM(0x40, 1)
Rpwm.setPWMFreq(30)

def callback(data, servo):
    Rpwm.setPWM(servo, 0, data.data)

if __name__ == '__main__':
    rospy.init_node('Right_hand_driver', anonymous=True)
    for servo in range(1, 10):
        rospy.Subscriber('servo/R' + str(servo), Int16, callback=callback, callback_args=servo)
    print 'RIGHT SERVO_DRIVER publishers & subscribers successful Initial'
    rospy.spin()
