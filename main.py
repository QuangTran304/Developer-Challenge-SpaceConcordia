from flask import Flask, render_template, request
from pyduino import *
import time

app = Flask(__name__)

arduino = Arduino(serial_port="/dev/cu.usbmodem14101")
time.sleep(3)

led_pin = 3
analog_pin = 0

arduino.set_pin_mode(led_pin, 'O')
print("Setup is done!")

# We're able to make 2 different requests to our page
# GET --> when we type in the URL
# POST --> when some sort of form submission is submit (button pressed)
@app.route("/", methods = ["POST", "GET"])
def main_page():
    author = "Quang"

    # When the button is pressed (made a POST request)
    if request.method == "POST":
        if request.form["submit"] == "Turn light ON":
            print("Light is on!")                  # 'Log' the info to the console
            arduino.digital_write(led_pin, 1)   # Turn the actual LED on

        elif request.form["submit"] == "Turn light OFF":
            print("Light is off!")
            arduino.digital_write(led_pin, 0)
        else:
            pass

    # Read the analog value from photoresistor
    read_val = arduino.analog_read(analog_pin)

    return render_template("hello.html", author=author, value=100*(read_val/1023.))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="5005")
