import time as t
import os

from sensor_library import Sensor

while True:
    t.sleep(5)
    os.system('clear')
    sensor = Sensor()
    print(' Accelerometer reads magnitude: {}'
          '\tAcceleration x is: {}'
          '\tAcceleration y is: {}'
          '\tAcceleration z is: {}\n'.format(
            sensor.accel_mag,
            sensor.accel_x,
            sensor.accel_y,
            sensor.accel_z))
    print(' Magnetometer reads magnitude: {}'
          '\tMagnetometer x is: {}'
          '\tMagnetometer y is: {}'
          '\tMagnetometer z is: {}\n'.format(
            sensor.mag_mag,
            sensor.mag_x,
            sensor.mag_y,
            sensor.mag_z))
    print(' Gyroscope reads magnitude: {}'
          '\tGyroscope x is: {}'
          '\tGyroscope y is: {}'
          '\tGyroscope z is: {}\n'.format(
            sensor.gyro_mag,
            sensor.gyro_x,
            sensor.gyro_y,
            sensor.gyro_z))
