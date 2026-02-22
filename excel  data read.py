import serial
import csv
import time

# Configure the serial connection
port = 'COM12'  # Change this to your port (e.g., '/dev/ttyUSB0' for Linux/Raspberry Pi)
baudrate = 9600  # Must match Arduino serial rate
timeout = 1

# Output CSV file name
csv_filename = r'D:\Forge\emg_data_with_envelope.csv'
csv_file_name = csv_filename.replace('.csv', f'_{time.strftime("%Y%m%d_%H%M%S")}.csv')

# Open serial connection
try:
    ser = serial.Serial(port, baudrate, timeout=timeout)
    print(f"Connected to {port} at {baudrate} baud rate")
except serial.SerialException:
    print(f"Failed to connect to {port}")
    exit()

# Create and open CSV file
with open(csv_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'EMG_Value'])  # Header row

    print("Reading EMG data... Press Ctrl+C to stop.")
    try:
        while True:
            line = ser.readline().decode().strip()

            if line:
                timestamp = time.time()
                print(f"{timestamp}, {line}")
                writer.writerow([timestamp, line])
    except KeyboardInterrupt:
        print("\nData collection stopped.")
    finally:
        ser.close()
        print(f"Data saved to {csv_file_name}")
