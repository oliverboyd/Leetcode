# https://leetcode.com/problems/trapping-rain-water

def left_maxs(height):
    array = []
    array.append(height[0])
    for i in range(1,len(height)):
        if height[i] > array[i-1]:
            array.append(height[i])
        else:
            array.append(array[i-1])
    array.append(0)
    return array

def right_maxs(height):
    L  = len(height)
    array = []
    array.append(height[L-1])
    for i in range(1,len(height)):
        if height[L-1-i] > array[i-1]:
            array.append(height[L-1-i])
        else:
            array.append(array[i-1])
    array2 = array[::-1]
    array2.append(0)
    return array2

def trap(height):
    leftarray = left_maxs(height)
    rightarray = right_maxs(height)
    water_blocks = 0
    for x in range(len(height)):
        max = min(leftarray[x-1],rightarray[x+1])
        if height[x] < max :
            water_height = max - height[x]
            water_blocks += water_height
    return water_blocks