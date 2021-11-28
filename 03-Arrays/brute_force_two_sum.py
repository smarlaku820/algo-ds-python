def two_sum(nums, target):
    """
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
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None