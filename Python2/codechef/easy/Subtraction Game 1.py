import sys

def p():
    tests = int(next(sys.stdin))
    for i in xrange(tests):
        num = int(next(sys.stdin))
        nums = [int(i) for i in set(next(sys.stdin).split())]
        #If numbers are not in sorted order then
        #the next commented line has to be used instead of previous one        
        #nums = sorted([int(i) for i in set(next(sys.stdin).split())])
        min_index = 0
        max_index = len(nums) - 1
        while True:
            if nums[max_index] == nums[min_index]:
                print nums[0]
                break
            else:
                nums[max_index] %= nums[min_index]
                if nums[max_index] == 0:
                    nums[max_index] += nums[min_index]

                min_index = max_index
                max_index -= 1

p()
