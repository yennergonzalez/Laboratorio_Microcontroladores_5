# Laboratorio de Microcontroladores
# Laboratorio 5 - Human Activity Recognition
# Yenner Gonzalez Araya - B83375
# Gabriel Barahona Otoya - B70896

# Arduino -> CSV Script


#  - - - - - - - - IMPORTS - - - - - - - - 
import serial
import csv

# - - - - - - - - SETUP - - - - - - - - 
arduino_port = "/dev/ttyACM1"           # puerto serial arduino
baud = 9600                             # tasa de baudios de arduino es 9600
fileName = "circles.csv"                   # nombre del archivo generado

ser = serial.Serial(arduino_port, baud) # inicializacion puerto serial
file = open(fileName, "w")              # abrir archivo a escribir

samples = 1000                          # cantidad de muestras a tomar
line = 0                                # contador de lineas

writer = csv.writer(file)

header = ["accx", "accy", "accz", "gyrx", "gyry", "gyrz"]       # encabezado del archivo csv

writer.writerow(header)                 # escribir encabezado

# ciclo para tomar todas las muestras requeridas 
while line <= samples:
    
    getData=str(ser.readline())              # leer una linea completa
    dataString = getData[2:-5]               # no tomar en cuenta \n ni \t
    dataList = dataString.split(',')         # convertir de cadena de texto a una lista
    data = []
    for i in range (len(dataList)):
        data.append(float(dataList[i].replace("'","")))
    print(data)                         # mostrar datos a escribir en consola

    # evitar escribir una linea incompleta de datos
    if len(data)==6:
        line = line+1                       # incrementar contador de lineas
        writer.writerow(data)                 # escribir datos al archivo csv
    else:
        pass

print("Data collection complete!")
file.close()