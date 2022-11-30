import serial
import csv

arduino_port = "/dev/ttyACM2" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="results.txt" #name of the CSV file generated

ser = serial.Serial(arduino_port, baud)
file = open(fileName, "w")

samples = 1000 #how many samples to collect
line = 0 #start at 0 because our header is 0 (not real data)

while line <= samples:
    getData=ser.readline()
    data = getData.decode('utf-8')
    print(data)
    line = line+1

    file = open(fileName, "a")
    file.write(data)

print("Results obtained!")
file.close()