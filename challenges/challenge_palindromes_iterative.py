def is_palindrome_iterative(word):
    if not word:
        return False
    mid = len(word) // 2
    if len(word) % 2 == 0:
        half_right_word = word[mid:]
    else:
        half_right_word = word[mid + 1 :]
    half_right_word = [letter for letter in half_right_word]
    half_right_word.reverse()
    half_right_word = "".join(half_right_word)
    return word[:mid] == half_right_word
