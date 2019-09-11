#!/usr/bin/env python3
import tkinter as tk
import rospy
print("rospy imported")
from mpu9250.msg import accelmsg
from mpu9250.msg import gyromsg
from mpu9250.msg import magmsg


def RecData(msg):
    rospy.init_node('mpu9250_toolbox', anonymous = True)
    rospy.Subscriber('mpu9250_data', msg, TkinterUI) 
    print("Waiting for Mpu9250 data")
    rospy.spin()

def TkinterUI(data):
    root = tk.Tk()

    GyroscopeText = ("Gyroscope X = %f \nGyroscope Y = %f \nGyroscope Z = %f ",data.gyrox, data.gyroy, data.gyroz)
    AccelerometerText = ("Accelerometer X = %f \nAccelerometer Y = %f \nAccelromter Z = %f", data.accelx, data.accely, data.accelz)
    MagnetometerText = ("Magnetometer X = %f \nMangetometer Y = %f \nMagnetometer Z = %f ", data.accelx, data.accely, data.accelz)

    GyroLabel = tk.Label(root, text = GyroscopeText, bg = "red", fg = "white")
    GyroLabel.pack(fill = tk.X)

    AccelLabel = tk.Label(root, text = AccelerometerText, bg = "blue", fg = "white")
    AccelLabel.pack(fill = tk.X)

    Magnetometer = tk.Label(root, text = MagnetometerText, bg = "green",fg = "white")
    Magnetometer.pack(fill = tk.X)

    tk.mainloop()

while True :
    try: 
        RecData(accelmsg)
        RecData(gyromsg)
        RecData(magmsg)
    except rospy.ROSInterruptException:
        pass
