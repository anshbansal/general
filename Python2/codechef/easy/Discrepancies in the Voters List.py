import sys
from itertools import islice

def p():
    num1, num2, num3 = map(int, next(sys.stdin).split())

    nums1 = set([int(next(sys.stdin)) for i in xrange(num1)])
    nums2 = set([int(next(sys.stdin)) for i in xrange(num2)])
    nums3 = set([int(next(sys.stdin)) for i in xrange(num3)])

    all_nums = set()
    all_nums.update(nums1)
    all_nums.update(nums2)
    all_nums.update(nums3)
    
    ans = []
    for i in all_nums:
        count = 0
        if i in nums1:
            count += 1
        if i in nums2:
            count += 1
        if count > 1:
            ans.append(i)
            continue
        if i in nums3:
            count += 1
        if count > 1:
            ans.append(i)

    ans.sort()
    print len(ans)
    for i in ans:
        print i


p()
