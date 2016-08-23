import mraa   # on ubilinux, dl & blt v0.8.1, but only works as sudo?
import time
import serial
import datetime

y=mraa.Uart(0)            # libmraa should configure the gpio ports
port = y.getDevicePath()  # and provide the devicepath name
print 'Opening Uart(0): %s' % port
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(port,19200)

#ser.open()
ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1 :
    # get keyboard input
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    input = raw_input(st+">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # Kangaroo x2 Simplified Serial Commands:  <Channel> <,> <Command> <\n> 
        ser.write(input + '\n')
    	out = ''
        # let's wait .25 second before reading output (let's give device time to answer)
        time.sleep(.25)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            print st + ">> " + out

