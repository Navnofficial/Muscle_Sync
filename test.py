import serial.tools.list_ports
from pynput.keyboard import Key, Controller

keyboard = Controller()
serialInst = serial.Serial()

# List available COM ports
ports = serial.tools.list_ports.comports()
portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

# User input for COM port
val = input("Select Port: COM")

# Match selected port
for x in range(len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print("Selected Port:", portVar)

# Setup serial
serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()

# Listen to serial and simulate keypress
while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        data = packet.decode('utf').strip()
        print("Received:", data)

        if data == 'RIGHT':  # RIGHT
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            print("RIGHT pressed")

        elif data == 'LEFT':  # LEFT
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            print("LEFT pressed")

        elif data == 'REST':  # REST
            print("REST state")
