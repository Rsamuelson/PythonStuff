

class Stats:
    """ A class to compute statistics for numbers. """
    def __init__(self):
        self.sum = 0.0
        self.count = 0

    def add(self, value):
        # Finish the code to handle a new value
        pass

    def get_average(self):
        # Finish the code to compute the average
        pass

    def get_sum(self):
        # Finish the code to return the sum
        pass

    def get_count(self):
        # Finish the code to return the count
        pass


statistics = Stats()
done = False
while not done:
    value_str = input("Enter number, or 'quit' to finish: ")
    if value_str == 'quit':
        done = True
    else:
        value = float(value_str)
        statistics.add(value)

print("Sum: {}".format(statistics.get_sum()))
print("Average: {}".format(statistics.get_average()))
