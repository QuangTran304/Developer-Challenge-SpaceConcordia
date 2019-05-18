from pyduino import *
import time

if __name__ == "__main__":

    print("Establishing connection to Arduino...")
    arduino = Arduino(serial_port="/dev/cu.usbmodem14101")
    time.sleep(3)
    print("Established!")

    # Setup the LED pin
    LED = 3
    arduino.set_pin_mode(LED, 'O')
    time.sleep(1)

    arduino.digital_write(LED, 1)

    for i in range(0, 1000):
        try:
            # Read the analog value from pin A0
            analog_val = arduino.analog_read(0)

            # Print value in range 0-100
            print("ANALOG READ =", int((analog_val/1023.)*100))
            time.sleep(1)

        except KeyboardInterrupt:
            break

    # Make sure we turn off the LED and close the serial connection
    print("CLOSING")
    arduino.digital_write(LED, 0)
    arduino.close()
