import sensorLibrary.py
import time;
i = 1;

while i < 100:
    print(getAccel_x());
    print(getGyro_x());
    print(getMag_x());
    i+1;