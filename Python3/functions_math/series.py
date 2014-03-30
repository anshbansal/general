__author__ = 'Aseem'


def fibonacci_inf(a, b):
    """Lazily generates Fibonacci numbers Infinitely"""
    while True:
        yield b
        a, b = b, a + b


def fibonacci(a, b, num):
    """Lazily generates Fibonacci numbers"""
    while b < num:
        yield b
        a, b = b, a + b


def sum_numbers(num):
    return (num * (num + 1)) // 2


def sum_squares(num):
    return (num * (num + 1) * (2 * num + 1)) // 6


def sum_multiples_upto(nums, upto):
    #TODO Needs to be refactored
    def sum_upto(num, upto):
        return num * sum_numbers(upto // num)

    if type(nums) is int:
        return sum_upto(nums, upto)
    if len(nums) > 2 or type(nums) is not tuple:
        return -1

    upto -= 1
    ans = sum_upto(nums[0], upto)
    ans += sum_upto(nums[1], upto)
    ans -= sum_upto(nums[0] * nums[1], upto)
    return int(ans)