#!/usr/bin/env python3

#Suscriptor que lee desde 3 publicadores valores de X, Y y Z
#(random_float_X,random_float_Y,random_float_Z)
#para despues generar un punto (Point)

#Luego publica un punto_leido
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Point

# el codigo se identifica ante ros
rospy.init_node('cod4_e4_fyp', anonymous=True)	

float_valueX=0
float_valueY=0
float_valueZ=0


#funcion para recibir el mensaje de X
def callback_X(data):	
    global float_valueX
    float_valueX=data.data
    #print(float_value)
    #rospy.loginfo("I heard %f", float_valueX)

#funcion para recibir el mensaje de Y
def callback_Y(data):	
    global float_valueY
    float_valueY=data.data
    #print(float_value)
    #rospy.loginfo("I heard %f", float_valueY)

#funcion para recibir el mensaje de Z
def callback_Z(data):	
    global float_valueZ
    float_valueZ=data.data
    #print(float_value)
    #rospy.loginfo("I heard %f", float_valueZ)


# se suscribe a los topicos
sub_X = rospy.Subscriber("random_float_X", Float64, callback_X)
sub_Y = rospy.Subscriber("random_float_Y", Float64, callback_Y)
sub_Z = rospy.Subscriber("random_float_Z", Float64, callback_Z)

#Ahora se publica el punto'

pub = rospy.Publisher('random_point', Point, queue_size=1)

rate = rospy.Rate(1) # 10hz --> 1/10hz=0.1s
while not rospy.is_shutdown():
    valorPunto = Point(float_valueX,float_valueY,float_valueZ)
    print(valorPunto)
    pub.publish(valorPunto)
    rate.sleep() # delay de 1 segundo