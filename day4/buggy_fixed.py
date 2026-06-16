def avg(nums):
    if len(nums) == 0:
        return "Error: cannot average an empty list"
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

def reverse_string(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):   
        result += s[i]
    return result

print(avg([10, 20, 30]))  
print(avg([]))                    
print(reverse_string("hello"))