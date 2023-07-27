#!/usr/bin/env python3
#Suscriptor que solo lee del publicador random_twist (x,y,z,w,p,r)
#
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('cod6_e5_twist', anonymous=True)	

int_X=0
int_Y=0
int_Z=0
int_W=0
int_P=0
int_R=0
#funcion para recibir el mensaje 
def callback(data):	
    global int_X,int_Y,int_Z,int_W,int_P,int_R
    int_X=data.linear.x
    int_Y=data.linear.y
    int_Z=data.linear.z
    int_W=data.angular.x
    int_P=data.angular.y
    int_R=data.angular.z
    #print(int_value)
    rospy.loginfo("Twist: ")
    rospy.loginfo("linear.x %i", int_X)
    rospy.loginfo("linear.y %i", int_Y)
    rospy.loginfo("linear.z %i", int_Z)
    rospy.loginfo("angular.x %i", int_W)
    rospy.loginfo("angular.y %i", int_P)
    rospy.loginfo("angular.z %i", int_R)

# se suscribe al topico
sub = rospy.Subscriber('random_twist', Twist, callback)


rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    
    rate.sleep() # delay de 1 segundo