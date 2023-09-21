# define default params low_index = right index and high_index = left index
def is_palindrome_recursive(word, low_index=-1, high_index=0):
    # business rule
    if word == "":
        return False

    # ensure that the word in the input is always upper case
    word = word.upper()
    """ from now on it is the logic of the prompt used in chatGPT 3.5
        'complete in python def is_palindrome_recursive(word, low_index,
        high_index):' """

    """ base case """
    # compare low_index and high_index
    if low_index >= high_index:
        return True
    # compare letter right and letter right
    if word[low_index] != word[high_index]:
        return False
    # state change and called recursion
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# test = "abC"
# print(is_palindrome_recursive(test))
# print(is_palindrome_recursive(test := "aba"))
