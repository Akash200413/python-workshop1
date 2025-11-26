balance=10000
while True:
    type=input("enter your choose Credit / Debit /stop : ")
    if(type=="stop"):
        break
    elif(type=="Credit"):
        credit_amount=int(input("enter your amount : "))
        balance=balance+credit_amount
        print(f"your new balance {balance}")
    elif(type=="Debit"):
        debit_amount=int(input("enter your amount : "))
        if(balance>debit_amount):
            balance=balance-debit_amount
            print(f"Amount debited your new balance {balance}")
        else:
            print("insufficent balance")
    else:
        print(f"balance:{balance}")