
# Inter_IIT_23_task1_team27

Contains codes for sending MSP packets to pluto drone via wireless communication. Also has codes to fly pluto using the packets with sequential functions and keyboard commands.




## Installation

The following libraries are required to be installed for the codes to work (make sure python version is 3.6 or higher):-

Python Library Manager
```bash
  sudo apt-get update
  sudo apt-get -y install python3-pip
```
Numpy
```bash
  pip install numpy
```
Keyboard
```bash
  pip install keyboard
```
## Fly the drone using keyboard (Task 1)

Run **`task1_keyboard.py`**. This establishes a connection with the drone that communicates at a rate of 50hertz.

Using the keybaord, you can now fly the drone. The key mappings are as follows:

| Key | Command |
| ----| ------- |
| v |Arm|
| b |Disarm|
| w  |Increase height of the drone|
| s  |Decrease height|
| l  |Roll right|
| j  |Roll left|
| i  |Pitch front|
| k |Pitch Back|
| a  |Yaw anticlockwise|
| d  |Yaw clockwise|
| t |Takeoff|
| y  |Land|

Run **`task1test.py`** to demonstrate the roll, pitch, yaw, takeoff and land capabilities of the drone. The sequence in which the demonstration happens is as follows:
* Arm
* Takeoff
* Pitch front
* Counter Pitch
* Roll right
* Counter Roll
* Pitch Back
* Counter Pitch
* Roll left
* Counter Roll
* Yaw clockwise
* Yaw anticlockwise
* Land
* Disarm
* Disconnect




## Documentation

The documentation of all codes can be found here.
[Task 1 Documentation](https://github.com/rajsurya1012/Inter_IIT_23_task1_team27/blob/master/Task1_code_documentation.pdf)

