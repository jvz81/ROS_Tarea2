#!/usr/bin/env python3

#Suscriptor que lee desde dos publicadores de nombre random_int_n1
#random_int_n2 
#tambien es publicador de int_suma
import rospy
from std_msgs.msg import Int32

# el codigo se identifica ante ros
rospy.init_node('cod3_e3_int', anonymous=True)	

int_n1=0
int_n2=0
#funcion para recibir el mensaje 
def callback(data):	
    global int_n1
    int_n1=data.data
    #print(float_value)
    #rospy.loginfo("I heard %f", float_value)

def callback_n2(data):	
    global  int_n2
    int_n2=data.data

# se suscribe al topico
sub1 = rospy.Subscriber("random_int_n1", Int32, callback)
sub2 = rospy.Subscriber("random_int_n2", Int32, callback_n2)
# el codigo Cod1_float.py publica al topico 'random_float'

pub = rospy.Publisher('random_int_suma', Int32, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valor = int_n1 + int_n2
    print(valor)
    pub.publish(valor)
    rate.sleep() # delay de 1 segundo