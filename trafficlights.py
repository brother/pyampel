# -*- coding: utf-8 -*-

import time
import subprocess

RED = 0
YELLOW = 1
GREEN = 2
ON = 1
OFF = 0

class TrafficLights(object):
    
    def __init__(self, control_tool, device):
        self.control_tool = control_tool
        self.device = device
        self.all_off()
    
    def set_light(self, light, state):
        cmd = "%s -c 1 -d %s -as %s %s" % (self.control_tool,
                                           self.device,
                                           light,
                                           "1" if state else "0")
        subprocess.check_output(cmd, shell=True)
    
    def set_lights(self, green, yellow, red):
        self.set_light(GREEN, green)
        self.set_light(YELLOW, yellow)
        self.set_light(RED, red)
    
    def all_on(self):
        self.set_lights(ON, ON, ON)
    
    def all_off(self):
        self.set_lights(OFF, OFF, OFF)
    
    def green_only(self):
        self.set_lights(ON, OFF, OFF)
    
    def yellow_only(self):
        self.set_lights(OFF, ON, OFF)
    
    def red_only(self):
        self.set_lights(OFF, OFF, ON)
    
    def blink(self, light, x, duration=0.05):
        for _ in range(x):
            self.set_light(light, ON)
            time.sleep(duration)
            self.set_light(light, OFF)
            time.sleep(duration)
    
    def blink_green(self, x):
        self.blink(GREEN, x)
    
    def blink_yellow(self, x):
        self.blink(YELLOW, x)
    
    def blink_red(self, x):
        self.blink(RED, x)
