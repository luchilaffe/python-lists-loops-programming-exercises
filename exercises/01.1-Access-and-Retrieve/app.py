
my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

# 1. print the item here
print (my_list[2])
# 2. change the position were 'thursday' is to None
for i in range(len(my_list)):
    if (my_list[i] == "thursday"):
        my_list[i] = None
# 3. print that position now here
        print(my_list[i])