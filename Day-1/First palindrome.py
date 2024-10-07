def first_palindromic_string(words):
    for word in words:
        if word == word[::-1]:  # Check if the word is a palindrome
            return word
    return ""  # Return an empty string if no palindrome is found

# Test with example input
words = ["abc", "car", "ada", "racecar", "cool"]
print(first_palindromic_string(words))  # Output: "ada"
