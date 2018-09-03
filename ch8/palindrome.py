def palindrome(s):
    return s[::-1] == s


if __name__ == '__main__':
    print("palindrome({}) = {}".format("aba", palindrome("aba")))
    print("palindrome({}) = {}".format("abc", palindrome("abc")))
