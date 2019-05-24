from flask import Flask, render_template, request
from pyduino import *
import time

app = Flask(__name__)
arduino = Arduino(serial_port="/dev/cu.usbmodem14101")
time.sleep(3)

pin1 = 9
pin2 = 10
pin3 = 11
pin4 = 12
global step_number
step_number = 0

arduino.set_pin_mode(pin1, 'O')
arduino.set_pin_mode(pin2, 'O')
arduino.set_pin_mode(pin3, 'O')
arduino.set_pin_mode(pin4, 'O')
print("Setup done!")


def one_step(direction, s):
    if direction:
        if s > 3:
            # del step_number
            # global step_number
            s = 0

        if s == 0:
            arduino.digital_write(pin1, 1)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
        elif s == 1:
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 1)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
        elif s == 2:
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 1)
            arduino.digital_write(pin1, 0)
        elif s == 3:
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 1)
    else:
        if s > 3:
            # del step_number
            # global step_number
            s = 0

        if s == 0:
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 1)
        elif s == 1:
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 1)
            arduino.digital_write(pin1, 0)
        elif s == 2:
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 1)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
        elif s == 3:
            arduino.digital_write(pin1, 1)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)
            arduino.digital_write(pin1, 0)

    s += 1


@app.route("/", methods=["GET", "POST"])
def stepper():
    if request.method == "POST":
        if request.form["button"] == "moveLeft":
            print("Request: motor goes left")
            for i in range(1000):
                one_step(False, step_number)
                time.sleep(2)
        elif request.form["button"] == "moveRight":
            print("Request: motor goes right")
            for j in range(1000):
                one_step(True, step_number)
                time.sleep(2)
        else:
            pass

    return render_template("stepper.html")


if __name__ == "__main__":
    app.run(debug=True)