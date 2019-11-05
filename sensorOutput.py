import sensorLibrary as sl
import time as t
import os

counter = 1

while counter >=1:
    t.sleep(5)
    os.system('clear')
    print(" Accelerometer reads magnitude: " + str(sl.getAccelMag()))
    print("    Acceleration x is: " + str(sl.getAccel_x()))
    print("    Acceleration y is: " + str(sl.getAccel_y()))
    print("    Acceleration z is: " + str(sl.getAccel_z()))
    print("\n Magnetometer reads magnitude: " + str(sl.getMagMag()))
    print("    Magnetometer x is: " + str(sl.getMag_x()))
    print("    Magnetometer y is: " + str(sl.getMag_y()))
    print("    Magnetometer z is: " + str(sl.getMag_z()))
    print("\n Gyroscope reads magnitude: " + str(sl.getGyroMag()))
    print("    Gyroscope x is: " + str(sl.getGyro_x()))
    print("    Gyroscope y is: " + str(sl.getGyro_y()))
    print("    Gyroscope z is: " + str(sl.getGyro_z()))
