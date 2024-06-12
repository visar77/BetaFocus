<div style="background-color: black; color: white; padding: 10px;">

<details>
<summary style="font-size: 24px; font-weight: bold;">Quick-Start Anleitung und Video Tutorial</summary>

![Alttext](thumbnail.jpg)

[Zum Video](https://youtu.be/HeGSPaNe2Dc) <br>

Um direkt loslegen zu können:
1. **Schalter [TIMESTAMP] auf AUS und BetaFocus-Device auf AUS. Verbinde ESP32 per USB mit PC**<br> damit RX vom ESP32 und TX vom Mikrocontroller nicht verbunden sind, während des Uploads (denn sonst funktioniert es nicht) </span>  
2.  **Sketch uploaden mit ArduinoIDE:** siehe [Github](https://github.com/visar77/BetaFocus/tree/main/Arduino%20Sketches) 
    1. Mit unserem Display: display_128x64_bluetooth_arduino_sketch.ino [hier](https://github.com/visar77/BetaFocus/blob/main/Arduino%20Sketches/README.de.md#display_128x64_bluetooth_arduino_sketchino) 
    2. Ohne Display: bluetooth_arduino_sketch.ino [hier](https://github.com/visar77/BetaFocus/blob/main/Arduino%20Sketches/README.de.md#bluetooth_arduino_sketchino)
3. **Verbindung zwischen PC und USB trennen (ACHTUNG: PC SOLLTE NICHT MIT BETAFOCUS-DEVICE VERBUNDEN SEIN WÄHREND BENUTZUNG)**
4. **Schalter auf AN und BetaFocus-Device AN**
5. **Verbinde PC per Bluetooth mit "BetaFocus Device"** → Es werden zwei serielle Ports auf dem Rechner kreiert, welche die Bluetooth-Verbindung darstellen  
6. **Wähle in der Software (GUI) unter "Verbinden" den Eingangs-Port aus**
7. **Setze das "BetaFocus Device" auf und befestige die Klemmen an den Ohren**
8. **Starte die Session**
</details>

<summary style="font-size: 24px; font-weight: bold;">FAQs</summary>
<details>
<summary style="font-size: 16px; font-weight: bold;">Wie funktioniert das mobile Hirnwellenmessgerät?</summary>
Siehe Info-Seite [LINK]
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Ist BetaFocus sicher?</summary>
Das Spielzeug "MindFlex" wurde von Mattel konzipiert und getestet und gilt demnach als sicher. Alle vorgenommenen Änderungen, wie im Video dargestellt, geschehen auf eigenem Risiko. 
**WICHTIG:** Das Gerät darf NIEMALS mit einem Kabel verbunden sein, während man es auf dem Kopf trägt. (Dies beinhaltet bspw. die Verbindung per USB-Kabel zum PC, etc.)
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Wie genau sind die Messungen?</summary>
Siehe Info-Seite [LINK]
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Welche Art von Daten kann ich erwarten?</summary>
Serielle Zahlenwerte für die Signalqualität (0 - 100, wobei 0 sehr schlechte Signalqualität darstellt), Meditation (), Concentration (). Die Daten werden in einer CSV-Datei erfasst und über die Zeit gekennzeichnet.
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Benötige ich spezielle Vorkenntnisse, um das Gerät zu verwenden?</summary>
Nein, mit Hilfe des Video-Tutorials und der Quick-Start-Anleitung sollte man problemlos erste Messungen starten können. Je öfter man das Gerät benutzt, desto intuitiver wird der Umgang.
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Wie lange dauert eine typische Messung?</summary>
Die Dauer der Sessions ist nicht begrenzt, sollte aber für eine korrekte und sinnvolle Auswertung bei mindestens 5 Minuten liegen. Des Weiteren braucht man eine gewisse Zeit, bis man sich in einem konzentrierte Zustand befindet, daher können die ersten Minuten der Messung weniger aussageräftig sein.
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Kann das Gerät mit meinem Smartphone oder Tablet verbunden werden?</summary>
Es ist möglich aber nicht sinnvoll, da noch keine BetaFocus App existiert, mit der man Asuwertungen betreiben kann. Man kann allerdings eine Verbindung zum Gerät herstellen und die seriellen Werte beobachten.
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Welche Betriebssysteme werden unterstützt?</summary>
WINDOWS, LINUX und MAC wurden getestet und werden von unserer Software unterstützt.
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Kann ich die Daten mit anderen Geräten oder Plattformen teilen?</summary>
Da die Daten im CSV-Format vorliegen kann man sie problemlos mit anderen Plattformen, Apps oder Geräten teilen. Allerdings liegen die Daten dann im Rohformat vor und sind nicht optimiert, um in anderer Software als BetaFocus verwendet zu werden.   
Es existiert außerdem noch keine Funktion, um die Messwerte anschaulich zu exportieren oder zu teilen.
</details>
<details>
<summary style="font-size: 16px; font-weight: bold;">Wie wird die Privatsphäre meiner Daten geschützt?</summary>
Alles ist lokal auf dem eigenen Rechner gespeichert, daher sind Nutzende selbst für die Sicherheit ihrer Daten verantwortlich.
</details>
  
</div>