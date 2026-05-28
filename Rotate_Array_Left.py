#Rotate array left by d positions#
array = [2,45,67,98,76,54,24,100]
print("Before Left Rotation: ",array)
d = 5
array = array[d:] + array[:d]
print("After Left Rotations: ",array)
         
    
   
    