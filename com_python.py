import sys
from time import sleep
import glob
import serial
# import board
# import busio
# import adafruit_mcp4728


# from adafruit_servokit import ServoKit

COM_PORT = '/dev/ttyUSB0'  # 請自行修改序列埠名稱
BAUD_RATES = 9600

def list_all_serial():
   """ Lists serial port names

       :raises EnvironmentError:
           On unsupported or unknown platforms
       :returns:
       A list of the serial ports available on the system
   """
   if sys.platform.startswith('win'):
       ports = ['COM%s' % (i + 1) for i in range(256)]
   elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
       # this excludes your current terminal "/dev/tty"
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
def intiArm(BAUD_RATES, COM_PORT ='/dev/ttyUSB0'):
   comList=list_all_serial()
   print(f'comList,{comList}')
   if len(comList)==0:
       print('No Serial Found')
       exit()
   # default name: '/dev/ttyUSB0'
   COM_PORT = comList[0]
   print(f'COM_PORT: {COM_PORT}')
   ser = serial.Serial(COM_PORT, BAUD_RATES)
   return ser
ser = intiArm(BAUD_RATES, COM_PORT )
# i=ser.write(encoded)
# s=ser.readline()



# i2c = busio.I2C(board.SCL, board.SDA)
# i2c = board.I2C()   # uses board.SCL and board.SDA
# kit = ServoKit(channels=16, i2c=(busio.I2C(board.SCL, board.SDA)))
# mcp4728 =  adafruit_mcp4728.MCP4728(i2c)


# mcp4728.channel_b.value = int(65535/2) # VDD/2
# mcp4728.channel_c.value = int(65535/4) # VDD/4
# mcp4728.channel_d.value = 0 # 0V

try:
   while True:
       # 接收用戶的輸入值並轉成小寫
       # choice = input('TYPE: 0 to open, 1 to flex-flip, 2 to close, other num below 255 to test').lower()
       choice = input('TYPE: 0 to 4 to represent the voltage(B3.5):\n').lower()
       if choice == 'e':
           ser.close()
           print('再見！')
           sys.exit()            
       else: 
           # choice = float(choice)
           # mcp4728.channel_a.value = 65535/5.0 * choice  # Voltage = VDD
           print(f'Sending command:{choice}')
           ser.write(choice.encode())
           ser.write(b'\n')
           sleep(0.5)

       # check if there is data available to read.
       while ser.in_waiting:
           mcu_feedback = ser.readline().decode()  
           print('Feedback:', mcu_feedback)
           
except KeyboardInterrupt:
   ser.close()
   print('再見！')

