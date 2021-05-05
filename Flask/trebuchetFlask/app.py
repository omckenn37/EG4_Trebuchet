from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO


fnt = ImageFont.truetype('arial.ttf', 15)

import numpy as np

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
#accelerometer = Adafruit_LSM303.LSM303() # accelerometer setup


@app.route("/", methods=["GET","POST"])
def index():
	print(request.method)
	if request.method == "POST":
		if request.form.get('button1') == 'button1':
			#pass

			print("Put ball on stand")

                        
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

				#find exit velocity and angle

				print("Wind Up Done")


				# inFreefall()
				print("In Freefall")





				print("Freefall done")

				# landed()

				print("Landed Running")



				#x = np.linspace(0,displacement,100)
				x = np.linspace(0,10,25)
				y = (A * x**2) + (B*x) + C
				yString = str(str(A)+ "x^2 + " + str(B) + "x + " + str(C))


				ax=plt.axes()
				ax.set_facecolor("#000033")
				plt.plot(x,y, c = "GhostWhite")
				plt.axis([0,10,0,10])
				#plt.axis(0,displacement, 0, max height)
				plt.savefig("static/images/refreshTestImage.png")
				plt.show()

				image = Image.new(mode="RGB", size = (300,225), color = (0,0,51))
				draw = ImageDraw.Draw(image)
				text = str("Equation = " + yString + "\n Distance = \n Height = ")
				draw.text((10,10), text, font=fnt, fill=(255,255,255))
				image.save("static/images/dataImage.png")

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


