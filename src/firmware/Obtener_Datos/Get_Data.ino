/*
  IMU Capture
  This example uses the on-board IMU to start reading acceleration and gyroscope
  data from on-board IMU and prints it to the Serial Monitor for one second
  when the significant motion is detected.
  While waiting for significant motion, data is recorded in memory, to avoid
  loosing the starting portion of the gesture movement. There will be a delay
  between capturing the data and outputting it to the Serial Monitor.
  You can also use the Serial Plotter to graph the data.
  The circuit:
  - Arduino Nano 33 BLE or Arduino Nano 33 BLE Sense board.
  Created by Don Coleman, Dominic Pajak, Sandeep Mistry
  This example code is in the public domain.
*/

#include <Arduino_LSM9DS1.h>


void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  // print the header
  Serial.println("aX,aY,aZ,gX,gY,gZ");
}

void loop() {
  float aX, aY, aZ, gX, gY, gZ;

  // wait for threshold trigger, but keep N samples before threshold occurs
  while (1) {
    // wait for both acceleration and gyroscope data to be available
    if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
      // read the acceleration and gyroscope data
      IMU.readAcceleration(aX, aY, aZ);
      IMU.readGyroscope(gX, gY, gZ);
      Serial.print(aX, 4);
      Serial.print(',');
      Serial.print(aY, 4);
      Serial.print(',');
      Serial.print(aZ, 4);
      Serial.print(',');
      Serial.print(gX, 4);
      Serial.print(',');
      Serial.print(gY, 4);
      Serial.print(',');
      Serial.print(gZ, 4);
      Serial.println();
    delayMicroseconds(8403); // delay between each line for Serial Plotter, this matches the 119 Hz data rate of IMU
    }
  }

  

  

  Serial.println(); // empty line
}