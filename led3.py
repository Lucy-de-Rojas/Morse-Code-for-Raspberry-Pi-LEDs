#I'm so happy to be able to do this.
#TRAIN TRACK STORY: long time ago, 2 boys were walking home from school along the train track.
#Actually on the train track. Health and safety those days, was based more on common sense and a bit of luck too.
#Back to our boys. Walking home along the track, they came across a fallen tree on the track. Knowing
#there would be a train passing by very soon, the boys started to panic. Some of their school friends were on the train.
#And other people too. In panic, they started hitting the track rails with stones hoping to alert the train driver.
#First, it was just about hitting the rails to create as much noise as possible, but then one of the boys remembered stories
#his grandad told him about travelling on sea and using Morse code to communicate using light. The SOS signal came to his
#mind and he started to use Morse Code to send the message. Strangely enough the driver of the approaching train overheard
#some strange noises, thinking there was something wrong with the train he started slowing down to a halt. Climbing out of
#machine to see what's wrong the ringing noises carried on coming from the direction the train was heading to. To cut
#the story short, the boys saved the day. They were very happy, their parrents were very proud and the school did a lesson
#or two on Morse code and other alternative ways to convey a message.  THE MORAL OF THE STORY: never walk on a train track. Alone.
#Always bring a friend. Because two people know more than one and are more likely to support each other in tricky situations.

#welcome to this project for Raspberry Pi.
#code bellow will le you connect LEDs to your Raspberry Pi.
#I used 5 different colours in 5 GPIOs: feel free to change these.
#we assume at this stage, the INPUT will be letters and space only. 

import RPi.GPIO as GPIO
import time

#here are the 5 LEDs allocations for the Raspberry board:
blue,red,yellow,green,white= 22,23,4,17,27


#in here are all the necessary setups:
GPIO.setmode(GPIO.BCM),GPIO.setwarnings(False)
GPIO.setup(blue, GPIO.OUT), GPIO.setup(red, GPIO.OUT),GPIO.setup(yellow, GPIO.OUT), GPIO.setup(green, GPIO.OUT), GPIO.setup(white, GPIO.OUT)


#here is the function switching the RED led on:
def led(lenght):
    GPIO.output(red, GPIO.HIGH) #<to change colour change the colour name here 1/2
    time.sleep(lenght)
    GPIO.output(red, GPIO.LOW)   #<to change colour change the colour name here 2/2
    time.sleep(0.30)   #<pause after letter 

    
#in here is the dictionary where the length of the beep/light on is in accordance with Morse code:
morse = {'a': (0.15, 0.5), 'b' : (0.5, 0.15, 0.15, 0.15), 'c': (0.5,0.15,0.5,0.15),
         'd':(0.5,0.15,0.15), 'e': (0.15), 'f': (0.15, 0.15,0.5,0.15), 'g':(0.5,0.5,0.15),
         'h':(0.15,0.15,0.15,0.15), 'i':(0.15,0.15), 'j': (0.15, 0.5,0.5,0.5), 'k': (0.5,0.15,0.5),
         'l': (0.15,0.5,0.15,0.15), 'm': (0.5,0.5), 'n': (0.5,0.15), 'o':(0.5,0.5,0.5),
         'p':(0.15,0.5,0.5,0.15), 'r':(0.15,0.5,0.15), 's': (0.15,0.15,0.15), 't': (0.15),
         'u': (0.15,0.15,0.5), 'v':(0.15,0.15,0.15,0.5), 'w': (0.15,0.5,0.5), 'x': (0.5,0.15,0.15,0.5),
         'y': (0.5,0.15,0.5,0.5), 'z': (0.5,0.5,0.15,0.15),}

#here is a sos signal to play with:
a = 'SOS sos'


#and here is the function doing all the magic:
def convertToMorse(stringie):
    stringie = stringie.lower()#<converts upper case to lower:
    
    for i in stringie:
        
        if i == ' ':  #<here we work with space in a string
            time.sleep(1.5)
            
           
        else: 
            for x in morse[i]:   #<and here we do the converting: 
                led(x)
            

                
#and here we test the code:                
convertToMorse(a)


#hope you like the project. Have a lovely day.
