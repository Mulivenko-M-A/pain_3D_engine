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

    def GetCoordinates(self):
        return (self.x, self.y, self.z)
        
    def __add__(self, other):
        if isinstance(other,vector3):
            return vector3(self.x+other.x, self.y+other.y, self.z+other.z)
        raise TypeError("прибавляй вектор, мудила")
    
    def __sub__(self, other):
        if isinstance(other,vector3):
            return vector3(self.x-other.x, self.y-other.y, self.z-other.z)
        raise TypeError("вычитай вектор, мудила")
    
    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return vector3(self.x*other, self.y*other, self.z*other)
        elif isinstance(other,vector3):
            return (self.x*other.x)+(self.y*other.y)+(self.z*other.z)
        elif isinstance(other,matrix3):
            return vector3(self.x*other.r1[0] + self.y*other.r2[0] + self.z*other.r3[0],
                           self.x*other.r1[1] + self.y*other.r2[1] + self.z*other.r3[1],
                           self.x*other.r1[2] + self.y*other.r2[2] + self.z*other.r3[2])
        raise TypeError("умножай на число, вектор или матрицу, мудила")
    
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


class matrix3:
    def __init__(self, r1=(0, 0, 0), r2=(0, 0, 0), r3=(0, 0, 0)):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3

    def Determinant(self):
        return self.r1[0]*self.r2[1]*self.r3[2]+self.r2[0]*self.r3[1]*self.r1[2]+self.r3[0]*self.r1[1]*self.r2[2]-self.r3[0]*self.r2[1]*self.r1[2]-self.r2[0]*self.r1[1]*self.r3[2]-self.r1[0]*self.r3[1]*self.r2[2]

    def Transpose(self):
        return matrix3((self.r1[0],self.r2[0],self.r3[0]),
                       (self.r1[1],self.r2[1],self.r3[1]),
                       (self.r1[2],self.r2[2],self.r3[2]))

    def __add__(self, other):
        if isinstance(other,matrix3):
            return matrix3((self.r1[0]+other.r1[0], self.r1[1]+other.r1[1], self.r1[2]+other.r1[2]),
                           (self.r2[0]+other.r2[0], self.r2[1]+other.r2[1], self.r2[2]+other.r2[2]),
                           (self.r3[0]+other.r3[0], self.r3[1]+other.r3[1], self.r3[2]+other.r3[2]))
        raise TypeError("прибавляй матрицу, мудила")
    
    def __sub__(self, other):
        if isinstance(other,matrix3):
            return matrix3((self.r1[0]-other.r1[0], self.r1[1]-other.r1[1], self.r1[2]-other.r1[2]),
                           (self.r2[0]-other.r2[0], self.r2[1]-other.r2[1], self.r2[2]-other.r2[2]),
                           (self.r3[0]-other.r3[0], self.r3[1]-other.r3[1], self.r3[2]-other.r3[2]))
        raise TypeError("вычитай матрицу, мудила")
    
    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return matrix3((self.r1[0]*other, self.r1[1]*other, self.r1[2]*other),
                           (self.r2[0]*other, self.r2[1]*other, self.r2[2]*other),
                           (self.r3[0]*other, self.r3[1]*other, self.r3[2]*other))
        elif isinstance(other,vector3):
            return vector3(self.r1[0]*other.x + self.r1[1]*other.y + self.r1[2]*other.z,
                           self.r2[0]*other.x + self.r2[1]*other.y + self.r2[2]*other.z,
                           self.r3[0]*other.x + self.r3[1]*other.y + self.r3[2]*other.z)
        elif isinstance(other,matrix3):
            return matrix3((self.r1[0]*other.r1[0] + self.r1[1]*other.r2[0] + self.r1[2]*other.r3[0], self.r1[0]*other.r1[1] + self.r1[1]*other.r2[1] + self.r1[2]*other.r3[1], self.r1[0]*other.r1[2] + self.r1[1]*other.r2[2] + self.r1[2]*other.r3[2]),
                           (self.r2[0]*other.r1[0] + self.r2[1]*other.r2[0] + self.r2[2]*other.r3[0], self.r2[0]*other.r1[1] + self.r2[1]*other.r2[1] + self.r2[2]*other.r3[1], self.r2[0]*other.r1[2] + self.r2[1]*other.r2[2] + self.r2[2]*other.r3[2]),
                           (self.r3[0]*other.r1[0] + self.r3[1]*other.r2[0] + self.r3[2]*other.r3[0], self.r3[0]*other.r1[1] + self.r3[1]*other.r2[1] + self.r3[2]*other.r3[1], self.r3[0]*other.r1[2] + self.r3[1]*other.r2[2] + self.r3[2]*other.r3[2]))
        raise TypeError("умножай на число, вектор или матрицу, мудила")
    
    def __truediv__(self, other):
        if isinstance(other,(int,float)):
            return matrix3((self.r1[0]/other, self.r1[1]/other, self.r1[2]/other),
                           (self.r2[0]/other, self.r2[1]/other, self.r2[2]/other),
                           (self.r3[0]/other, self.r3[1]/other, self.r3[2]/other))
        raise TypeError("дели на число, мудила")
    
    def __neg__(self):
        return matrix3((-self.r1[0],-self.r1[1],-self.r1[2]),
                       (-self.r2[0],-self.r2[1],-self.r2[2]),
                       (-self.r3[0],-self.r3[1],-self.r3[2]))

    def __str__(self):
        return f"|{self.r1}|\n|{self.r2}|\n|{self.r3}|"
