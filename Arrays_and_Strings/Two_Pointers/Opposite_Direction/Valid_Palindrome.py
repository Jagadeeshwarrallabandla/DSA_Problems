# Given a String and Check if it is a Valid Palindrome or not
def valid_palindrome(word):

    
    n = len(word)
    left = 0
    right = n - 1
    while left < right and not word[left].isalnum():
        left += 1
    while left < right and not word[right].isalnum():
        right -= 1
        
        if (word[left] != word[right]):
            return "No Not a Palindrome ",False
        else:
            left += 1
            right -= 1
    return "Yes, It is a Paindrome ",True

k = input("Enter the word : ")
print(valid_palindrome(k))
