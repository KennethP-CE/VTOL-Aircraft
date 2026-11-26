import serial
import time

# Define port (use '/dev/ttyACM0' or check your port name)
PORT = '/dev/ttyACM0'
BAUD = 115200

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)

    message = "Hello from Raspberry Pi!\n"
    ser.write(message.encode('utf-8'))
    print(f"Sent: {message.strip()}")

    response = ser.readline().decode('utf-8').strip()
    if response:
        print(f"Received from Teensy: {response}")
        
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()