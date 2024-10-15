def isPalindrome(word : str) -> bool:
        if not word: # if len(word) == 0:
            return True
        elif len(word) == 1:
            return True
        elif len(word) <= 3:
            return word[0] == word [-1]
        else:
            i = 0
            j = len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False

                i += 1
                j -+ 1
            # end of while
            return True
# end of isPalindrome()