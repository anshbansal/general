import sys
def p():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        length = int(sys.stdin.readline())
        nums = dict()

        for num in sys.stdin.readline().split(' '):
            num = int(num)
            if nums.has_key(num):
                nums[num] += 1
            else:
                nums[num] = 1

        max_value = -1
        max_key = -1
        for key in nums:
            if (nums[key] == max_value and key < max_key):
                max_key = key
            elif nums[key] > max_value:
                max_key = key
                max_value = nums[key]

        print max_key, nums[max_key]


p()
