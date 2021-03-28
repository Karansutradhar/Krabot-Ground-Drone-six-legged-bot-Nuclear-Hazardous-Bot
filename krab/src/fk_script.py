#!/usr/bin/env python
import numpy as np

th1 = 0.81, th2 = 0, th3 = 1.22, th4 = 0, th5 = -0.89, th6 = 0

a1 = 8.5, a2 = 20, a3 = 22, a4 = 1.97, a5 = 2.53, a6 = 8.61

c1 = np.cos(th1), c2 = np.cos(th2), c3 = np.cos(th3)
c4 = np.cos(th4), c5 = np.cos(th5), c6 = np.cos(th6)

s1 = np.sin(th1), s2 = np.sin(th2), s3 = np.sin(th3)
s4 = np.sin(th4), s5 = np.sin(th5), s6 = np.sin(th6)

a = -c1*c2*s3 - c1*s2*c3, b = -s1*c2*s3 - s1*s2*c3, c = c2*c3 - s2*s3

r11 = c5*c6*(a*c4 + s1*s4) - a*s5*c6 - a*s4*s6 + s1*c4*s6
r12 = c5*s6*(a*c4 + s1*s4) + a*s5*s6 - a*s4*c6 + s1*c4*c6
r13 = -s5*(a*c4 + s1*s4) - a*c5
r21 = c5*c6*(c4*b - c1*s4) - b*s5*c6 - s6*(s4*b + c1*c4)
r22 = -c5*s6*(c4*b - c1*s4) + b*s5*s6 - c6*(s4*b + c1*c4)
r23 = -s5*(c4*b - c1*s4) - b*c5
r31 = c*c4*c5*c6 - c*s5*c6 - c*s4*s6
r32 = -c*c4*c5*s6 + c*s5*s6 - c*s4*c6
r33 = -c*c4*s5 - c*c5
dx = (a5+a6)*r13 + a2*c1*c2 - a*(a3+a4)
dy = (a5+a6)*r23 + a2*s1*c2 - b*(a3+a4)
dz = (a5+a6)*r33 + a1 + a2*s2 -c*(a3+a4)

print(r11)
print('\n')
print(r12)
print('\n')
print(r13)
print('\n')
print(r21)
print('\n')
print(r22)
print('\n')
print(r23)
print('\n')
print(r31)
print('\n')
print(r32)
print('\n')
print(r33)
print('\n')
print(dx)
print('\n')
print(dy)
print('\n')
print(dz)
print('\n')