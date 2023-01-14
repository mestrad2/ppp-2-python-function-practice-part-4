def mult_list(numList):
    if len(numList) == 0:
        return 0
    
    product = numList[0]

    if len(numList) > 1:
        for i in numList[1:]:
            product = product * i
    
    return product


print(mult_list([10, 20, 30]))
print(mult_list([1, 2, 3, 4, 5]))
print(mult_list([]))
print(mult_list([42]))
