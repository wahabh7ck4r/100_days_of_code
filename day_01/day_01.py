# Given an arry of integers nums and an integer target, return the indices of the two numbers such that they add up to target.


# we can solve this problem by many ways but the most comman way is this:

num = [2 , 3, 4, 5, 22, 4] 

# target
target = 6
req_indx = ()
for i in  range(len(num)):
    for j in range(i+1 , len(num)):
        if num[i] + num[j] == target:
            req_indx = (num.index(num[i]), num.index(num[j]))
            break


print(req_indx)

print("------------------------------------------------------------/n")
# from the above way you will get the index of first match up value, but a little fix make it more efficient instead of using "index" we can print the time where we will get the value so let's do it again.


for i in range(len(num)):
    for j in range(i+ 1, len(num)): # so i add +1 beacuse i don't want the same index on the like if i is 0 j must be 1
        if num[i] + num[j] == target:
            print(i, j)  #it will print all indexs where sum is equal to target.


# now this one is more good but there is still probelm we can make it much more better like now it is taking O(n*2) but we can make this O(n)

print("---------------------------------------------------/n")
# its a dictionary at strat its empty then we start adding value using while loop
seen = {}
x = 0
checker = 0
while x < len(num):
    checker = target - num[x]
    if checker in seen:
        print(seen[checker], x)
    seen[num[x]] = x
    x += 1

# task for all of you " use for loop or enumerate funtion to it more clean and more space efficient als try to reduce more time complexity big O"
print("day one finshed........ 4/3/2026")