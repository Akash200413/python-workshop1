balance=10000
amount=int(input("Enter a amount:"))
if(amount>balance):
    print("you have insufficient balance")
else:
    print("your amount has been debited")
    balance-=amount
    print(f"your new balance {balance}")

