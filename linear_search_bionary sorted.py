#DSA-Tryout

import random

def find_it(num,element_list):
    #Remove pass and copy the solution earlier written for this function here
    #Modify it, if required
    for i in element_list:
        if num == i:
            print(i)
            print(element_list.index(i) + 1, ' guesses made')

def initialize_list_of_elements(n):
    #Modify the code to initialize the list of elements in ascending order
    #Try with descending order also
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    mid=n//2
    for j in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1
    list_of_elements.sort(reverse= True)
    return list_of_elements

def play(n):
    #Remove pass and copy the solution earlier written for this function her
    lst = initialize_list_of_elements(n)
    num = random.choice(lst)
    print(lst)
    print(num)
    return find_it(num, lst)

#Pass different values to play() and observe the output
play(400)