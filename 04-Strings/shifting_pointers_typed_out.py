def typed_out(s,t):
    """
    from shifting_pointers_typed_out import typed_out
    typed_out("ab#z", "az#z")
    True
    typed_out("abc#d","acc#c")
    False
    typed_out("x#y#z#","a#") - both will return the empty string
    True
    typed_out("a###b", "b")
    True
    typed_out("Ab#z", "az#z") "Az" != "az"
    False

    Time Complexity: O(n)
    Space Complexity: O(n)

    Doesn't work.
    """
    i=len(s)-1
    j=len(t)-1
    while i>=0 or j>=0:
        if s[i]=='#' or t[j]=='#':
            if s[i] == '#':
                back_count=2
                while back_count > 0:
                    i-=1
                    back_count-=1
                    if s[i] == '#':
                        i-=1
                        back_count+=2
            if t[j] == '#':
                back_count=2
                while back_count > 0:
                    j-=1
                    back_count-=1
                    if t[j] == '#':
                        j-=1
                        back_count+=2
        else:
            if s[i] != t[j]:
                return False
            else:
                i-=1
                j-=1
    return True