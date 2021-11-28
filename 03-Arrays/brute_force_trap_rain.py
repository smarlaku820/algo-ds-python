def trap_water(nums):
    """
    Use-Cases:
    trap_water([1,0,1])
    1
    trap_water([0,1,2])
    0
    trap_water([0,1,0,2,1,0,3,1,0,1,2])
    8
    trap_water([4,2,0,3,2,5])
    9
    trap_water([0,1,0,2,1,0,1,3,2,1,2,1])
    6
    """
    TotalArea=0
    MaxLeft=0
    MaxRight=0
    for i in range(len(nums)):
        try:
            MaxLeft=max(nums[:i])
        except ValueError:
            MaxLeft=0
        try:
            MaxRight=max(nums[i:][1:])
        except ValueError:
            MaxRight=0
        # print("max to the left is "+str(MaxLeft))
        # print("max to the right is "+str(MaxRight))
        area = min(MaxLeft, MaxRight) - nums[i]
        if area<0:
            area=0
        # print("Area contribute is "+str(area))
        TotalArea += area
    return TotalArea