# Overview
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/visar77/BetaFocus/blob/main/Arduino%20Sketches/README.md)
[![de](https://img.shields.io/badge/lang-de-red.svg)](https://github.com/visar77/BetaFocus/blob/main/Arduino%20Sketches/README.de.md)

Dieses Verzeichnis enthält Arduino sketches, welche auf den meisten Mikrocontroller hochgeladen werden können. <br>
We used an ESP32-WROOM MC, which requires the installation of extra drivers to load sketches. Here is the link to the driver-site:
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads

## bluetooth_arduino_sketch.ino
Dieser Sketch sollte mit allen ESP32-Geräten und Arduinos mit Bluetooth-Funktionalitäten kompatibel sein, wobei BLE nicht ausreicht. 
Der Bluetooth-Name des Mikrocontrollers kann geändert werden, indem der String im ersten Argument in der folgenden Zeile geändert wird:
```cpp
SerialBT.begin("BetaFocus Device", false);
```
## display_bluetooth_sketches
Diese Sketches sollten mit allen ESP32-Geräten und Arduinos mit Bluetooth-Funktionalitäten kompatibel sein.

Falls der Bluetooth-Name geändert werden möchte, siehe oben.

**Wichtige Information:** Die `SCREEN_ADDRESS` des Displays könnte sich unterscheiden von `0x3C`. In diesem Fall muss die Adresse im Datenblatt nachgeschaut werden
oder man kann die Standard-Bibliothek `Wire` der Arduino IDE verwenden und den Beispielsketch `WireScan` ausprobieren, welcher automatisch durch Brute-Force die
Adresse des Displays ermittelt.
### display_128x64_bluetooth_arduino_sketch.ino
Funktioniert and wurde an einem I2C Display der Größe 128x64 ausgetestet. 
### display_128x32_bluetooth_arduino_sketch.ino
Sollte mit einem I2C Display der Größe 128x32 einwandfrei funktionieren. 

## usb_arduino_sketch.ino
**WARNUNG: ES DARF UNTER KEINEN UMSTÄNDEN BENUTZT WERDEN UND ES FUNKTIONIERT AUCH NICHT, FALLS DAS EEG-SPIELZEUG DEN MIKROCONTROLLER MIT STROM VERSORGT ODER
DIE STROMVERSORGUNG DES EEG MIT DEM VCC-PIN DES MIKROCONTROLLER VERBUNDEN IST!!!**

Dieser Sketch sollte mit allen ESP32-Geräten und Arduinos kompatibel sein. Funktioniert nur, wenn der Mikrocontroller mit dem Rechner per USB verbunden ist. 
