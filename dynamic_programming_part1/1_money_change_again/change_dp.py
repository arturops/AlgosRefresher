# Uses python3
import sys

#Program to exchange money into the minimum amount of coins
# It uses coin denominations of 1, 3 and 4
# Use case of dynamic programming bottom-up case

def get_change(m, coin_denominations=[1,3,4]):
    """
	m : Money to exchange (limitation: this value must be an integer)
	Function returns the minimum number of coins (using coin denominations) 
    """
    # base case	
    if m <= 0:
    	return 0

    # store the number of minimum coins for m amount of money	
    change_table = {}
    change_table[0] = 0

    # build matrix and find change on the process
    for amount in range(1,m+1):
    	change_table[amount] = 999999999 #init min change to a big value
    	for c in coin_denominations:
    		# ensure amount is greater than any coin denomination (no negatives)
    		if amount >= c:
    			min_coins_change = change_table[amount - c] + 1
    			if min_coins_change < change_table[amount]:
    				change_table[amount] = min_coins_change

    return change_table[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
