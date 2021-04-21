from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

dataImageFilename = "dataImage.png"
fnt = ImageFont.truetype('arial.ttf', 15)



import random
import time

import board
import busio


import Adafruit_LSM303

import matplotlib.pyplot as plt
plt.ion()

i2c = busio.I2C(board.SCL, board.SDA)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


#Altimeter set up
import adafruit_mpl3115a2
altimeter = adafruit_mpl3115a2.MPL3115A2(i2c)
# maybe set up the pascal thing from the example? if it is inaccurate


#Accelerometer set up
RST = 24
accelerometer = Adafruit_LSM303.LSM303() # accelerometer setup


@app.route("/", methods=["GET","POST"])
def index():
	print(request.method)
	if request.method == "POST":
		if request.form.get('button1') == 'button1':
			#pass
                        
			startPhrase = str("Lukas")
			startInput = input("Enter " + str(startPhrase) + "  to confirm Launch: ")

			if startInput != startPhrase:
				print("Invalid launch phrase, please type: " + str(startPhrase))                        

			if startInput == startPhrase:
				# runCountdownTimer()
				for i in range (1,5):
					num = 6 - i
					print("Launching in " + str(num))
					time.sleep(1)
				print("Launching in 1")
				time.sleep(1)
				print("Countdown Done")

				# Launch()
				print("Launch Initiated")
				#add actual launch code here
				print("Launch Done")

				# windUp()
				print("Wind Up Started")
				time.sleep(1)
				print("Wind Up Done")

				# inFreefall()
				print("In Freefall")
				#take readings
				print("Freefall done")

				# landed()
				print("Landed Running")
				colors = ['ro', 'mo', 'yo']
				ax=plt.axes()
				ax.set_facecolor("#000033")
				plt.plot([1,2,3,4],[1,4,9,19], random.choice(colors))
				plt.axis([0,6,0,20])
				plt.savefig("static/images/refreshTestImage.png")
				plt.show()
				print("Landed Done")

		else:
			# pass # unknown
			return render_template("index.html")

	elif request.method == 'GET':
		# return render_template("index.html")
		print("No Post Back Call")
	return render_template("index.html")


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)  #port was 80


