s = 'newteststring'

# let's store value in dic to check the char is repeating or not 
check = {

}

for i in s:
    if i in check:
        check[i] += 1  
    else:
        check[i] = 1

# print(check) 

for k, v in check.items():
    if v == 1:
        print(f"The first non repeating chr in the list is, {k}")
        break
else:
    print("no non-repeating chr fond in the list..")


# # this is the first way yo can solve proble that i mention bt the more good way is th below like pro or it's yor task : try to the same thing"    if i in check:
#         check[i] += 1  
#     else:
#         check[i] = 1"   with sing get() methond in python.