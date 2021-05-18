# Tutorial_ https://github.com/oscgonfer/sensors_dsp_lectures/blob/master/02_datalogging/examples/python_serial.py


# Import packages
import serial
import datetime
import glob
import sys
from sys import stdout

# Numpy
import numpy as np

BAUDRATE = 115200


def serial_ports():
    """Lists serial ports
    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []

    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def ReadSerial(serial):
    return serial.readline().decode().replace("\r\n", "")


# Retrieve constants (ports, time, header)
ports = serial_ports()
# print (ports)
ser = serial.Serial(ports[1], BAUDRATE)

filename = 'log.csv'

# Create header
with open(filename, 'a') as file:
    file.write(f"TIME,READING\n")

# Create the reading
while True:
    timestamp = datetime.datetime.now()
    timestamp_formatted = str(timestamp.year) + "-" + str(timestamp.month) + "-" + str(timestamp.day) + "-" + str(
        timestamp.hour) + "-" + str(timestamp.minute) + "-" + str(timestamp.second)
    reading = ReadSerial(ser)
    try:
        reading_formatted = float(reading)
        if reading_formatted< 10:
            reading_formatted="null"
        print(reading_formatted)

        with open(filename, 'a') as file:
            file.write(f"{timestamp_formatted},{reading_formatted}\n")
        sys.stdout.flush()
    except Exception as e:
        print("error:"+reading)



