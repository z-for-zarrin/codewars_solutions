"""
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will
have a volume of n^3, the cude above will have a volume of (n-1)^3 and so on until the top which
will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find the number n of cubes
you will have to build?

The parameter of the function find_nd will be an integer m and you have to return the integer n
such that
    n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = m
if such an n exists, or -1 if there is no such n.

Examples:
find_nb(1071225) --> 45

find_nb(91716553919377) --> -1
"""

def find_nb(m):
    n = 0
    while m > 0:
        n += 1
        m -= n**3
    
    return n if m == 0 else -1

if __name__ == '__main__':
    print(find_nb(1071225))
    print(find_nb(9))
    print(find_nb(5))
