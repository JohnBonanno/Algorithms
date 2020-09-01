'''
    CoPrime.py

    Generates a graph of the m x n co-primes
    
    [John Bonanno]
'''
#import math
import sys

'''
generates the co-primes in an m x n matrix
'''
def coprimes(m, n):
    '''
    creates a list of size n each with
    each element initialized to None
    '''
    result = [None] * (m + 1)

    '''
    each element in the list is now a
    list of size m where each value
    is initialized to a space ' '
    '''
    for i in range(m+1):
        result[i] = [''] * (n + 1)
    '''
    output the contents of result
    '''
    for x in range (m,0,-1):
       
        for y in range (1,n+1):
            row = result[x] #iterate over row, then iterate over result after
            if(gcd (x,y) == 1):
                row[y]="*"
            else:    
                row[y]=" "


    for x in result[::-1]:
        # x[:] is a list "slice"
        for y in x[:]:
            '''
            by putting a comma at the end, we prevent a newline
            '''
            
            print(y + ' ', end="")
            
        print()

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x%y)
print(gcd(10,2))
'''
this is euclids from discrete
'''



if __name__ == "__main__":
    # some error checking
    if len(sys.argv) != 3:
        print('Usage\n python CoPrime [int] [int]')
        quit()

    coprimes(int(sys.argv[1]), int(sys.argv[2]))
