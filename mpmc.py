import serial
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Change this to your Arduino's COM port
ser = serial.Serial('COM7', 115200, timeout=1)

# Flags to avoid holding key forever
left_pressed = False
right_pressed = False

while True:
    try:
        line = ser.readline().decode('utf-8').strip()

        if line == '3':  # LEFT
            if not left_pressed:
                keyboard.press(Key.left)
                left_pressed = True
            if right_pressed:
                keyboard.release(Key.right)
                right_pressed = False

        elif line == '2':  # RIGHT
            if not right_pressed:
                keyboard.press(Key.right)
                right_pressed = True
            if left_pressed:
                keyboard.release(Key.left)
                left_pressed = False

        elif line == '1':  # REST
            if left_pressed:
                keyboard.release(Key.left)
                left_pressed = False
            if right_pressed:
                keyboard.release(Key.right)
                right_pressed = False

    except KeyboardInterrupt:
        break
    except Exception as e:
        print("Error:", e)
