# n^2 operations + n operations = n^2 + n operations
# We drop the non-dominant n operations
# So, the time complexity still stands at O(n^2)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)
      
print_items(10)