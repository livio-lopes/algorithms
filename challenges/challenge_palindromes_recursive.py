def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    """Faça o código aqui."""
    # raise NotImplementedError


print(is_palindrome_recursive("ABA", -1, 0))
