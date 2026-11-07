n = int (input ("enter number of products : "))
total = 0 
for i in range (n):
    price = float (input("enter products price : "))
    total += price
if  total > 200 :
    discount = total * 15
elif total >= 100 :
    discount = total * 10
else :
    discount = 0 

total_price = total + discount


