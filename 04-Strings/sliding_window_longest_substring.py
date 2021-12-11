def longest_substring(s):
    longest=0
    hash_map={}
    left=0
    right=0
    if len(s) <= 1:
        return len(s)
    while right <= len(s)-1:
        if s[right] not in hash_map:
            hash_map[s[right]]=right
            if right-left+1 > longest:
                longest=right-left+1
            right+=1
        else:
            if hash_map[s[right]] >= left:
                left=hash_map[s[right]]+1
            hash_map[s[right]]=right
            if right-left+1 > longest:
                longest=right-left+1
            right+=1
    return longest