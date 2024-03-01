nums = list(map(int, input('').split(' ')))
n = int(input(''))
count = 0

def getMax(sub, nums):
    if nums == []:
        return None
    if max(nums) <= sub:
        return max(nums)
    else:
        nums.remove(max(nums))
        return getMax(sub, nums)
    
digits = []
while count < n :
    sub = n - count
    if nums == [] or (len(nums) == 1 and sub < nums[0]):
        break

    max_n = getMax(sub, nums)
    if max_n is None:
        break
    digits.append(max_n)
    count += max_n

print(sum(digits))