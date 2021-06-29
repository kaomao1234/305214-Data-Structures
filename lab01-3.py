import math
x,y,z = (int(input()) for i in range(3)) 
posi_a = math.sqrt(x**2+y**2)
posi_b = z 
print("Mr. A is far from the starting point {0}".format(posi_a))
print("Mr. B is far from the starting point {0}".format(posi_b))
print("{0} is closer to the starting point.".format("A" if posi_a < posi_b else "No One" if posi_a == posi_b else "B"))