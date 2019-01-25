# 							ROBOT CAR PROJECT

# WRITEN BY: Lucas Everts
# WRITEN FOR: WMU Raspberry Pi Clubs Fall 2015 Sumo Robot Compitition
# LAST EDITED: August 21, 2015

# DESCRIPTION:
# The following Python code was writen for a sumo compition robot.  The robot is powered by a Raspberry Pi B+, two L298N H-Bridges,
# and four 18650 3.7V batteries.  The motors are hobby level high torque DC motors.  


print("Beginning of program, wait for initialization....")

# imports
import time
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

#initializing pygame.  NOTE: the display.set_mode((400,400)) is setting the size of the display in pixels. 
pygame.init()
screen = pygame.display.set_mode((400,400))

print("Imports Completed.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO Pin Setup
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

# Setting all Pins to LOW and Pin Assignments

GPIO.output(5,0)    # left motor control 1
GPIO.output(6,0)    # left motor control 2
GPIO.output(7,0)	# right motor control 1
GPIO.output(8,0)	# right motor control 2

GPIO.output(23,0)	# lift motor control 1
GPIO.output(24,0)	# lift motor control 2

GPIO.output(12,0)	# top correction control 1
GPIO.output(16,0)	# top correction control 2
GPIO.output(20,0)	# side correction control 1
GPIO.output(21,0)	# side correction control 2

GPIO.output(26,1)	# Program ON/OFF LED's

end = 0

print("Begin to enter directions: ")

# Main Loop
while(end == 0):
	for event in pygame.event.get():
		if event.type == KEYDOWN:
		
			if event.key == K_w:		# K_w signifies that the key was from the keyboard
				print("'w' was pressed, going straight.")
				GPIO.output(5,1)	# output configuration for going straight
               	GPIO.output(6,0)	# outputs 5,6 control left motor
				GPIO.output(7,1)	# outputs 7,8 control right motor
				GPIO.output(8,0)
				pressedKey = 'w'
				pygame.event.pump()	# pygame.pump() removes the event flag/only runs keydown once
				
            if event.key == K_a:
				print("'a' was pressed, turning left.")
				GPIO.output(5,0)  
				GPIO.output(6,1)
				GPIO.output(7,1)
				GPIO.output(8,0)
				pressedKey = 'a'
				pygame.event.pump()
				
			if event.key == K_d:
				print("'d' was pressed, turning right.")
				GPIO.output(5,1)
				GPIO.output(6,0)
				GPIO.output(7,0)
				GPIO.output(8,1)
				pressedKey = 'd'
				pygame.event.pump()
				
			if event.key == K_s:
				print("'s' was pressed, going backwards.")
				GPIO.output(5,0)
				GPIO.output(6,1)
				GPIO.output(7,0)
				GPIO.output(8,1)
				pressedKey = 's'
				pygame.event.pump()
					
			if event.key == K_y:
				print("'y' was pressed, correction motors going out.")
				GPIO.output(5,0)
				GPIO.output(6,0)
				GPIO.output(7,0)
				GPIO.output(8,0)
				pressedKey = 'y'
				pygame.event.pump()
			if event.key == K_h:
				print("'h' was pressed, correction motors coming in.")
				GPIO.output(5,0)
				GPIO.output(6,0)
				GPIO.output(7,0)
				GPIO.output(8,0)
				pressedKey = 'h'
				pygame.event.pump()
			if event.key == K_k:
				end = 1
				print("'k' was pressed, the program will end.")
				
			if event.key == K_l:
				end = 1
				print("'l' was pressed, the program will end.")
				
			if event.key == K_i:
				end = 1
				print("'i' was pressed, the program will end.")
				
			if event.type == KEYUP:
				print(pressedKey + " key was released")
				GPIO.output(7,0)
				GPIO.output(8,0)
				GPIO.output(23,0)
				GPIO.output(24,0)
				GPIO.output(12,0)
				GPIO.output(16,0)
				GPIO.output(20,0)
				GPIO.output(21,0)
				GPIO.output(5,0)
				GPIO.output(6,0)
				pygame.event.pump()		

GPIO.output(7,0)
GPIO.output(8,0)
GPIO.output(23,0)
GPIO.output(24,0)
GPIO.output(12,0)
GPIO.output(16,0)
GPIO.output(20,0)
GPIO.output(21,0)
GPIO.output(5,0)
GPIO.output(6,0)
GPIO.output(26,0)


GPIO.cleanup()
print("THIS IS THE END OF THE PROGRAM!")


