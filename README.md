# Serial Animator

## What is this?
A python script to visualize the serial data on a real time moving plot. It utilizes matplotlib library to generate the plot. The script does the following:

* Connects to and reads from a serial port.
* Parses each line coming from the serial port into the labels and values.
  * In each line received on the serial port there should be a pair(s) of label and value seperated by equal sign (=), coma (,) or colon (:)
  * Blank spaces before the label and after the value are ignored
  * Blank spaces before and after the seperating characters are ignored
  * Some valid line examples received on the serial port:
  ```
  Position=12
  Position= 12 Velocity= 21 Acceleration= -3
  Position : 12.0    Velocity = 21.2 Acceleration,-3
  ```
* Draws values with different labels on to the plot.
* Provides checkboxes to toggle data labels.
* Automatically scales the y-axis to fit the visible lines.

## Screenshots
<p align="center">
  <img src="https://github.com/bataseven/serial_animator/blob/master/Screenshots/Serial_Plotter.png" width=400 title="Plot 1">
  <img src="https://github.com/bataseven/serial_animator/blob/master/Screenshots/Serial_Plotter2.png" width="400" title="Plot 2">
</p>

<p align="center">
  <img src="https://github.com/bataseven/serial_animator/blob/master/Screenshots/Console.png" width=400 title="Port Selection">
</p>


