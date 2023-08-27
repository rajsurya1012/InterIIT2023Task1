from plutodrone import *
import numpy as np
import time

class pluto_control():
    
    def __init__(self):        
        self.quadCopter=plutodrone("192.168.4.1", 23)
        self.quadCopter.arm()
        
        self.quadCopter.roll = 1500
        self.quadCopter.pitch = 1500
        self.quadCopter.throttle = 1500
        self.quadCopter.yaw = 1500
        
    def sequence(self):
        
        try:
            # Takeoff
            self.quadCopter.takeoff()
            
            # Pitch forward
            print("PITCH FRONT")
            self.quadCopter.pitch = 1600
            period = 1
            self.quadCopter.setcmd(period)
            
            # Counter Pitch
            print("COUNTER PITCH")
            self.quadCopter.pitch = 1300
            period = 0.3
            self.quadCopter.setcmd(period)
            
            #Reset Pitch
            self.quadCopter.pitch=1500

            # Roll
            print("ROLL RIGHT")
            self.quadCopter.roll =1600 
            period = 1
            self.quadCopter.setcmd(period)
            
            # Counter Roll
            print("COUNTER ROLL")
            self.quadCopter.roll = 1300
            period = 0.3
            self.quadCopter.setcmd(period)
            
            #Reset Roll
            self.quadCopter.roll=1500

            # Pitch backward
            print("PITCH BACK")
            self.quadCopter.pitch = 1400
            period = 1
            self.quadCopter.setcmd(period)
            
            # Counter pitch
            print("COUNTER PITCH")
            self.quadCopter.pitch = 1700
            period = 0.2
            self.quadCopter.setcmd(period)
        
            #Reset Pitch
            self.quadCopter.pitch=1500

            # Roll
            print("ROLL LEFT")
            self.quadCopter.roll =1400 
            period = 1
            self.quadCopter.setcmd(period)
            
            # Counter roll
            print("COUNTER ROLL")
            self.quadCopter.roll = 1700
            period = 0.2
            self.quadCopter.setcmd(period)
        
            #Reset Roll
            self.quadCopter.roll=1500
        
            self.quadCopter.throttle=1500

            # Clockwise Yaw
            print("YAW CLOCKWISE")
            self.quadCopter.yaw =1800
            period = 1
            self.quadCopter.setcmd(period)
            
            # Yaw to zero
            self.quadCopter.yaw=1500
            period = 0.5
            self.quadCopter.setcmd(period)

            # Anticlockwise Yaw
            print("YAW ANTI-CLOCKWISE")
            self.quadCopter.yaw =1200
            period = 1
            self.quadCopter.setcmd(period)
            
            # Yaw to zero
            self.quadCopter.yaw=1500
            period = 0.5
            self.quadCopter.setcmd(period)

            #Land
            self.quadCopter.land()
            
            #Disarm and Disconnect
            self.quadCopter.disarm()
            self.quadCopter.disconnect()

        except KeyboardInterrupt:
            self.quadCopter.land()
            self.quadCopter.disarm()
            self.quadCopter.disconnect()
        
if __name__ == "__main__":
    drone = pluto_control()
    drone.sequence()