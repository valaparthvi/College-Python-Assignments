product = 1
# product = 0
for i in range(1, 10):
    product *= i

sum_square = 0
for i in range(10):
    i_sq = i**2
    sum_square += i_sq
sum_square += i_sq

nums = 0
for num in range(10):
    nums += num
    # num += num

print("product = %d, sum_square = %d, nums = %d" % (product, sum_square, nums))

'''
BEFORE
Output:  python3 chapter4_2_logicerror.py
product = 0, sum_square = 81, nums = 0

AFTER
Output: python3 chapter4_2_logicerror.py
product = 362880, sum_square = 366, nums = 45
'''
