#!/usr/bin/env python3
#publicador tipo float, rango de 0 a 2.50, de nombre
#random_float
import rospy
from std_msgs.msg import Float64
import random

rospy.init_node('cod1_E2_float', anonymous=True)

pub = rospy.Publisher('random_float', Float64, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valor= round(random.uniform(0, 2.5),2)
    print(valor)
    #rospy.loginfo("I send %f", valor)
    pub.publish(valor) # se publica el valor    
    rate.sleep() # delay de 1 segundo