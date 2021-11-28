def two_sum(nums, target):
    """
    Optimal Solution is obtained by using a HashMap
    Test Case 1:-
    nums=[1, 3, 7, 9, 2], target=11
    two_sum([1,3,7,9,2],11)
    Ans: [3,4]

    Test Case 2:-
    nums=[], target=11
    two_sum([],11)
    Ans: None

    Test Case 3:-
    nums=[5], target=11
    two_sum([5], 11)
    Ans: None
    """
    nums_hashmap = {}
    for i in range(len(nums)):
        numberToFind = target - nums[i]
        if nums[i] not in nums_hashmap:
            nums_hashmap[numberToFind]=i
        else:
            return [nums_hashmap[nums[i]],i]
    return None