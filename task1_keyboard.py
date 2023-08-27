from plutodrone import *
import keyboard
import time

class pluto_keyboard():
    
    def __init__(self):        
        self.quadCopter=plutodrone("192.168.4.1", 23)
        
        self.quadCopter.roll = 1500
        self.quadCopter.pitch = 1500
        self.quadCopter.throttle = 1000
        self.quadCopter.yaw = 1500
        self.flag_takeoff=0
        self.flag_arm = 0

    def key_cmd(self):
        # Arm
        if keyboard.is_pressed('v'): #v
            if self.flag_arm == 0:
                print('arm')
                self.quadCopter.arm()
                self.flag_arm =1
            else:
                print('armed')
        
        # Disarm
        elif keyboard.is_pressed('b'): #b
            if self.flag_arm == 1:
                print('disarm')
                self.quadCopter.disarm()
                self.flag_arm = 0
            else:
                print('disarmed')

        # Increase Height
        elif keyboard.is_pressed('w'): #w
            print('increase height')
            self.quadCopter.throttle = 1800
            self.quadCopter.setcmd(0.02)

        # Decrease Height
        elif keyboard.is_pressed('s'): #s
            print('decrease height')
            self.quadCopter.throttle = 1400
            self.quadCopter.setcmd(0.02)

        # Roll Right
        elif keyboard.is_pressed('l'): #l
            print('roll right')
            self.quadCopter.roll = 1600
            self.quadCopter.setcmd(0.02)

        # Roll Left
        elif keyboard.is_pressed('j'): #j
            print('roll left')
            self.quadCopter.roll = 1400
            self.quadCopter.setcmd(0.02)

        # Pitch Front
        elif keyboard.is_pressed('i'): #i
            print('pitch front')
            self.quadCopter.pitch = 1600
            self.quadCopter.setcmd(0.02)

        # Pitch Back
        elif keyboard.is_pressed('k'): #k
            print('pitch back')
            self.quadCopter.pitch = 1400
            self.quadCopter.setcmd(0.02)

        # Yaw Clockwise
        elif keyboard.is_pressed('d'): #d
            print('yaw clockwise')
            self.quadCopter.yaw = 1800
            self.quadCopter.setcmd(0.02)

        # Yaw Anticlockwise
        elif keyboard.is_pressed('a'): #a
            print('yaw anticlockwise')
            self.quadCopter.yaw = 1200
            self.quadCopter.setcmd(0.02)

        # Takeoff
        elif keyboard.is_pressed('t'): #t

            if self.flag_takeoff==0:
                print('takeoff')
                self.quadCopter.takeoff()
                self.flag_takeoff = 1

        # Land
        elif keyboard.is_pressed('y'): #y
            if self.flag_takeoff == 1:
                print('land')
                self.quadCopter.land()
                self.flag_takeoff = 0

        # Reset to hover
        else:
            self.quadCopter.roll = 1500
            self.quadCopter.pitch = 1500
            self.quadCopter.throttle = 1500
            self.quadCopter.yaw = 1500
            self.quadCopter.setcmd(0.02)
        
if __name__ == "__main__":
    drone = pluto_keyboard()
    while 1:
        drone.key_cmd()
        