my_list = [1,2,3,4,5]

def square_of_list(list):
    new_list = []
    for i in list:
        new_list.append(i**2)
    return new_list
    #print("Square of %d = %d" %(i,(i**2)))

squared_list = square_of_list(my_list)
print (squared_list)

for i in squared_list:
    print (i)