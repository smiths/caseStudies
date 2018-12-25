import datetime
import time
import math
class Clock:
    start = datetime.datetime.now()
    def __init__(self):
        self.lastTime = Clock.get_in_ms()
        self.timeSinceLastRefresh = 0
        self.framesCounter = 0;
        self.elapsedTime = 0
        self.deltaTime = 0

    def get_delta_time(self):
        now = Clock.get_in_ms()
        dt =  Clock.get_in_ms() - self.lastTime
        self.lastTime = now

        return dt
    def tick(self, fps):
        dT = self.get_delta_time()
        self.timeSinceLastRefresh += dT
        refreshTime = 1000/fps
        if self.timeSinceLastRefresh < refreshTime:
            delta = refreshTime - self.timeSinceLastRefresh
            time.sleep(delta/1000)
        else:
            self.framesCounter+=1
            self.timeSinceLastRefresh = 0

        self.elapsedTime += dT
        if(self.elapsedTime > 1000):

            self.elapsedTime = 0
            self.framesCounter =0
        if dT == 0:
            dT = 0.1
        return round(1/fps, 5)
    @classmethod
    def get_in_ms(cls):
        t = datetime.datetime.now() - Clock.start
        return t.total_seconds()*1000


