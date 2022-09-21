import RPi.GPIO as GPIO
import time,os
from twilio.rest import Client
import keys
import motion

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

client=Client(keys.account_sid,keys.token)

while True:
	time.sleep(5)
	status=GPIO.input(12)
	if status==1:
		if motion.motion():
		  message=client.messages      \
				.create(body="There is an intruder in the house !!",from_="+14582041940",to="+4917656843223")
		  print(message.sid)		
	else:
		print("The place is safe")

