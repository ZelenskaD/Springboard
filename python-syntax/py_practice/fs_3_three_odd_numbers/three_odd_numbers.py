def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    for i in range(len(nums) - 2):
        # Calculate the sum of the current triplet
        current_sum = nums[i] + nums[i+1] + nums[i+2]
        # Check if the current sum is odd
        if current_sum % 2 != 0:
            return True  # Return True as soon as we find an odd sum
    return False  # Return False if no odd sum is found