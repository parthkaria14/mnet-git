def avg(nums):
    total=0
    for n in nums:
        total+=n
    return total/len(nums) #crashes if empty list

def reverse_string (s):
    result=""
    for i in range(len(s)):
        result+=s[i] #just copies, no reversing
    return result

print(avg([10, 20, 30]))  
print(avg([]))                    
print(reverse_string("hello"))