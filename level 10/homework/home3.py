secretnumber = 42 
attempts = 0 
while True  :
    guess =  int (input ("enter number : "))
    attempts += 1 
if guess > secretnumber :
    print ("number is too high ")
elif guess < secretnumber : 
    print (" number is too low ")
else:
    print("congratulation ")

