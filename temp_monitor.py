#!/usr/bin/env python3
import math
import time
import pyvisa as visa

translator = str.maketrans('', '', ''.join([chr(char) for char in range(1, 32)]))

def convert_str(foo):
  return foo.translate(translator)

def pt1000_resToTemp(resistance):
  try:
    return -(math.sqrt(17.59246-0.00232*resistance)-3.908)/0.00116
  except:
    return -1.

rm = visa.ResourceManager() #('@py')
print('Detected devices:')
print(rm.list_resources())

#kmm = rm.open_resource('ASRL/dev/ttyUSB2::INSTR', baud_rate = 9600)
kmm = rm.open_resource('ASRL/dev/ttyUSB0::INSTR', baud_rate = 9600)
kmm.timeout = 10000
print(repr(convert_str(kmm.query('*IDN?'))))
kmm.write('*RST')
kmm.write("SENS:FUNC 'RES'")
#kmm.write("SENS:RES:RANGE 1000000")
#kmm.write("SENS:RES:NPLC 1")
#kmm.write("SENS:RES:MODE MAN")

print('-'*55)
print('| {:^24} | {:^24} |'.format('Date & Time', 'Temperature [Celsius]'))
print('-'*55)

while True:
  localtime = time.localtime()
  time_str = time.strftime("%Y/%m/%d %H:%M:%S", localtime)

  try:
    temp_degC = pt1000_resToTemp(float(convert_str(kmm.query('READ?'))))
    print('| {:^24} | {:^24.2f} |'.format(time_str, temp_degC))
  except:
    print('| {:^24} | {:^24} |'.format(time_str, 'N/A'))

  time.sleep(5)

print('-'*55)
