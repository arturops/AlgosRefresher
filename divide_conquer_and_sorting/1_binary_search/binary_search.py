# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)

    half = (left + right)//2
    #print('target: {}'.format(x))
    #print('input array: {}'.format(a))
    #print('half: {}'.format(half))
    #print('--------------------------------------------------')

    if a[half] == x:
        #print('result: {}'.format(half))
        #print('*********************************************')
        return half
    elif half <= 0:
        #print('result: -1')
        #print('*********************************************')
        return -1
    elif a[half] < x:
        b = a[(half+1):(right-1)]
        b.append(a[-1])
        return binary_search(b,x)
    elif a[half] > x:
        return binary_search(a[left:half],x)

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
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
