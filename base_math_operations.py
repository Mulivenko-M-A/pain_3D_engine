import math as m

class vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def GetLength(self):
        l_x = self.x
        l_y = self.y
        l_z = self.z
        return m.sqrt(l_x*l_x+l_y*l_y+l_z*l_z)
        
    def __add__(self, other):
        return vector3(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __sub__(self, other):
        return vector3(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return vector3(self.x*other, self.y*other, self.z*other)
        elif isinstance(other,vector3):
            return (self.x*other.x)+(self.y*other.y)+(self.z*other.z)
        raise TypeError("умножай на число или вектор, мудила")
    
    def __truediv__(self, other):
        if isinstance(other,(int,float)):
            return vector3(self.x/other, self.y/other, self.z/other)
        raise TypeError("дели на число, мудила")
    
    def __neg__(self):
        return vector3(-self.x, -self.y, -self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def Normalize(self):
        l_lenght = self.GetLength()
        self = self/l_lenght
        return self
