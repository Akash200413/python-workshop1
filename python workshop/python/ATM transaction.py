Balance=10000

input_user=input('Enter Credit or Debit:')
if(input_user=="credit"):
    amount=int(input("enter amount:"))
    Balance=amount+Balance
    print("Balance=",Balance)
elif input_user=="debit":
    amount=int(input("enter amount"))
    if amount<Balance:
        print("successfully withdrawn amount")
        print("Remaining =",(Balance-amount))
    else:
        print("Insufficient balance amount")
        print("Deposite Amount")
