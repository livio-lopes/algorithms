def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return (first_string, second_string, False)
    f_lower = first_string.lower()
    s_lower = second_string.lower()
    f_list = [letter for letter in f_lower]
    s_list = [letter for letter in s_lower]
    f_list = merge_sort(f_list)
    s_list = merge_sort(s_list)
    f_lower = "".join(f_list)
    s_lower = "".join(s_list)
    return (f_lower, s_lower, f_lower == s_lower)
