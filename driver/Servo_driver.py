#!/usr/bin/env python
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import rospy
from right_hand.msg import servoSet, servoCmd
from servo.Adafruit_PWM_Servo_Driver import PWM
print "RIGHT SERVO_DRIVER successful import"
Rpwm = PWM(0x40, 1)
Rpwm.setPWMFreq(30)




def doIt(Rcmd):
    Rpwm.setPWM(1, 0, Rcmd[0])
    Rpwm.setPWM(2, 0, Rcmd[1])
    Rpwm.setPWM(3, 0, Rcmd[2])
    Rpwm.setPWM(4, 0, Rcmd[3])
    Rpwm.setPWM(5, 0, Rcmd[4])
    Rpwm.setPWM(6, 0, Rcmd[5])
    Rpwm.setPWM(7, 0, Rcmd[6])
    Rpwm.setPWM(8, 0, Rcmd[7])
    Rpwm.setPWM(9, 0, Rcmd[8])

    


def CALLBACK(data):
    print data
    doIt(data.cmd)

def callback(data):
    print data
    Rpwm.setPWM(data.motor, 0, data.command)



if __name__ == '__main__':

    rospy.init_node('Right_hand_driver', anonymous=True)
    rospy.Subscriber('servo/Rcmd', servoSet, callback=CALLBACK)
    rospy.Subscriber('servo/rcmd', servoCmd, callback=callback)
    print 'RIGHT SERVO_DRIVER publishers & subscribers successful Initial'
    rospy.spin()
