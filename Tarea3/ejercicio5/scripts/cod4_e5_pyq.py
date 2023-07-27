#!/usr/bin/env python3

#Suscriptor que lee random_point (x,y,z) y luego Publica un 
#quaternion  random_quat (x,y,z,w) donde w = x+y+z

import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from std_msgs.msg import Int32
# el codigo se identifica ante ros
rospy.init_node('cod4_e5_pyq', anonymous=True)	

int_X = 0
int_Y = 0
int_Z = 0
#funcion para recibir el mensaje 
def callback(data):	
    global int_X, int_Y, int_Z
    int_X=data.x
    int_Y=data.y
    int_Z=data.z
    #print(int_X)
    #rospy.loginfo("I heard %f", int_X)

# se suscribe al topico
sub1 = rospy.Subscriber('random_point', Point, callback)


# el codigo Cod1_float.py publica al topico 'random_float'

pub = rospy.Publisher('random_quat', Quaternion, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    int_W = int_X + int_Y + int_Z
    valorQuat = Quaternion(int_X,int_Y,int_Z,int_W)
    print(valorQuat)
    pub.publish(valorQuat)
    rate.sleep() # delay de 1 segundo