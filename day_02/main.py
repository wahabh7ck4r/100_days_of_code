# way 1. 

nums = [3,4,5,33,44,]

duplicate_checker = []
for i in range(len(nums)):
    if nums[i] in duplicate_checker:
        print(True)
        break
    else:
        duplicate_checker.append(nums[i])
    if i == len(nums) -1:
        print(False)

# way 2

# yo can solve this more good or clean way like sing elase with for loop
# to clear duplicate_checker so we can test it for way 2
duplicate_checker.clear()
for i in range(len(nums)):
    if nums[i] in duplicate_checker:
        print(True)
        break
    duplicate_checker.append(nums[i])
else:
    print(False)

# way 3 
# you can also do it more clear and clean like that 

duplicate_checker.clear()
for i in nums:
    if i in duplicate_checker:
        print(True)
        break
    duplicate_checker.append(i)
else:
    print(False)