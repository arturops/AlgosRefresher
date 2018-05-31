# Uses python3
import sys
import random

def partition3(array, left, right):
    x = array[left]  
    j = left
    for idx in range(left + 1, right + 1):
        if array[idx] < x:
            
    #pass

def partition2(array, left, right):
    x = array[left]
    j = left;
    for i in range(left + 1, right + 1):
        if array[i] <= x:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[left], array[j] = array[j], array[left]
    return j


def randomized_quick_sort(array, left, right):
    """
    Randomized quick sort dividing array in 2 partitions:
        + Greater than pivot
        + Equal to or less than pivot
    """
    if left >= right:
        return
    pivot = random.randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    #use partition3
    pointer = partition2(array, left, right)
    randomized_quick_sort(array, left, pointer - 1);
    randomized_quick_sort(array, pointer + 1, right);


def randomized_quick_sort3(array, left, right):
    """
    Randomized quick sort dividing array in 3 partitions:
        + Greater than pivot
        + Less than pivot
        + Equal to pivot
    """
    if left >= right:
        return
    pivot = random.randint(left,right)
    # swap pivot and left
    array[left], array[pivot] = array[pivot], array[left]
    # divide in partitions 
    pointer1, pointer2 = partition3(array, left, right)
    #recurse on the partitions
    randomized_quick_sort3(array, left, pointer1 -1)
    randomized_quick_sort3(array, pointer2 + 1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
