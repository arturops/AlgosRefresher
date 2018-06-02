# Uses python3
import sys

#input example
#5 1 2 3 4 5
#5 1 2 3 4 5

def binary_search_recursive(a, l, r, x):
    """
    Recursive binary search
    a: sorted array
    l: most left index of array (in each recursion)
    r: most right index of array (in each recursion)
    x: target value (value to search)
    """
    left, right = l, r

    half = left + (right - left)//2
    #print('target: {}'.format(x))
    #print('input array: {}'.format(a))
    #print('half: {}'.format(half))
    #print('--------------------------------------------------')

    if a[half] == x:
        #print('result: {}'.format(half))
        #print('*********************************************')
        return half
    elif a[half] < x:
        return binary_search_recursive(a, half+1, right, x)
    elif a[half] > x:
        return binary_search_recursive(a, left, half-1, x)

    return -1

def binary_search_iter(a, x):
    """
    Iterative binary search
    a: sorted array
    x: target value (value to search)
    Uses less stack (memory space) than the recursive approach
    """

    left, right = 0, len(a)-1

    while left <= right:
    
        half = left + (right - left)//2

        if a[half] == x:
            return half
        elif a[half] < x:
            left = half + 1
        elif a[half] > x :
            right = half - 1

    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search_iter(a, x), end = ' ')
    
    #print()
    #for x in data[n + 2:]:
    #    print(binary_search_recursive(a,0,len(a)-1,x), end = ' ')
