import board6;
import busio78;
import adafruit_fxas21002c;
import adafruit_fxos8700;

i2c = busio.I2C(board.SCL, board.SDA);
sensor = adafruit_fxas21002c.FXAS21002C(i2c);
sensor = adafruit_fxos8700.FXOS8700(i2c);


#getAcc reads sensor data from accelerometer
def getAccel_x():
    return sensor.accelerometer[0];

def getAccel_y():
    return sensor.accelerometer[1];

def getAccel_z():
    return sensor.accelerometer[2];


#getGyro reads gyroscope values
def getGyro_x():
    return sensor.gyroscope[0];

def getGyro_y():
    return sensor.gyroscope[1];

def getGyro_z():
    return sensor.gyroscope[2];


#getMag reads magnetometer values
def getMag_x():
   return sensor.magnetometer[0];

def getMag_y():
    return sensor.magnetometer[1];

def getMag_z():
    return sensor.magnetometer[2];
