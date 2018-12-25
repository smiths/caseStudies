from Tamias2D.output import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import math
from itertools import cycle
cycol = cycle('bgrcmk')
class Plotter:
    def __init__(self, whatToPlot = Options.POSITION, timeToPlot=4000, waitToPlot = False):
        self.timeToPlot = timeToPlot
        self.done = False
        self.ready = False
        self.bodiesInfo =  dict()
        self.waitToPlot = waitToPlot
        self.option = whatToPlot
        self.last_plot_type = 0
        self.plot_number = 1

    def add_to_output(self, output):
        self.output = output
        output.plotter = self

    def _to_curve(self, ar, lastN):
        curve = []
        T = None
        if (isinstance(ar[0], list)):
            x = np.array(ar[0])
            y = np.array(ar[1])
            fX = interp1d(np.arange(len(x)), x, kind="quadratic")
            fY = interp1d(np.arange(len(y)), y, kind="quadratic")
            tnew = np.arange(0, len(x)-1, 0.1)
            xnew = fX(tnew)
            curve.append(xnew)

            ynew = fY(tnew)
            T = np.linspace(0, lastN, len(xnew))
            curve.append(ynew)

        else:
            x = np.array(ar)
            fX = interp1d(np.arange(len(x)), x, kind="quadratic")
            tnew = np.arange(0, len(x) - 1, 0.1)
            xnew = fX(tnew)
            T = np.linspace(0, lastN, len(xnew))
            curve.append(xnew)

        return curve, T
    def show(self):
        if self.waitToPlot:
            plt.show()

    def plot(self, options = ''):
       option = None
       if options == '':
         options = self.option
       if not isinstance(options, list):
           opt = options
           options = []
           options.append(opt)
       for option in options:
           bodyIds = self.bodiesInfo.keys()
           isVec = False
           i=1
           nArr =[]
           doneAxes = False
           ax1 = None
           ax2 = None

           for b in bodyIds:
               print("ID: "+b)
               data=[]
               lastN=0
               bodyTimeAr = self.bodiesInfo[b]
               for bodyAtTime in bodyTimeAr:
                   d = bodyAtTime[option]
                   if isinstance(d, Vec2):
                       isVec = True
                       if len(data) == 0:
                           data.append([])
                           data.append([])
                       data[0].append(d.getX())
                       data[1].append(d.getY())
                   else:
                       data.append(d)
                   thisN = bodyAtTime['n']
                   nArr.append(thisN)
                   lastN = math.floor(thisN)
               if len(data) > 0:
                   curve, T = self._to_curve(data, lastN)
                   if not isVec:
                        if self.last_plot_type == 2:
                            self.plot_number +=1
                            plt.figure(self.plot_number)
                        plt.plot(T, curve[0], c=next(cycol), label='body {} - {}'.format(b, option.value), linewidth=2)
                        plt.xlabel('Time')
                        plt.ylabel(option.value)
                        self.last_plot_type = 1

                   else:
                       if self.last_plot_type == 1:
                           self.plot_number += 1
                           plt.figure(self.plot_number)
                       if ax1 == None:
                           fig, (ax1, ax2) = plt.subplots(1, 2)
                       fig.suptitle(option.value +" over time", fontsize = 17)
                       ax1.set_title(option.value + " - " + "X", fontsize = 13)
                       ax2.set_title(option.value + " - " + "Y", fontsize=13)
                       ax1.plot(T, curve[0], c=next(cycol), label='body {}'.format(b), linewidth=2)
                       ax1.set_xlabel('Time')
                       ax1.set_ylabel('X')
                       ax2.plot(T, curve[1], c=next(cycol), label='body {}'.format(b), linewidth=2)
                       ax2.set_xlabel('Time')
                       ax2.set_ylabel('Y')
                       self.last_plot_type = 2
               i+=1
           if isVec:
            ax1.legend()
            ax2.legend()
           else:
            plt.legend()
       if self.waitToPlot:
         plt.show(block = False)
       else:
           plt.show()



