
import serial
import time


ser = serial.Serial('/dev/ttyS10', 9600) // change based on your own port


# Turns the motor once based on the calibration
def motorClockwiseOnce(char motorNum){
	
	
	try:
	    ser.write(motorNum)
	except ser.SerialTimeoutException:
	    print 'Data could not be read'
	    time.sleep(1)

}




