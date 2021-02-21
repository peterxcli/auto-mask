import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=10)

while True:
    led_on = input('Do you want the mask close? ')[0]
    if led_on in 'yY':
        ser.write(bytes('YES\n','utf-8'))
    if led_on in 'Nn':
        ser.write(bytes('NO\n','utf-8'))

