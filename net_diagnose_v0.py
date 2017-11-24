import os
import RPi.GPIO as GPIO
import time

def bibi_short(args):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(11, GPIO.LOW)
    time.sleep(1)

def bibi_long(args):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(11, GPIO.LOW)
    time.sleep(1)

def bibi_long3s(args):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(11, GPIO.LOW)
    time.sleep(1)

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

def check_net():
   return1=os.system('ping www.baidu.com -c 1 -w 1000')
   #print return1
   if return1:
       print 'ping fail'
       bibi_long3s('')
   else:
       print 'ping ok'
       bibi_short('')
       time.sleep(2)


init()
bibi_long3s('')

count = 0
while (count < 9):
   #print 'The count is:', count
   #count = count + 1
   check_net()
