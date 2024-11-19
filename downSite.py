# programming task
#u get array of numbers
#make new array with multiplication of numbers without this one on you are standing

getted = [1,2,3,4]

long = len(getted)
result_left = [1] * long
result_right = [1] * long
result = [1] * long

for i in range(long):   #multiplication from the left
    left = 0
    if(getted[i] == 0):
        result_left[i] = 0
        continue
    while left < i:
        result_left[i] = getted[left] * result_left[left]
        left += 1

print(result_left)

for i in range(long-1,-1,- 1):  #multiplication from the right
    right = long - 1
    if(getted[i] == 0):
        result_right[i] = 0
        continue
    while right > i:
        result_right[i] = getted[right] * result_right[right]
        right -= 1

print(result_right)

for i in range(long): #make final move
    result[i] = result_left[i] * result_right[i]

print(result)