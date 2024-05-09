# Overview
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/visar77/BetaFocus/blob/main/Arduino+Sketches/README.md)
[![de](https://img.shields.io/badge/lang-de-red.svg)](https://github.com/visar77/BetaFocus/blob/main/Arduino+Sketches/README.de.md)

Dieses Verzeichnis enthält Arduino sketches, welche auf den meisten Mikrocontroller hochgeladen werden können. <br>
We used an ESP32-WROOM MC, which requires the installation of extra drivers to load sketches. Here is the link to the driver-site:
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads

## bluetooth_arduino_sketch.ino
Dieser Sketch sollte mit allen ESP32-Geräten und Arduinos mit Bluetooth-Funktionalitäten kompatibel sein, wobei BLE nicht ausreicht. 
Der Bluetooth-Name des Mikrocontrollers kann geändert werden, indem der String im ersten Argument in der folgenden Zeile geändert wird:
```cpp
SerialBT.begin("BetaFocus Device", false);
```

## display_bluetooth_arduino_sketch.ino
Dieser Sketch sollte mit allen ESP32-Geräten und Arduinos mit Bluetooth-Funktionalitäten kompatibel sein, wobei BLE nicht ausreicht in Verbindung mit einem I2C Display der Größe 128x32. 

Falls der Bluetooth-Name geändert werden möchte, siehe oben. Falls man einen 128x64 Display verwenden möchte, dann müssen folgende Zeilen
im Sketch verändern werden
(**so wird das im Code nicht aussehen, man muss die einzelnen Zeilen im oberen Bereich des Sketches suchen und verändern**):
```cpp
#define SCREEN_HEIGHT 32 // OLED display height, in pixels
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
#define GRAPH_HEIGHT 23
```
zu
```cpp
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define SCREEN_ADDRESS 0x3D ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
#define GRAPH_HEIGHT 46
```
**Wichtige Information:** Die `SCREEN_ADDRESS` des Displays könnte weder `0x3C` noch `0x3D` sein. In diesem Fall muss die Adresse selbst herausgefunden werden
oder man kann die Standard-Bibliothek `Wire` der Arduino IDE verwenden und den Beispielsketch `WireScanner` ausprobieren, welcher automatisch durch Brute-Force die
Adresse des Displays ermittelt.
## usb_arduino_sketch.ino
**WARNUNG: ES DARF UNTER KEINEN UMSTÄNDEN BENUTZT WERDEN UND ES FUNKTIONIERT AUCH NICHT, FALLS DAS EEG-SPIELZEUG DEN MIKROCONTROLLER MIT STROM VERSORGT ODER
DIE STROMVERSORGUNG DES EEG MIT DEM VCC-PIN DES MIKROCONTROLLER VERBUNDEN IST!!!**

Dieser Sketch sollte mit allen ESP32-Geräten und Arduinos kompatibel sein. Funktioniert nur, wenn Mikrocontroller mit Rechner per USB verbunden ist. 
