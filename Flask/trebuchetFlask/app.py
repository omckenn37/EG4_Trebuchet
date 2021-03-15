from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	print(request.method)
	if request.method == "POST":
	        if request.form.get('button1') == 'button1':
                	# pass
               		print("button1")

		elif request.form.get('button2') == 'button2':
                	# pass # do something else
                	print("button2")


            	elif request.form.get('button3') == 'button3':
                	# pass # do something else
                	print("button3")


            	elif  request.form.get('button4') == 'button4':
                	# pass # do something else
                	print("button4")


            	else:
                	# pass # unknown
                	return render_template("index.html")

        elif request.method == 'GET':
            # return render_template("index.html")
            print("No Post Back Call")
        return render_template("index.html")


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)

