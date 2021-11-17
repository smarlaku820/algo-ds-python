# In this case, 2*n  operations occured so, its O(2n)
# But O(2n) ~= O(n), we drop the constants.
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
      
print_items(10)