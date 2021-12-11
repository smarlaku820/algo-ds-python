def balanced_params(s):
    """
    balanced_params("()[{}()]")
    True
    balanced_params("](){}")
    False
    balanced_params("[)(]")
    False
    balanced_params("[(])")
    False
    """
    stack=[]
    hash_map={
        "[":"]",
        "(":")",
        "{":"}"
    }
    if len(s) <= 1:
        return False
    for _ in s:
        if _ in '[({':
            stack.append(_)
        else:
            if len(stack) == 0:
                return False
            if hash_map[stack.pop()] != _:
                return False
    if len(stack) == 0:
        return True
    else:
        return False