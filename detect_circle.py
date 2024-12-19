import sys
from time import sleep
import glob
import serial
import cv2
import time
import numpy as np

COM_PORT = '/dev/ttyUSB0'  
BAUD_RATES = 9600

class GRIPPER():
    def __init__(self, COM_PORT, BAUD_RATES):
        self.COM_PORT = COM_PORT
        self.BAUD_RATES = BAUD_RATES
    def list_all_serial(self,):
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

    def init_port(self):
        comList= self.list_all_serial()
        print(f'comList,{comList}')
        if len(comList)==0:
            print('No Serial Found')
            exit()
        # default name: '/dev/ttyUSB0'
        COM_PORT = comList[0]
        print(f'COM_PORT: {COM_PORT}')
        self.ser = serial.Serial(COM_PORT, self.BAUD_RATES)

    def close(self):
        choice = 'c'
        print(f'Close: {choice}')
        self.ser.write(choice.encode())
        self.ser.write(b'\n')   # 发送换行符
        sleep(0.5)
    
    def open(self):
        choice = 'o'
        print(f'Open: {choice}')
        self.ser.write(choice.encode())
        self.ser.write(b'\n')   # 发送换行符
        sleep(0.5)

def get_circle_xy(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 霍夫圆变换
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]
            # 在图像上绘制检测到的圆
            cv2.circle(image, center, radius, (0, 255, 0), 2)
            # 标记圆心
            cv2.circle(image, center, 2, (0, 0, 255), 3)

        # 显示带有检测到的圆的图像
        image = cv2.resize(image, (960, 720))
        cv2.imshow('Detected Circles', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No circles detected.")
    
def pid_control(delta_x, delt_y):
    pass

flag = 0
gripper = GRIPPER(COM_PORT, BAUD_RATES)
gripper.init_port()
# i=ser.write(encoded)
# s=ser.readline()

video = cv2.VideoCapture(1)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)

while True:
    ret, image = video.read()
    if not ret: break
    # get_circle_xy(frame)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]
            # 在图像上绘制检测到的圆
            cv2.circle(image, center, radius, (0, 255, 0), 2)
            # 标记圆心
            cv2.circle(image, center, 2, (0, 0, 255), 3)

        # 显示带有检测到的圆的图像
        image = cv2.resize(image, (960, 720))
        cv2.imshow('Detected Circles', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        print("No circles detected.")

    # output = cv2.resize(frame, (960, 720))
    # cv2.imshow('Estimated Pose', output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# while d > threshold
    # 1.检测视频帧中圆心的坐标xy
    # 2.得到圆心坐标与相机中心距离差 delta_x, delt_y, d
    # if d < threshold: 
    #       flag = 1
    #       break
    # else 
    # PID_control(delta_x, delt_y)

if flag == 1:
    gripper.open()







