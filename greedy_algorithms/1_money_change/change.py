# Uses python3
import sys

def get_change(m):

    if m == 1 or m == 5 or m == 10:
    	return 1

    ten = m//10
    five = (m%10)//5
    one = ((m%10)%5)

    #print('Change {} = 10({}) + 5({}) + 1({})'.format(m,ten,five,one))
    return ten+five+one


if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
