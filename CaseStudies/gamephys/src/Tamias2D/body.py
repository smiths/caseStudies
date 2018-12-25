from Tamias2D.vec2 import *
from Tamias2D.shapes import *
class Body:
    STATIC = 0
    DYNAMIC = 1
    MAX_V_VELOCITY = 1000
    MAX_ANG_VEL = 200
    MAX_TORQUE = 10000
    def __init__(self, position_, mass_,  shape_, angle=0, bodyType_= DYNAMIC, restitution_ = 1):
        self.position = position_
        self.mass = mass_
        self.inv_mass = 1/max(mass_, 0.1)
        self.force = Vec2(0,0)
        self.velocity = Vec2(0,0)
        self.lastVel = Vec2(0, 0)
        self.accel = Vec2(0,0)
        self.lastAccel = Vec2(0,0)
        self.torque = 0
        self.lastTorque = 0
        self.angle = angle
        self.lastAngle = angle
        self.angularVel = 0
        self.lastAngularVel = 0
        self.avg_ang_vel = 0
        self.angularAccel=0
        self.bodyType = bodyType_
        self.shape = shape_
        self.shape.set_pos(position_)
        self.shape.set_angle(angle)
        self.gravity = Vec2(0,0)
        self.restitution = restitution_
        self.isBotCol = False
        self._calc_moment_of_inertia()
        self.should_clamp_angle = True
    #in: deltaTime(float)
    #out: void

    def update(self, deltaTime):
        if self.bodyType == Body.DYNAMIC:
            self.lastAngularVel = self.angularVel
            self.angle += self.angularVel * deltaTime + (0.5 * self.angularAccel * (deltaTime*deltaTime))
            self.angularAccel = (self.torque / self.inertia)

            self.angularVel += self.angularAccel * deltaTime
            self.avg_ang_vel = (self.angularVel +self.lastAngularVel)/2
            self._clamp_angle()

            gravity = self.gravity
            if self.isBotCol:
                gravity=Vec2(0,0)


            self.thrust = self.force
            self.lastAccel = self.accel
            self.position += ((self.velocity) * 0.5) * deltaTime + (0.5 *self.lastAccel *(deltaTime*deltaTime))
            self.accel = (self.force/ self.mass) + gravity
            avg_accel = (self.lastAccel + self.accel)/2

            self.lastVel = self.velocity
            self.velocity += avg_accel * deltaTime



            self.shape.set_pos(self.position)
            self.shape.set_angle(self.angle)


        else:
            self.velocity=Vec2(0,0)
            self.accel =Vec2(0,0)
            self.torque = 0
        self.lastDeltaTime = deltaTime

    #input: force_ (Vec2)
    def apply_force(self, force_):
        force_ = force_
        self.force += force_

    #input: torque_ (float)
    def apply_torque(self, torque_):
        self.torque += torque_

    # input: torque_ (float)
    def set_torque(self, torque_):
        self.torque = torque_

    #input: space_ (Space)
    def set_space(self, space_):
        self.space = space_
        self.gravity = space_.gravity
    def _clamp_angle(self):
        if self.should_clamp_angle:
            if self.angle > 360:
                self.angle -= 360 * (math.ceil(self.angle/360))
            if self.angle < 0:
                self.angle += 360 * (math.ceil(abs(self.angle)/360))
    def _calc_moment_of_inertia(self):
        m = self.mass
        w = self.shape.get_width()
        h = self.shape.get_height()
        self.inertia = m * (w * w + h * h) / 1200

