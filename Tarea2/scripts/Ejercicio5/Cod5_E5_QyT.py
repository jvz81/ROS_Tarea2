#!/usr/bin/env python3

#Suscriptor que lee random_quat (x,y,z,w) y luego Publica un 
#twist  random_twist (x,y,z,w,p,r) donde p = x+y+z+w y r = p^2

import rospy
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('Cod5_E5_QyT', anonymous=True)	

int_X = 0
int_Y = 0
int_Z = 0
int_W = 0
#funcion para recibir el mensaje 
def callback(data):	
    global int_X, int_Y, int_Z, int_W
    int_X=data.x
    int_Y=data.y
    int_Z=data.z
    int_W=data.w
    #print(int_X)
    #rospy.loginfo("I heard %f", int_X)

# se suscribe al topico
sub = rospy.Subscriber('random_quat', Quaternion, callback)


# el codigo  publica al topico 'random_twist'

pub = rospy.Publisher('random_twist', Twist, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    int_P = int_X + int_Y + int_Z + int_W
    int_R = int_P*int_P
    valorTwist = Twist()
    valorTwist.linear.x = int_X
    valorTwist.linear.y = int_Y
    valorTwist.linear.z = int_Z
    valorTwist.angular.x = int_W
    valorTwist.angular.y = int_P
    valorTwist.angular.z = int_R
    print(valorTwist)
    pub.publish(valorTwist)
    rate.sleep() # delay de 1 segundo