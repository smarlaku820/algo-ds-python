# We have n*n operations, therefore the complexity
# becomes O(n^2)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
      
print_items(10)