# # import serial.tools.list_ports
# # ports = list(serial.tools.list_ports.comports())
# # for p in ports:
# #     print(p)
import serial
import time
ser = serial.Serial('/dev/ttyS10', 9600)

while 1:
	try:
	    #print "something"
	    #print ser.readline()
	    ser.write('5')
	    time.sleep(1)
	    ser.write('6')
	    time.sleep(1)
	except ser.SerialTimeoutException:
	    print 'Data could not be read'
	    time.sleep(1)


# import serial, time
# arduino = serial.Serial('/dev/ttyS10', 9600, timeout=.1)
# time.sleep(1) #give the connection a second to settle
# arduino.write("Hello from Python!")
# while True:
# 	data = arduino.readline()
# 	if data:
# 		print data.rstrip('\n') #strip out the new lines for now
# 		# (better to do .read() in the long run for this reason