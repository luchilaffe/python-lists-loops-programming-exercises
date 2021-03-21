list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(the_list):
    oddList = []
    evenList = [] 
    for i in the_list:
        if i % 2 == 0:
            evenList.append(i)
        elif i % 2 != 0:
            oddList.append(i)
        else:
            print("Something is wrong")
    new_list = []
    new_list.append(oddList)
    new_list.append(evenList)
    return new_list


print(merge_two_list(list_of_numbers))

