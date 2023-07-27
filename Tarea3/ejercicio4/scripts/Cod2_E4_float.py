#!/usr/bin/env python3
#publicador tipo float, rango de 0 a 100, de nombre
#random_float_Y
import rospy
from std_msgs.msg import Float64
import random

rospy.init_node('cod2_E4_float', anonymous=True)

pub = rospy.Publisher('random_float_Y', Float64, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valor= round(random.uniform(0, 100),2)
    print(valor)
    #rospy.loginfo("I send %f", valor)
    pub.publish(valor) # se publica el valor    
    rate.sleep() # delay de 1 segundo