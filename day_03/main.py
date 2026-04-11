nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]

missing_num = []

for i in range(len(nums)):
    if i+1 == nums[i]:
        continue
    else:
        missing_num.append(1+i)
        break

if len(missing_num) > 0:
    print(f"the messing number are {missing_num}")
else:
    print("no missing number found")

# This is the first way to solve this problem with O(n) but you can also solve that kind of problem using math to make it more effective think like what if there are many missing value and you have to find also this so then what will you do.

# you task : make a program to solve this problem for multiple missing value and order is random.
