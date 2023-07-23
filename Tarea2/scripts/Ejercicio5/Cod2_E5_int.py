#!/usr/bin/env python3
#publicador tipo int, rango de 0 a 100, de nombre
#random_int_n2
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('cod2_E5_int', anonymous=True)

pub = rospy.Publisher('random_int_n2', Int32, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valor= random.randint(0,100)
    print(valor)
    #rospy.loginfo("I send %f", valor)
    pub.publish(valor) # se publica el valor    
    rate.sleep() # delay de 1 segundo