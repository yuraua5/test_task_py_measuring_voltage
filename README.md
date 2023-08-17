# Arduino and Python Communication Example

This repository contains an example of communication between an Arduino and a Python script using a COM port. The Arduino measures voltage using an analog input, and the Python script reads the measured voltage via the COM port.

## Getting Started

### Prerequisites

- Arduino IDE installed for uploading the code to the Arduino board.
- Python 3.x installed on your computer.
- PySerial library installed for Python (`pip install pyserial`).

### Hardware Setup

1. Connect your Arduino board to the computer using a USB cable.
2. Upload the Arduino code (`arduino_sketch.ino`) to your Arduino using the Arduino IDE.

### Running the Python Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing the Python script (`python_script.py`).
3. Run the Python script:


The Python script will communicate with the Arduino over the COM port, read the measured voltage, and print it to the console.

## Code Explanation

### Arduino Code (`arduino_sketch.ino`)

The Arduino code reads analog data from pin A0 and listens for commands from the Python script. It sets the integration time (NPLC) based on the received command and sends back the measured analog value.

### Python Script (`python_script.py`)

The Python script establishes a connection to the Arduino via the specified COM port. It sends commands to set the integration time and read the measured voltage. The received data is processed and converted to voltage.
