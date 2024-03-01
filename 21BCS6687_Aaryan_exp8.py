nums = [1, 6, 9]
n = 12
count = 0

def getMax(sub, nums):
    if max(nums) <= sub:
        return max(nums)
    else:
        nums.remove(max(nums))
        return getMax(sub, nums)
    
digits = []
while count < n :
    if nums == []:
        break
    sub = n - count
    max_n = getMax(sub, nums)
    digits.append(max_n)
    count += max_n

print(sum(digits))