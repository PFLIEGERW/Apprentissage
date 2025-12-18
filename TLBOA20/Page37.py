numbers_list = [9,8,7,5,6,2,1,12,14,0,13]
lowest = numbers_list[0]
for count in range(len(numbers_list)):
    if numbers_list[count] < lowest:
        lowest = numbers_list[count]
print("The lowest number in the list is ", lowest)

#sinon on a numbers_list.sort(), au pif...