#!/usr/bin/env python3

#Suscriptor que lee desde dos publicadores de nombre random_int_n1
#random_int_n2, a partir de esto valores crea un n3 = n1 + n2
#tambien es publicador de un punto como random_point, que tiene
#point.x = n1, point.y = n2, point.z = n3
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Int32
# el codigo se identifica ante ros
rospy.init_node('cod3_e5_iyp', anonymous=True)	

int_X = 0
int_Y = 0

#funcion para recibir el mensaje 
def callback_n1(data):	
    global int_X
    int_X=data.data
    #print(int_X)
    #rospy.loginfo("I heard %f", int_X)

def callback_n2(data):	
    global  int_Y
    int_Y=data.data
    #print(int_Y)
    #rospy.loginfo("I heard %f", int_Y)


# se suscribe al topico
sub1 = rospy.Subscriber("random_int_n1", Int32, callback_n1)
sub2 = rospy.Subscriber("random_int_n2", Int32, callback_n2)

# el codigo Cod1_float.py publica al topico 'random_float'

pub = rospy.Publisher('random_point', Point, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    int_Z = int_X + int_Y
    valorPunto = Point(int_X,int_Y,int_Z)
    print(valorPunto)
    pub.publish(valorPunto)
    rate.sleep() # delay de 1 segundo