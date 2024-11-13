def pow1(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * pow1(base, exponent-1)

def pow2(base, exponent, answer=1):
    if exponent == 0:
        return answer
    else:
        return pow2(base, exponent-1, answer * base)

def is_pali(word):
    # Two pointer recursion for fun
    def helper(word, left, right):
        if left > right:
            return True
        elif word[left] != word [right]:
            return False
        else:
            return helper(word, left + 1, right - 1)
        # end of helper
    if not word:
        return True
    elif len(word) <= 3:
        return word[0] == word[-1]
    else:
        return helper(word, 0, len(word)-1)