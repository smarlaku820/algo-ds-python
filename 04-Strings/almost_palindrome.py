def check_palindrome(s):
    s=s.lower()
    s=''.join([char for char in s if char.isalnum()])
    l=list(s)
    l.reverse()
    r=''.join(l)
    for i in range(len(s)):
        if s[i] != r[i]:
            return False
    return True