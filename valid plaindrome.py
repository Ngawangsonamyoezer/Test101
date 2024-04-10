def is_valid_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

input_string = "A man, a plan, a canal: Panama"
print(is_valid_palindrome(input_string)) 
