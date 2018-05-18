# Uses python3
import sys

def optimal_summands(n):
    """
	Finds the maximum number of different numbers that added together give n
    """
    summands = []
    i = 1
    while(n != 0):
    	#print('n-i:{}-{} = {}'.format(n,i,n-i))
    	if(n-i > i or n-i == 0):
    		summands.append(i)
    		n -= i
    		i += 1
    	else:
    		i = n
    	#print(summands)
    	#print('new n,i: {},{}'.format(n,i))

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
