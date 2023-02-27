


def is_palindrome(word):
    # Stop condition
    if len(word) < 2:
        return True
    
    # Compare first and last characters
    if word[0] == word[-1]:
        # Recursively check the rest of the word
        return is_palindrome(word[1:-1])
    
    # If first and last characters are different, it's not a palindrome
    return False
