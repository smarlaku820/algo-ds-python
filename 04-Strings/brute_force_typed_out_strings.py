def typed_out(s,t):
    """
    from brute_force_typed_out_strings import typed_out
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

    where a is the size of string 's' and b is the size of string 'b'
    Time Complexity: O(a+b)
    Space Complexity: O(a+b)
    """
    lisa=[]
    lisb=[]
    for strng in s,t:
        for char in strng:
            if char != '#':
                if strng is s:
                    lisa.append(char)
                else:
                    lisb.append(char)
            else:
                if strng is s:
                    if len(lisa) > 0:
                        lisa.pop()
                else:
                    if len(lisb) > 0:
                        lisb.pop()
    return ''.join(lisa) == ''.join(lisb)