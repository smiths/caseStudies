from Tamias2D.body import *
from enum import Enum
import matplotlib.pyplot as plt
import numpy as np
class Options(Enum):
    POSITION = "position"
    ANGLE = "angle"
    VELOCITY = "velocity"
    ANGVEL = "angularVel"
    FORCE = "force"
    TORQUE = "torque"
    ACCEL = "accel"
    ANGACCEL ="angAccel"

class OutputOptions:
    def __init__(self):
        self.options = {
            Options.POSITION: False,
            Options.ANGLE: False,
            Options.VELOCITY: False,
            Options.ANGVEL: False,
            Options.FORCE: False,
            Options.TORQUE: False,
            Options.ACCEL: False,
            Options.ANGACCEL: False
        }
    def __getitem__(self, key):
        if key in self.options:
            return  self.options[key]
        else:
            raise Exception("Key {0} doesn't exist in options".format(key))
    def __setitem__(self, key, value):
        if key in self.options:
            self.options[key] = value
        else:
            raise Exception("Key {0} doesn't exist in options".format(key))
    def enable_option(self, key):
        if key in self.options:
            self.options[key] = True

    def disable_option(self, key):
        if key in self.options:
            self.options[key] = False

class PhysicsOutput:
    def __init__(self, frequency = 1000, options = OutputOptions(), shouldOutput = False):
        self.deltaTime = frequency
        self.elapsedTime = 0
        self.frequency = frequency
        self.bodies = []
        self.options = options

        self.plotter = None
        self.plotTimer = 0
        self.n=0
        self.nPartial = 0
    def add_body(self, body):
        if isinstance(body, Body):
            self.bodies.append(body)

    def update(self, deltaTime):
        self.deltaTime += deltaTime*1000
        self.elapsedTime +=deltaTime*1000
        if self.deltaTime > self.frequency:
            self.deltaTime = 0
            self._print_output()
        if self.plotter != None:
            self.plotTimer += deltaTime*1000
            self.nPartial = self.n + (self.deltaTime/self.frequency)
            self.plotTimer = 0
            if not self.plotter.done:
                self._add_frame_info()
                if self.elapsedTime > self.plotter.timeToPlot:
                    if not self.plotter.done and not self.plotter.ready:
                        self._print_output()
                        self.plotter.ready = True
                        self.plotter.plot()
                        self.plotter.done = True
                        return





    def set_options(self, options):
        if isinstance(options, OutputOptions):
            for key in self.options.options.keys():
                self.options[key] = options[key]
    def _add_frame_info(self):
        i = 0
        for b in self.bodies:
            bInfo = dict()
            bInfo ['n'] = self.nPartial
            if self.options[Options.POSITION]:
                bInfo[Options.POSITION] = b.position
            if self.options[Options.VELOCITY]:
                bInfo[Options.VELOCITY] = b.velocity
            if self.options[Options.ACCEL]:
                bInfo[Options.ACCEL] = b.accel
            if self.options[Options.ANGLE]:
                bInfo[Options.ANGLE] = b.angle
            if self.options[Options.ANGVEL]:
                bInfo[Options.ANGVEL] = b.angularVel
            if self.options[Options.ANGACCEL]:
                bInfo[Options.ANGACCEL] = b.angularAccel
            if self.options[Options.FORCE]:
                bInfo[Options.FORCE] = b.force
            if self.options[Options.TORQUE]:
                bInfo[Options.TORQUE] = b.torque
            bTimeInfo = []
            sI = str(i)
            if sI in self.plotter.bodiesInfo:
                bTimeInfo = self.plotter.bodiesInfo[sI]
            bTimeInfo.append(bInfo)
            self.plotter.bodiesInfo[sI] = bTimeInfo
            i+=1
    def _print_output(self):
        i=0
        print("---------At n = {}---------".format(self.n))
        for b in self.bodies:
            print("==Body"+str(i)+": ")
            if self.options[Options.POSITION]:
                print("Pos: "+str(b.position))
            if self.options[Options.VELOCITY]:
                print("Vel: "+str(b.velocity))
            if self.options[Options.ACCEL]:
                print("Accel: "+str(b.accel))
            if self.options[Options.ANGLE]:
                print("Angle: "+str(b.angle))
            if self.options[Options.ANGVEL]:
                print("Angular Vel: "+str(b.angularVel))
            if self.options[Options.ANGACCEL]:
                print("Angular Accel: "+str(b.angularAccel))
            if self.options[Options.FORCE]:
                print("Affecting Force: "+str(b.force))
            if self.options[Options.TORQUE]:
                print("Affecting Force: "+str(b.torque))
            print("=========")

            i+=1
        self.n+=1

