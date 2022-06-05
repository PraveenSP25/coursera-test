import math
for i in range(1,90):
    s = math.sqrt(i)
    if s - math.floor(s) == 0:
       print(i)


