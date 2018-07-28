"""
# autoGarden

#The Program
This program is used as a timer mechanism for a and hydroponic/aeroponic system controlling lighting and irrigation.
The raspberry pi is used to turn on/off lighting and a water pump. 
Lighting is on for 13hrs and off for 11hrs.
The water pump is set on for 1 minute every five minutes.

There are three different buttons.
 - Button 1: Turns on/off the system.
 - Button 2: Changes time that motor is on. 3 different times: 30 secs, 60 secs, or 90 secs on in a 5 minute cycle.
 - Button 3: Changes time that LED is on. 6 different times: 11hrs, 12hrs, 13hrs, 14hrs, 15hrs on in a 24hr cycle.

Future Improvements:
- To add a temperature and humidity sensor for better monitoring √
- To create software over a network for remote access to the system changing motor timing and light timing
  as well as send information on humdity and temperature.

For more information please check the wiki.
"""



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
#light times hrs15 = 54000.00, hrs12  = 43200.00, hrs13 = 46800.00, , hr = 3600
#light time default is 13 hrs
hrs = 46800.00
#motor times default is 1 min on and 4 minutes off
tMotorOn = 60.00
tMotorOff = 240.00  #increments of 30 seconds
motorTime = 0
currentTime = 0
LEDTime = 0

hrs24 = 86400.00

#Function handles timing for lighting in a 24hr cycle. 
def LEDTimer():
    global LEDTime
    if (time.time() - LEDTime) < hrs:
        lights.on()
    elif (time.time() - LEDTime) < hrs24:
        lights.off()
    else:
        LEDTime = time.time()
#Function handles timing for water pump in a 5min cycle. 
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
        
#Handles button press event changing duration of ON time for water pump in a 5min cycle.    
def motorTimeButtonPress():
    global tMotorOn
    global tMotorOff
    if tMotorOn == 90.00: #maximum time on is 1min and 30secs
        tMotorOn = 30.00
        tMotorOff = 270.00
    else:
        tMotorOn = tMotorOn + 30.00
        tMotorOff = tMotorOff - 30.00
        
#Handles button press event changing duration of ON time for lighting in a 24hr cycle.    
def lightTimeButtonPress():
    global hrs
    if hrs == 54000.00:#15hrs is maximum
        hrs = 39600.00 #resets to 11hrs
    else:
        hrs = hrs + 3600.00
    print("Light is on for: " + hrs/3600.00 + ".\n")
    
def tempHumSensor():
    return 0

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
        if motorTime_Button.is_pressed:
            motorTimeButtonPress()
        if lightTime_Button.is_pressed:
            lightTimeButtonPress()
                

    
