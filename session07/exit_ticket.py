#!/usr/bin/env python3

import math

#1
var1 = "9.2"
var2 = 17
var3 = 3.4

print(type(var1))
print(type(var2))
print(type(var3))

#2
var4 = "19"
print(int(var4))

#3
var5 = -26 
print(str(var5))

#4
var6 = 83
print(float(var6))

#5
varadd = int(var4) + var5
print(varadd)

#6
varsub = var2 - float(var1)
print(varsub)

#7
varmult = int(var5) * var3
print(varmult)

#8
varpow = pow(var3, float(var1))
print(varpow)

#9
var7 = 9
varsqrt = math.sqrt(var7)
print(varsqrt)

#10
var8 = 10
pi = 3.1459
varcir = 2 * pi * var8
print(f'The circumference of a circle with a radius of 10 cm is {varcir} cm.')

#11
var9 = 33 + 37 + 35 + 31 + 29 + 39
varhour = var9 / 60
print(f'The employee spent {varhour} hours driving.')