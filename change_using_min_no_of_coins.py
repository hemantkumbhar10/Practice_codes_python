def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    for i in range(0,no_of_five+1):
        for j in range(0,no_of_one+1):
            if(((i*5)+(j*1))==rupees_to_make):
                five_needed=i
                one_needed=j
                break
            else:
                continue
    if(five_needed!=0 or one_needed!=0):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)
print(make_amount(100, 21, 5))



