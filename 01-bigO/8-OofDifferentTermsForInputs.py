# O(a + b)
def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

# O(a*b)
def print_itm(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)