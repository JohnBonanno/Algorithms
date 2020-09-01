'''
Closest pair problem

This returns the closest pair of numbers.

Usage:
    
    python closest_pair.py [size of list of numbers]

[ Garrett Halladay , JOHN BONANNO]

[8/19/2020]
'''

import random
import sys

'''
return the distance between two parameters
'''
def distance(a,b):
    return abs(a-b)


'''
populate the array with listSize unique random numbers between 1 ... 5000
'''
def populate(listSize):
    a = []
    count = 0

    while count < listSize:
        number = random.randint(1,5000)
        if number in a:
            continue
        else:
            a.append(number)
            count += 1

    return a

'''
now determine the closest pair
using brute force algorithm
'''
def closest_pair(values):
    pt_a = -100
    pt_b = 100

    lowestDist = distance(values[0], values[1])

    for x in range (len(values)):
        for y in range (1,len(values)):
            measure = distance(values[x], values[y])
            if measure <= lowestDist and x != y:
                pt_a = values[x]
                pt_b = values[y]
                lowestDist = measure
    return [pt_a, pt_b]


'''
This behaves just like the Java main() method
'''
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage Python closest_pair.py [number of points]')
        quit()
    else:
        numbers = populate(int(sys.argv[1]))

        closest = closest_pair(numbers)

        print('The closest numbers are', closest[0], 'and', closest[1])

