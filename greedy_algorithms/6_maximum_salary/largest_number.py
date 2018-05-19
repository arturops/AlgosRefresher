#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    for x in a:
        res += x
    return res


def largest_num(digits):

	answer = ""

	while len(digits)>0:
		maxDigit = '0' #-999999999999999999
		for digit in digits:
			if num_comparison(digit,maxDigit): # comparing strings first position
				maxDigit = digit
		answer += maxDigit
		digits.remove(maxDigit)
	return answer


def num_comparison(a,b, base=10):

	if int(a[0]) >= int(b[0]):
			return True
	return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_num(a))
    

