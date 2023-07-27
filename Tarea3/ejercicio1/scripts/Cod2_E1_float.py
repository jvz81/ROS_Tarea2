#!/usr/bin/env python3

#suscriptor tipo float
import rospy
from std_msgs.msg import Float64

# el codigo se identifica ante ros
rospy.init_node('Cod2_E1_float', anonymous=True)	

float_value=0

#funcion para recibir el mensaje 
def callback(data):	
    global float_value
    float_value=data.data
    #print(float_value)
    rospy.loginfo("valor: %f", float_value)

# se suscribe al topico
sub = rospy.Subscriber("random_float_E1", Float64, callback)
# el codigo Cod1_float.py publica al topico 'random_float'

rate = rospy.Rate(5) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    rate.sleep() # delay de 1 segundo