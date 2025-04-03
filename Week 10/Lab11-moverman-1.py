# M. Overman, 4/3/2025
# lab 11, question 1

def clampAngle(angle):
    a = angle
    while a > 360 or a < 0:
        if a > 360:
            a -= 360
        elif a < 0:
            a += 360
    return a

print(clampAngle(460))
print(clampAngle(-100))