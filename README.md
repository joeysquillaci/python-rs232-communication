# python-rs232-communication
This project was used to practice more serial communication with python, this time utilizing RS232.

Hardware set up:
Using loopback testing, we can use PC--> USB to RS232 --> female RS232 to female RS232 --> RS232 to USB--> PC to connect the PC to itself.

We will use a program called Teraterm, a terminal emulator, to allow us to read and write over the RS232 connection.
This project allows us to write over RS232 serial to Teraterm by using the s.write() function.
After user input, the python program waits for a 5 character input from Teraterm before reading it and outputting it back to the user via command line.

A very simple program to test our python to RS232 communication, however it will be integrated with a command line application in the future.

