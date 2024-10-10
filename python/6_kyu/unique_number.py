"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

"""

def find_uniq(arr):
    num1 = arr[0]
    num2 = arr[1]
    if num1 == num2:
        n = [num for num in arr[2:] if num != num1] 
        return n[0]
    
    if num1 == arr[2]:
        return num2
    return num1