

  def custom_key(num):
    # Check if the number is zero, in which case return a high value (e.g., 1000)
    if num == 0:
      return 1000
    while num % 10 == 0 and num != 0:
      num //= 10
    return num

  sorted_nums = sorted(nums, key=custom_key)
  smallest_int = int("".join(str(num) for num in sorted_nums))
  return smallest_int

# Example usage
nums = [170, 120, 2]
smallest_num = smallest_number(nums)
print(f"Original list: {nums}")
print(f"Smallest number: {smallest_num}")
