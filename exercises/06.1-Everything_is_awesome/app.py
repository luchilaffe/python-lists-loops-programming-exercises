my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def my_function(numbers):
    new_list = []
    for numb in numbers:
    #The magic go here:
        if numb == 1:
            new_list.append(numb)
        elif numb == 0:
            new_list.append("Yahoo")
        else:
            new_list.append("Something is wrong!")
        
    return new_list
print(my_function(my_list))


