def find_duplicate(nums):
    if isinstance(nums, list) and len(nums) >= 2:
        set_nums = set()
        nums.sort()
        for num in nums:
            if isinstance(num, str) or num < 0:
                return False
            if num in set_nums:
                return num
            set_nums.add(num)
        return False
    else:
        return False


# test = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# #  test = [1,2,3,4,5]

# print(find_duplicate(test))
