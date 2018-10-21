"""
This is octopusLab basic library for robotBoard PCB
Edition: --- 21.10.2018 ---

Installation:
ampy -p /dev/ttyUSB0 put ./octopus_robot_board.py
"""

#ESP32 pinout setup
BUILT_IN_LED = 2
WS_LED_PIN = 13    #ws RGB ledi diode
ONE_WIRE_PIN = 32  #one wire (for Dallas temperature sensor)

#I2C:
I2C_SCL_PIN = 22
I2C_SDA_PIN = 21

#PWM/servo:
PIN_PWM1 = 17
PIN_PWM2 = 16
PIN_PWM3 = 4

#inputs:
I39 = 39
I34 = 34
I35 = 35

#main analog input (for power management)
PIN_ANANALOG = 36

#---/