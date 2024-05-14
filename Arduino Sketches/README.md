# Overview
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/visar77/BetaFocus/blob/main/Arduino%20Sketches/README.md)
[![de](https://img.shields.io/badge/lang-de-red.svg)](https://github.com/visar77/BetaFocus/blob/main/Arduino%20Sketches/README.de.md)

This directory contains a number of Arduino sketches, which can be loaded onto most microcontrollers. <br>
We used an ESP32-WROOM MC, which requires the installation of extra drivers to load sketches. <br> 
Here is the link to the driver-site:
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads

## bluetooth_arduino_sketch.ino
This sketch should work with all ESP32 or Arduino Boards with Bluetooth (not BLE). You can change the name of your device
by changing the string in the first argument of code (in `setup()` method) :
```cpp
SerialBT.begin("BetaFocus Device", false);
```
## display_bluetooth_sketches
These sketches should work with all ESP32 or Arduino Boards with Bluetooth (not BLE) capabilities. 

If you wish to change the Blueetooth device name, look at the instruction above.


**Important Information:** `SCREEN_ADDRESS` could be different from `0x3C`. In that case, you can either find the screen address 
by looking at the datasheet or use `Wire`, a standard library in the Arduino IDE and use the example sketch `WireScan`, which will determine the screen address automatically.
### display_128x64_bluetooth_arduino_sketch.ino
Works and has been tested on an I2C display with size 128x64. 
### display_128x32_bluetooth_arduino_sketch.ino
Should work without issues on an I2C display with size 128x32. 

## usb_arduino_sketch.ino
**WARNING: DOESN'T WORK AND DON'T USE IF POWERSUPPLY OF MICROCONTROLLER IS CONNECTED TO EEG (VCC PIN OF MICROCONTROLLER CONNECTED / SOLDERED TO POWERSUPPLY OF EEG TOY) !!!**

This sketch should work with all ESP32 or Arduino Boards. It only works if the microcontroller is constantly connected to your PC through USB. 
