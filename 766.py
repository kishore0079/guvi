import math
def area_equilateral( side ): 
    area = (math.sqrt(3) / 4) * side * side 
    print ("%.2f"%round(area,2)) 

side =float(input())
area_equilateral( side ) 
