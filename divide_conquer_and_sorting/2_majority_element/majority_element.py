# Uses python3
import sys

def get_majority_element(a, left, right):
    #if left == right:
    #    return -1
    #if left + 1 == right:
    #    return a[left]
    #write your code here
    return -1


def get_majority_element_fast(array):
    """
    Returns the majority element if there is any, else -1
    """
    counts = {}
    for element in array:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    #print('counts: {}'.format(counts))

    n = len(array)
    for key,value in counts.items():
        if value > n//2:
            return counts[key]

    return -1 


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #if get_majority_element(a, 0, n) != -1:
    if get_majority_element_fast(a) != -1:
        print(1)
    else:
        print(0)
