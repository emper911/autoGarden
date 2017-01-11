import time
import RPi.GPIO as GPIO
from gpiozero import LED, Button

#GPIO pins
motor = LED(4)
lights = LED(23)
ONOFF_Button = Button(21)
motorTime_Button = Button(5)
lightTime_Button = Button(25)
start = False #when button is pressed to begin
#light times hrs15 = 54000.00, hrs12  = 43200.00, hrs13 = 46800.00, hrs24 = 86400.00, hr = 3600
#light time default is 13 hrs
hrs = 46800.00
#motor times default is 1 min on and 4 minutes off
tMotorOn = 60.00
tMotorOff = 240.00  #increments of 30 seconds
motorTime = 0
currentTime = 0
LEDTime = 0

def LEDTimer():
    global LEDTime
    if (time.time() - LEDTime) < hrs:
        lights.on()
    elif (time.time() - LEDTime) < hrs24:
        lights.off()
    else:
        LEDTime = time.time()

def motorTimer():
    global motorTime
    global LEDTime
    if (time.time() - motorTime) < tMotorOn:
        motor.on()
    elif (time.time() - motorTime) < tMotorOff:
        motor.off()
    else:
        printer(LEDTime)
        motorTime = time.time()
    
def motorTimeButtonPress():
    global tMotorOn
    global tMotorOff
    if tMotorOn == 90.00: #maximum time on is 1min and 30secs
        tMotorOn = 30.00
        tMotorOff = 270.00
    else:
        tMotorOn = tMotorOn + 30.00
        tMotorOff = tMotorOff - 30.00

def lightTimeButtonPress():
    global hrs
    if hrs == 54000.00:#15hrs is maximum
        hrs = 39600.00 #resets to 11hrs
    else:
        hrs = hrs + 3600.00
    print("Light is on for: " + hrs/3600.00 + ".\n")
        
while True:
    motor.off()
    lights.off()
    #when program is turned on waiting for button to be pressed to turn on garden
    if ONOFF_Button.is_pressed:
        time.sleep(1)
        print("Garden is On")
        start = True
        currentTime = time.time()
        LEDTime = time.time()
        motorTime = time.time()
    #when button is pressed program starts
    while start:#on/off button
        #if button is pressed again program terminates into user determined loop
        LEDTimer()
        motorTimer()
        tempHumSensor()
        if ONOFF_Button.is_pressed:
            time.sleep(1)
            start = False
            print("Garden is Off")
        if motorTime_button.is_pressed:
            motorTimeButtonPress()
        if lightTime_Button.is_pressed:
            lightTimeButtonPress()
                

    
