# Give a String and Reverse it by best Optimised Technique

def reversing_string(word):
    s = list(word)
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    result =  "".join(s)
    return result
word = input("Enter a Word : ")
print(reversing_string(word))