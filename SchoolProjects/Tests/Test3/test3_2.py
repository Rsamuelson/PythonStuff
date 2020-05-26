def generate_evens(max):
    # Yield even numbers starting at 2.
    for n in range(2, max):
        if n%2 == 0:
            yield n
    

max = int(input("Enter the maximum number: "))
for x in generate_evens(max):
    print(x)