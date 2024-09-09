my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list[1] = 15
print(my_list)

my_list.extend([50,60,70])
print(my_list)

my_list.pop(-1)
print(my_list)

my_list.sort()

find_index = my_list.index(30)
print("The index of 30 is:", find_index)
