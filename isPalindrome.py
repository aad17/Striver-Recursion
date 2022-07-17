# Check if String is palindrome or not

mystr = 'MADAM'

def isPalindrome(mstr, l, r):
    if l >= r:
        return True
    
    if mstr[l] != mstr[r]:
        return False
    
    return isPalindrome(mstr, l+1, r-1)

print(isPalindrome(mystr, 0, len(mystr)-1))