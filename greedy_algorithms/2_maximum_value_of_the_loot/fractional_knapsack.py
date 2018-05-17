# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # debug statements
    #print('Capacity: {}'.format(capacity))
    #print('Values: {}'.format(values)) # first column
    #print('Weights: {}'.format(weights)) # second column

    # need to compute unit price fo each
    unit_price = { i:(1.0*val/(1.0*weight)) \
    				for i, (val, weight) in enumerate(zip(values,weights)) }
    #print('Unit price: {}'.format(unit_price))

    # sort by maximum unit price first
    item_index = sorted(unit_price, key=unit_price.__getitem__, reverse=True)
    #print(item_index)
    
    # find a way to relate the unit price back to its item (no need only returing value)
    for item in item_index:
    	if capacity <= 0:
    		return value
    	amount = min(weights[item],capacity)
    	value += (amount* unit_price[item])
    	capacity -= amount
    	weights[item] -= amount

    return value


if __name__ == "__main__":
    
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
