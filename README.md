# BetaFocus
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/visar77/BetaFocus/blob/main/README.md)
[![de](https://img.shields.io/badge/lang-de-red.svg)](https://github.com/visar77/BetaFocus/blob/main/README.de.md)

## About
BetaFocus is a project that uses the Mindflex EEG toy from Mattel to measure concentration and visualize them in real-time. 

The project is divided into two parts: 
the hardware, which consists of hacking the Mindflex toy and connecting it to a microcontroller, and the software part, which visualizes the attention data.

This README was written in German and English. If you want to see the German version, click [hier](https://github.com/visar77/BetaFocus/blob/main/README.de.md) or click the badge under the title.

## Setup

### 1. Setup BetaFocus Device
1. Buy a Mindflex EEG toy from Mattel. As they are not produced anymore, you need to get one from Ebay or similar platforms.
2. Get a Microcontroller (Arduino Uno, Nano, etc.) with Bluetooth (not BLE!).
3. (Optional) Get a 128x64 or 128x32 OLED Display with I2C interface.
4. Follow our YouTube tutorial to hack the Mindflex toy and connect it to an Arduino: [Extremly cool video](https://youtube.com/HeGSPaNe2Dc)

### 2. Upload sketch to the Microcontroller
1. Read the [Arduino Readme](https://github.com/visar77/BetaFocus/blob/main/Arduino%20Sketches/README.md) and choose the right Arduino sketch.
2. Upload the sketch to the microcontroller via Arduino IDE or PlatformIO (VS Code).
3. Done!

### 3. Install BetaFocus
Only tested with Python 3.8+. Tested on Windows 10, macOS and Ubuntu 22.04.

#### No Installation
```shell
git clone https://github.com/visar77/BetaFocus.git
pip install pyserial pyqt5 pyqtgraph pyqtwebengine pandas 
cd BetaFocus/BetaFocus/src
python3 main.py
```

#### Release Installation
(Under development)

## Usage
### Starting and stopping a session on Windows 10
1. Open system device manager ![](Images/device_manager_before.png)
2. Connect to the BetaFocus device via Bluetooth ![](Images/connect_bluetooth.png)
3. Look at the opened COM port and remember the number ![](Images/device_manager_after.png)
4. Open the BetaFocus software ![](Images/main_connect.png)
5. Go to Verbinden -> COM Port and select the COM port number

   - Because the sketches create two COM ports, you need to check which one is the right one
   - Try to connect to one COM port and start a session via step 6. If a timeout error occurs after 10 seconds, then you have selected the wrong COM port and the other one is the correct one
   ![](Images/select_right_port.png)
6. Put headset on and click on "Los geht's" to start a session
   ![](Images/session_being_taken.png)
7. Stop the session by clicking on the red square

### Starting and stopping a session on other operating systems
1. Connect to the BetaFocus device via Bluetooth
2. Select the correct port by trying out the available ports that are shown in the software (step 5 in the Windows 10 guide)

### Evaluating the session data
After a session has been stopped, you will see the time in seconds that you have concentrated (that means that the concentration value was over 40), the maximum concentration value and the concentration values over time with a regression line indicating the trend of the concentration values.
Lastly a bottom graph shows the average concentration values of all sessions that have been recorded.
   ![](Images/evaluation.png)

### Checking old session data
1. Click on the "Statistik" button in the main window
2. You will see a list of all sessions that have been recorded and a graph of the average concentration time of all sessions ![](Images/archive.png)
3. To see the data of a specific session, double-click on the session in the list ![](Images/archive_select.png) ![](Images/evaluation_archive.png)
4. To change the name of a session, write a valid name in the text field and click on "Fertig"

### Help
For more information on how to use the the software, click on the question mark button in the main window on the top right. There you will find a detailed explanation of the software as a PDF.

## Info
The science behind the Mindflex toy is based on the EEG technology. We explain the technology in our Info PDF, which can be accessed through the info button in the main window at the top left.
## Licenses of Components / Used Libraries
### Adafruit GFX and SSD1306 library

Specifically thanks to the wonderful Limor Fried (Ladyada) for providing the open source software to control i2c and spi mini-displays.
```
Software License Agreement (BSD License)

Copyright (c) 2012, Adafruit Industries
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holders nor the
names of its contributors may be used to endorse or promote products
derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
## Acknowledgements
The main inspiration for this project was the Frontier Nerds' blog about hacking EEG toys: https://frontiernerds.com/brain-hack. 
It's a wonderful read, easy to follow and gives a lot of insight.
It's written by Eric Mika, a NYU alumni and current Creative Director of Local Projects (https://www.linkedin.com/in/emika/). <br>
His Arduino Brain Library https://github.com/kitschpatrol/Brain also reads NeuroSky-EEG-Headsets and can be combined with BrainGrapher https://github.com/kitschpatrol/BrainGrapher to visualize the read values. <br>
Thanks to Eric, we came up with this idea and expanded upon his hack.
