from machine import UART

uart = UART(0, 9600)
uart.init(9600, bits=8, parity=None, stop=1, tx=13)

while True:
