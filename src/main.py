# import serial.tools.list_ports
# ports = list(serial.tools.list_ports.comports())
# for p in ports:
#     print(p)
import serial
import time
ser = serial.Serial('COM11', 9600)
 
while 1:
    try:
        print "something"
        print ser.readline()
        time.sleep(1)
    except ser.SerialTimeoutException:
        print 'Data could not be read'
        time.sleep(1)