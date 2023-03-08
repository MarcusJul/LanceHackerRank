def bonAppetit(bill, k, b):
    # Write your code here
    sb = sum(bill)
    kick = bill.pop(k)
    
    anna = int((sb-kick)/2)
    # print(anna, b)
    if b==anna:
        print("Bon Appetit")
    else:
        print("%d"%(int(b-anna))) 