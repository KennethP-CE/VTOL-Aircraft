import time
import json
import socket

def connectSocket():
    global pi
    print("Connecting to pi")
    pi = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pi.connect(("192.168.50.2", 5000))
    print("Connected to pi")

def collectInputs():
    digital_Input = int(input("what degrees to set servo to? (enter integer 0-180): "))
    return digital_Input

def sendInputs(m):
    message = m
    json_message = json.dumps(message)
    data = json_message.encode("utf-8")
    pi.send(data)
    print("Sent: ", message)

def finishProgram():
    pi.close()

connectSocket()
try:
    while True:
        inputs = collectInputs()
        sendInputs(inputs)
        time.sleep(0.05)
except KeyboardInterrupt:
    finishProgram()