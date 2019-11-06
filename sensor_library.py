import board
import busio
import adafruit_fxas21002c
import adafruit_fxos8700

from enum import Enum


class Sensor:
    def __init__(self):
        self._i2c = busio.I2C(board.SCL, board.SDA)
        self._sensor_gyro = adafruit_fxas21002c.FXAS21002C(self._i2c)
        self._sensor = adafruit_fxos8700.FXOS8700(self._i2c)

    # getAcc reads sensor data from accelerometer
    @property
    def accel_x(self):
        return self._sensor.accelerometer[SensorAxis.X]

    @property
    def accel_y(self):
        return self._sensor.accelerometer[SensorAxis.Y]

    @property
    def accel_z(self):
        return self._sensor.accelerometer[SensorAxis.Z]

    @property
    def accel_mag(self):
        return None

    # getGyro reads gyroscope values
    @property
    def gyro_x(self):
        return self._sensor_gyro.gyroscope[SensorAxis.X]

    @property
    def gyro_y(self):
        return self._sensor_gyro.gyroscope[SensorAxis.Y]

    @property
    def gyro_z(self):
        return self._sensor_gyro.gyroscope[SensorAxis.Z]

    @property
    def gyro_mag(self):
        return None
    # getMag reads magnetometer values
    @property
    def mag_x(self):
        return self._sensor.magnetometer[SensorAxis.X]

    @property
    def mag_y(self):
        return self._sensor.magnetometer[SensorAxis.Y]

    @property
    def mag_z(self):
        return self._sensor.magnetometer[SensorAxis.Z]

    @property
    def mag_mag(self):
        return None

class SensorAxis(Enum):
    X = 0
    Y = 1
    Z = 2
