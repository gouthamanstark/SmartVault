import RPi.GPIO as GPIO
import time,os
from twilio.rest import Client
import keys
import motion

#Configuring the GPIO pin (as input) in the raspberry pi
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

#initializing the twilio client
client=Client(keys.account_sid,keys.token)

while True:
	time.sleep(5)
	#Checks the output from the GPIO pin no. 12
	status=GPIO.input(12)
	
	# When motion is detected by the PIR sensor motion method is called for further confirmation through CV detection
	if status==1:
		if motion.motion():
		# SMS sent to the user when a human face is detected by CV program
		  message=client.messages      \
				.create(body="There is an intruder in the house !!",from_="+14582041940",to="+4917656843223")
		  print(message.sid)		
	else:
		print("The place is safe")

