my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
my_sample_list[1] = "Steven"
my_sample_list[len(my_sample_list) - 1] = "Pepe"
my_sample_list[0] = my_sample_list[2] + my_sample_list[4]
my_new_list = list(reversed(my_sample_list))
for i in range(len(my_new_list)):
    print(my_new_list[i])