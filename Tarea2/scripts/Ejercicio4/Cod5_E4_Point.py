#!/usr/bin/env python3

#Suscriptor que lee desde el publicador de nombre random_point
#
import rospy
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('Cod5_E4_Point', anonymous=True)	

float_valorX = 0
float_valorY = 0
float_valorZ = 0

#funcion para recibir el mensaje 
def callback(data):	
    global float_valorX,float_valorY,float_valorZ
    float_valorX =data.x
    float_valorY =data.y
    float_valorZ =data.z
    #print(float_value)
    rospy.loginfo("x: %f", float_valorX)
    rospy.loginfo("y: %f", float_valorY)
    rospy.loginfo("z: %f", float_valorZ)

# se suscribe al topico
sub = rospy.Subscriber("random_point", Point, callback)
# el codigo Cod4_E4_FyP.py publica al topico 'random_point'

rate = rospy.Rate(10) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    
    rate.sleep() # delay de 1 segundo