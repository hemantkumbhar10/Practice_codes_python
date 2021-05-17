def merge_list(list1, list2):
    merged_data=""
    j = len(list1)-1
    for i in range(len(list1)):
        str1 = str2 = ''
        if list1[i]:
            str1 = list1[i]
        if list2[j] == None:
            pass
        else:
            str2 = list2[j]
        j -=1
        merged_data += str1+str2+' '

    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)