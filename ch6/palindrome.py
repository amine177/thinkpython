def palindrome(s):
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])


if __name__ == '__main__':
    print("palindrome({}) = {}".format("iamai", palindrome("iamai")))
    print("palindrome({}) = {}".format("iama", palindrome("iama")))
