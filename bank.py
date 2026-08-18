import json


with open("accounts.json", "r") as file:
   accounts = json.load(file)

accounts = {int(key): value for key, value in accounts.items()}

def save_accounts():
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)


while True:
 print('''
    ========== AR BANK SYSTEM ==========
         1. Login
         2. Create New Account
         3. Exit
    ''')
 main_choice=int(input("Enter Your Choice : "))
 if main_choice == 1:           

  n = int(input("Enter Your Account Number :"))

  if n not in accounts:
    print("Account Number Not Found")

  else:
    account = accounts[n]

    
    p = input("Enter Your Pin :")
    if p == account["pin"]:
     print("Login Succesfull please wait")    
     while True:
        print("="*44)
        print("Hello",                 account["name"])
        print('''============== AR BANK SYSTEM ==============
        1. Check Balance
        2. Deposit Money
        3. Withdraw Money
        4. Account Details
        5. Show Transactions
        6. Exit
        7. Mini Statment 
        ''')
        choice = int(input("Enter Your Choice 1-7 :"))

        #  1. Check Balance
        if choice==1:
            print("="*44)

            print("Your Current Available Ammount Is : " , account["balance"])


        # 2. Deposit Money
        elif choice==2:
            amt = int(input("Enter Ammount To  Add"))  
            if amt>0:
                account["balance"] = account["balance"] + amt
                account["transactions"].append("Deposited Rs. "+ str(amt))
                save_accounts()
            else:
                print("Enter Correct Ammount")


        # 3. Withdraw Money
        elif choice==3:
            w_amt= int(input("Enter Ammount To Withdrawl :"))
            if w_amt > account["balance"]:
                print("insufficient Balance ")
            elif w_amt <=0:
                print("Enter Correct Ammount ")
            else:
                account["balance"] = account["balance"] - w_amt  
                account["transactions"].append("Withdrawn Rs. " + str(w_amt))
                save_accounts()
                print ( w_amt," Withdraw Succesfully")
                print("="*40)
                print("Current Available Balance = " , account["balance"])

        # 4. Account Details
        elif choice==4:
            print("-"*43)

            print("======== Your Account Details Are =======")


            print("Name :", account["name"])
            print("Account Number :", n)
            print("Account Type :", account["type"])
            print("Address :", account["address"])

            print("=========Thank You=========")


        # 5. Show Transactions
        elif choice==5:
            print("-"*43)

            print("========Transaction History========")
            # print(account["transactions"])
            for transaction in account["transactions"]:
                print(transaction)
            print("-"*43)


        # 6. Exit
        elif choice==6:
            break

        # 7. mini Statment 
        elif choice==7:
            print("-"*43)
            print('Account Holder :' , account["name"])
            print('Account Number :' , n)

            print('======Mini Statment======')
            for transaction in account["transactions"][-5:]:
             print(transaction)
            print("-"*43)


        else:
            print('Enter a valid Choice ')
    else:
        print("Invalid PIN")   
        print("Enter Correct PIN")   

# ---------------------------------------------------------------------------------------------------------------------------------------


 elif main_choice==2:
     name = input("Enter Your Name : ")
     if not name.strip():
      print("Name cannot be empty")
      continue
     pin = input("Create Your PIN : ")
     if len(pin) != 4 or not pin.isdigit():
        print("PIN Needs To Be Exectly 4 Digits")
        continue
     confirm_pin = input("Enter Pin Again")
     if pin != confirm_pin:
        print("PIN Does Not Match")
        continue
     
     balance = int(input("Enter Initial Deposit : "))
     if balance <= 0:
      print("Ammount Must Be Atleast More Than 0")
      continue
     account_type = input("Enter Account Type : ")
     address = input("Enter Your Address : ")

     new_account_no = max(accounts) + 1

     accounts[new_account_no] = {
        "name": name,
        "pin": pin,
        "balance": balance,
        "type": account_type,
        "address": address,
        "transactions": []

}
     save_accounts()
     print('Account Created Succesfully')
     print("Your New Account Number Is " , new_account_no)


# ---------------------------------------------------------------------------------------------------------------------------------------

 elif main_choice==3:
    break
# ---------------------------------------------------------------------------------------------------------------------------------------
 
 else :
    print("Enter A Valid Choice")




            










