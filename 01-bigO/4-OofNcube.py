# Here it is O(n^3), which is 1000 operations if n=10
# So, it doesn't matter if its O(n^k), we would still
# refer it as O(n^2)

# O(n^2) is lot less efficient when thought interms of time complexity.
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k) 

print_items(10)