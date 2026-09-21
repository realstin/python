import math 

print(math.pi)
print(math.sqrt(81))
angle = 45
# converting in radians 

radian_angle = math.radians(angle)
# we do this because cos() of math expect the parameter as radians 
# so to find the the cosine of it we will use that radian value

print(math.cos(radian_angle))  # this is the cosine of 45 degrees 