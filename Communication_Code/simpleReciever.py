import serial
import socket
import json
import time

PORT = '/dev/ttyACM0'
BAUD = 115200

def connectSocket():
    global receptor
    receptor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receptor.bind(("0.0.0.0", 5000))
    receptor.settimeout(1000000000)
    print("Socket established")

def readInputs():
    data, address = receptor.recvfrom(2048)
    json_message = data.decode("utf-8")
    message = int(json.loads(json_message))
    return message

def finishProgram():
    receptor.close()

def send_Serial(message1):
    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(2)

        message = str(message1) + "\n"
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

connectSocket()
try:
    while True:
        try:
            inputs = int(readInputs())
        except socket.timeout:
            print("Stopped receiving data")
            inputs = 0
        send_Serial(inputs)
        print("Sent: ", inputs)
except KeyboardInterrupt:
    finishProgram()
