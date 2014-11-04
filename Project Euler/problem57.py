import math

# Normal recursive gcd causes stack overflow... Pretty big fractions
def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a

class frac(object):
    a = 0
    b = 0 
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reduce(self):
        diver = gcd(self.b,self.a)
        self.a /= diver
        self.b /= diver

    def __repr__(self):
        return str(self.a) + "/" + str(self.b)

    def minus(self, other):
        temp = self.b
        self.a *= other.b
        self.b *= other.b
        other.a *= temp
        other.b *= temp
        self.a -= other.a
        self.reduce()
        
        return frac(self.a, self.b)

    def add(self, other):
        temp = self.b
        self.a *= other.b
        self.b *= other.b
        other.a *= temp
        other.b *= temp
        self.a += other.a
        self.reduce()
        return frac(self.a, self.b)

    def div(self, other):
        self.a *= other.b
        self.b *= other.a
        self.reduce()
        return frac(self.a, self.b)
        
n = 1000 
a = frac(2, 1)
x = frac(1, 1)
count = 0

for i in range(n):
    divv = frac(1,1).add(x)
    min = a.minus(frac(1,1))
    a.add(frac(1,1))
    x = frac(1, 1).add(min.div(divv))
    if len(str(x.a)) > len(str(x.b)):
        count += 1
        
print count
