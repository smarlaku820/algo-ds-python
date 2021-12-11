def longest_substring(s):
    """
    longest_substring("abccabb")
    3
    longest_substring("cccccccc") 
    1
    longest_substring("")
    0
    longest_substring("abcbda")
    4
    """ 
    t=[]
    l=[]
    for i in range(len(s)):
        # print("i={};s[i]={}".format(i,s[i]))
        t.append(s[i])
        for j in range(i+1,len(s)):
            # print("j={};s[j]={}".format(j,s[j]))
            if s[j] not in t:
                t.append(s[j])
            else:
                # print(''.join(t))
                l.append(len(''.join(t)))
                t=[]
                break;
        if len(t) != 0:
            # print(''.join(t))
            l.append(len(''.join(t)))
            t=[]
    if len(l) == 0:
        return 0
    else:
        return max(l)
