def swap(num_list, index1, index2):
    global no_of_swaps
    temp = num_list[index1]
    num_list[index1] = num_list[index2]
    num_list[index2]  = temp
    no_of_swaps +=1

def bubble_sort(num_list):
    global no_of_passes
    end_index = len(num_list)
    for index1 in range(0, end_index-1):
        swapped = False
        no_of_passes +=1
        for index2 in range(0, (end_index-index1-1)):
            if(num_list[index2] > num_list[index2 + 1]):
                swap(num_list, index2, index2 + 1)
                swapped = True
        if swapped == False:
            break

no_of_swaps = 0
no_of_passes = 0
lst = [45,14,12,45,16,58,15,78,89,87]
bubble_sort(lst)
print(lst)