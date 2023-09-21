def is_palindrome_iterative(word):
    if not word:
        return False
    word_to_list = [letter for letter in word]
    reverse = word_to_list.reverse()
    reverse = "".join(reverse)
    return reverse == word
