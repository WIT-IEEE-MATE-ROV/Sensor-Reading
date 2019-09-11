#!/usr/bin/env python3
import rospy
import FaBo9Axis_MPU9250
import time
import sys
from mpu9250.msg import accelmsg
from mpu9250.msg import gyromsg
from mpu9250.msg import magmsg
mpu = FaBo9Axis_MPU9250.MPU9250()

def Publisher(msg,Data1,Data2,Data3):
    pub = rospy.Publisher('mpu9250_data', msg, queue_size = 10)
    rospy.init_node('mpu9250', anonymous = true)
    pub.publish(Data1,Data2,Data3)
    
try:
     while True:
         accel = mpu.readAccel()
         accelX = accel['x']
         accelY = accel['y']
         accelZ = accel['z']
         
         gyro = mpu.readGyro()
         gyroX = gyro['x']
         gyroY = gyro['y']
         gyroz = gyro['z']

         mag = mpu.readMagnet()
         magX = mag['x']
         magY = mag['y']
         magZ = mag['z']

         Publisher(accelmsg,accelX,accelY,accelZ)
         Publisher(gyromsg,gyroX,gyroY,gyroZ)
         Publisher(magmsg,magX,magY,magZ)

         time.sleep(0.5)
except KeyboardInterrupt:
    sys.exit()
