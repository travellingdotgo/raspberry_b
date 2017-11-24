import os
import RPi.GPIO as GPIO
import time


def bibi_timed(args):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(args)
    GPIO.output(11, GPIO.LOW)
    time.sleep(1)

def bibi_short(args):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(11, GPIO.LOW)
    time.sleep(1)

def bibi_loop(args):
    for i in range(1, 6):
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.1)

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
   start = time.time()
   return1=os.system('ping www.baidu.com -c 1 -w 1000')
   elapsed = (time.time() - start)
   print("elapsed: ",elapsed)
   if return1:
       print 'ping fail'
       bibi_loop('')
       time.sleep(2)
   else:
       print 'ping ok'
       bibi_timed(elapsed/5.0)
       time.sleep(2)


init()
bibi_timed(1)

count = 0
while (count < 9):
   #print 'The count is:', count
   #count = count + 1
   check_net()
