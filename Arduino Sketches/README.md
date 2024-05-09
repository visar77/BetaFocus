# Overview
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/visar77/BetaFocus/blob/main/Arduino+Sketches/README.md)
[![de](https://img.shields.io/badge/lang-de-red.svg)](https://github.com/visar77/BetaFocus/blob/main/Arduino+Sketches/README.de.md)

This directory contains a number of Arduino sketches, which can be loaded onto most microcontrollers. <br>
We used an ESP32-WROOM MC, which requires the installation of extra drivers to load sketches. <br> 
Here is the link to the driver-site:
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads

## bluetooth_arduino_sketch.ino
This sketch should work with all ESP32 or Arduino Boards with Bluetooth (not BLE). You can change the name of your device
by changing the string in the first argument:
```cpp
SerialBT.begin("BetaFocus Device", false);
```

## display_bluetooth_arduino_sketch.ino
This sketch should work with all ESP32 or Arduino Boards with Bluetooth (not BLE) and has only been tested on a mini I2C display (128x32). 

If you wish to change your devices bluetooth name, look at the instruction above. If you wish to use a 128x64 display, then you need to change following lines in the sketch 
(**they are not grouped like this, you need to find them in the upper part of the sketch**):
```cpp
#define SCREEN_HEIGHT 32 // OLED display height, in pixels
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
#define GRAPH_HEIGHT 23
```
to
```cpp
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define SCREEN_ADDRESS 0x3D ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
#define GRAPH_HEIGHT 46
```
**Important Information:** `SCREEN_ADDRESS` could be different from `0x3C` or `0x3D`. In that case, you can either find the screen address by yourself or 
use the `Wire`, a standard library in the Arduino IDE and use the example sketch `WireScanner`, which will determine the screen address automatically.
## usb_arduino_sketch.ino
**WARNING: DOESN'T WORK AND DON'T USE IF POWERSUPPLY OF MICROCONTROLLER IS CONNECTED TO EEG (VCC PIN OF MICROCONTROLLER CONNECTED / SOLDERED TO POWERSUPPLY OF EEG TOY) !!!**

This sketch should work with all ESP32 or Arduino Boards. It only works if the microcontroller is constantly connected to your PC through USB. 
