#lex_auth_0127667370895278083332

def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list
    ls = []
    for i in range(len(num_list)):
        if num_list[start_index] < num_list[i]:
            ls.append(num_list[i])

    mn = min(ls)
    for j in range(len(num_list)):
        if mn == num_list[j]:
            return j


#Pass different values to the function and test your program
num_list=[10,2,100,67]
start_index=
print("Index of the next minimum element is", find_next_min(num_list,start_index))
print(num_list)
