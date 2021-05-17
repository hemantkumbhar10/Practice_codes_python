def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill = 0
    if quantity_ordered > 0 and distance_in_kms > 0:
        for i in range(distance_in_kms+1):
            if i <= 3:
                x = 0
            elif i >3 and i <= 6:
                x += 3
            else:
                x += 6
        bill = x
    amount = ((food_type*quantity_ordered)+bill)
    return amount
V = 120
N = 150
print(calculate_bill_amount(N,2,9))

