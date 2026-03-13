from base_math_operations import*

class object:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0, 0), scl=(0,0,0)):
        self.pos = pos
        self.rot = rot
        self.scl = scl

class camera:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0, 0)):
        self.pos = pos
        self.rot = rot
