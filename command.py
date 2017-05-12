#!/usr/bin/env python3
########## DO NOT CHANGE ##########
import rover
import time
  
#create instance
myRover=rover.MARSROVER() 

###################################

#Enter your code below
#Use "#" to comment out the code

#myRover.capture_image()
myRover.go_forward(5)
#myRover.go_backward(2)
#myRover.measure_humidity() 
#myRover.measure_temperature() 

#myRover.turn_left(5)
#myRover.turn_right(5)
#myRover.measure_temperature() 
#myRover.go_backward(2)

#take photo
#myRover.capture_image()

#turn using encoder
#myRover.turn_left_using_speed_sensor(20)
#myRover.turn_right_using_speed_sensor(20)

#Use this function to control iso and shutter speed (in microsecond, max 6s)
#myRover.capture_manual_image(100,1000000)

########## DO NOT CHANGE BELOW ##########
#clear gpio ports
myRover.clear()



