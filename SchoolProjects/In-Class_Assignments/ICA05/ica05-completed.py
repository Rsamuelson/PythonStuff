# Incrementally adding data to a dictionary.
# Often, as we're working on a large set of input, we're collectng results
# in a dictionary (like IA03 - summing data over a set of keys,
# like county names, city names, or store names). We don't know in advance
# what keys will be in the dictionary, so we build it as we go.
# Let's sketch out a typical solution.
# First, create an empty dictionary to keep our sums by some key value.
sums_by_key = {}

# Assume this list of inputs are like the rows of data we're reading from
# a CSV file. Let's use a simple list of sales for this program's input:
sales = [
    ['How-Vee', 70.00],
    ['Fairway', 99.00],
    ['How-Vee', 24.23],
    ['Way-Mart', 77.32],
    ['Way-Mart', 21.55],
    ['How-Vee', 11.11]
]

# Now, we'll complete this loop in class to compute the sum of the
# sales to each store.
for row in sales:
    store_name = row[0]
    sale_amount = row[1]
    if store_name not in sums_by_key:
        sums_by_key[store_name] = 0.0 
    sums_by_key[store_name] += sale_amount



index = 0
for key in sums_by_key:
    index += 1
    print("{:3d}. {:15s} {:8.2f}".format(index, key, sums_by_key[key]))