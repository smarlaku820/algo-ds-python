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
    area=0
    MaxLeft=0
    MaxRight=0
    i=0
    j=len(nums)-1
    while i < j:
        if nums[i] <= nums[j]:
            # calculate the water
            if nums[i] < MaxLeft:
                area=MaxLeft-nums[i]
                i+=1
            # update the max left
            else:
                MaxLeft=nums[i]
                i+=1
        else:
            # update the max right
            if nums[j] > MaxRight:
                MaxRight=nums[j]
                j-=1
            # calculate the water
            else:
                area=MaxRight-nums[j]
                j-=1
        TotalArea += area
        area=0
    return TotalArea