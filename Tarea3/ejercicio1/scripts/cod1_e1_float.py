#!/usr/bin/env python3
#publicador tipo float
import rospy
from std_msgs.msg import Float64
import random

rospy.init_node('cod1_e1_float', anonymous=True)

pub = rospy.Publisher('random_float_E1', Float64, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valor= round(random.uniform(0, 1),2)
    print(valor)
    #rospy.loginfo("I send %f", valor)
    pub.publish(valor) # se publica el valor    
    rate.sleep() # delay de 1 segundo