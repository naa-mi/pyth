#area calculator
import math

print('1. Triangle')
print('2. Rectangle')
print('3. Square')
print('4. Circle')
print('5. Quit')
shape=int(input('Select a shape(1-5):'))
if shape == 1:
    h=float(input('height:'))
    b=float(input('base:'))
    print('\nArea of triangle:',(h*b)/2)
elif shape == 2:
    l=float(input('length:'))
    w=float(input('width:'))
    print('\nArea of rectangle:',l*w)
elif shape == 3:
       s=float(input('side:'))
       print('\nArea of square:',s**2)
elif shape == 4:
     r=float(input('radius:'))
     print('\nArea of circle:',math.pi*(r**2))  
elif shape == 5:
     print('\nQuit')
else:
     print('\nINVALID')     
         




