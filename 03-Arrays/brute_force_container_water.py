def greatest_container(nums):
    """
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
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            area=min(nums[i],nums[j])*(j-i)
            if area > maxArea:
                maxArea=area
    return maxArea