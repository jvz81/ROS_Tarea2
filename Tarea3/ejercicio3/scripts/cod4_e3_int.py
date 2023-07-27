#!/usr/bin/env python3

#Suscriptor que lee desde el publicador de nombre 
#random_int_suma
import rospy
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('cod4_e3_int', anonymous=True)	

int_value=0

#funcion para recibir el mensaje 
def callback(data):	
    global int_value
    int_value=data.data
    #print(int_value)
    rospy.loginfo("valor: %f", int_value)

# se suscribe al topico
sub = rospy.Subscriber('random_int_suma', Int32, callback)


rate = rospy.Rate(10) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    
    rate.sleep() # delay de 1 segundo