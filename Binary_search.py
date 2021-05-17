import random
def find_it(num,element_list):
    low = 0
    high = len(element_list)-1
    p = 1
    while(low <= high):
        mid = (low + high)//2
        if(element_list[mid] == num):
            print(element_list[mid])
            break
        else:
            if(element_list[mid] < num):
                low = mid +1
            else:
                high = mid -1
        p +=1
    print(p)
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements
def play(n):
    ls = initialize_list_of_elements(n)
    ran_num = random.choice(ls)
    print(ls)
    print(ran_num)
    print(find_it(ran_num, ls))
play(400)
