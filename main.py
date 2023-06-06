import serial
import time

#We must make sure we match the port, baudrate, parity, stop bits, and byte size (no parity for this ex)
s = serial.Serial(port='COM4', baudrate=9600, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

inp = ''
answer = ''
while(answer != "n"):

    inp = input("Enter some info to be written to Teraterm\n")
    print("Enter something in Teraterm to be read over RS232 (limit 5 hex characters)\n")

    s.write(bytes(inp, 'utf-8'))
    out = ''

    time.sleep(1)

    out = s.read(5)
    print(out.decode('utf-8'))
    answer = input("Do you want to continue? (y/n)\n")



