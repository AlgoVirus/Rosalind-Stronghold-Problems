def total_rabbits(n, k):
    #base cases
    if n == 1 or n == 2:
        return 1
    
    # Initialize the first two months
    rabbits = [0] * (n +1)
    rabbits[1], rabbits[2] = 1, 1


    # Compute using recurrence relation
    for i  in range(3, n + 1):
        rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2]    
    
    return rabbits[n]

# sample input
n, k = 33, 3
print(total_rabbits(n, k))  