def greatest_container(nums):
    """
    Optimal solution is obtained by implementing a technique called
    Shifting pointers.
    Test Cases:
    greatest_container([6,9,3,4,5,8])
    32
    greatest_container([7,1,2,3,9])
    28 
    greatest_container([1,1])
    1
    greatest_container([4,3,2,1,4])
    16
    greatest_container([1,2,1])
    2
    """
    maxArea=0
    i=0
    j=len(nums)-1
    while i < j:
        print("[{},{}]".format(i,j))
        area=min(nums[i], nums[j])*(j-i)
        if area > maxArea:
            maxArea=area
        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1
        print("maxArea={}".format(maxArea))
    return maxArea