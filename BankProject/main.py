import json
import random
import string
from pathlib import Path


class Bank:
    database ="BankProject/data.json"
    data = []
    try:   
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("file not exist")
    except Exception as err:
         print(f"an error occured as {err}")
         
    @classmethod    
    def __Update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(cls.data))
            
    @classmethod
    def __accountgenrate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits , k = 3)
        spchar = random.choices("!@#$%^&*()_+{}:?" ,k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
    
    
             
         
    def CreateAccount(self):
        info ={
            "name":input("Enter your name:- "),
            "age": int(input("Enter your age:- ")),
            "email": input("Enter your email:- "),
            "pin": int(input("Enter your pin:- ")),
            "accountNo": Bank.__accountgenrate(),
            "balance": 0                
        }
        
        if info["age"] < 18 or len(str(info["pin"])) !=4:
            print("Sorry you cannot create your account")
        else:
            print("Account Created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down you account number")
            
            Bank.data.append(info)
            Bank.__Update()     
     
     
    def DepositMoney(self):
         accountNo = input("Enter your account number:- ")
         pin = int(input("Enter your pin:- "))
         
         userData = [i for i in Bank.data if i["accountNo"] == accountNo and i["pin"] == pin]
         
         if not userData:
             print("Invalid account number or pin")
             
         else:
             amount = int(input("Enter the amount you want to deposit:- "))
             if amount > 15000 or amount < 0:
                 print("sorry you cannot depos it more than 15000 or less than 0")
             else:
                 userData[0]["balance"] += amount
                 Bank.__Update()
                 print("Deposit successfully")
                

             
     
    def WithdrawingMoney(self):
          accountNo = input("Enter your account number:- ")
          pin = int(input("Enter your pin:- "))
                 
          userData = [i for i in Bank.data if i["accountNo"] == accountNo and i["pin"] == pin]
                 
          if not userData:
                print("Invalid account number or pin")
                     
          else:
             amount = int(input("Enter the amount you want to withdraw:- "))
             if amount > 10000 or amount < 0:
                 print("sorry you cannot withdraw it more than 10000 or less than 0")
             
             elif amount > userData[0]["balance"]:
                  print("insufficient balance")
                                  
             else:
                 userData[0]["balance"] -= amount
                 Bank.__Update()
                 print("Withdrawal successfully")
                         
                         
    def CheckDetails(self):
         accountNo = input("Enter your account number:- ")
         pin = int(input("Enter your pin:- "))
                
         userData = [i for i in Bank.data if i["accountNo"] == accountNo and i["pin"] == pin]
                
         if not userData:
               print("Invalid account number or pin")
                    
         else:
             print("Your account details are:- \n")
             for i in userData[0]:
                print(f"{i} : {userData[0][i]}")
                
                
    def UpdateDetails(self):
        accountNo = input("Enter your account number:- ")
        pin = int(input("Enter your pin:- "))
               
        userData = [i for i in Bank.data if i["accountNo"] == accountNo and i["pin"] == pin]
               
        if not userData:
              print("Invalid account number or pin")
                   
        else:
            print("You can Not change the age , account Number and balance")
            
            print("fill the details for changes or leave it empty if no change")
            
            newData ={
                "name": input("Enter your new name or press enter:- "),
                "email": input("Enter your new email or press enter:- "),
                "pin": input("Enter your new pin or press enter:- "),
            }
            if newData["name"] == "":
                newData["name"] = userData[0]["name"]
                
            if newData["email"] == "":
                newData["email"] = userData[0]["email"]
                
            if newData["pin"] == "":
                newData["pin"] = userData[0]["pin"]
                
            newData["age"] = userData[0]["age"]    
            newData["accountNo"] = userData[0]["accountNo"]    
            newData["balance"] = userData[0]["balance"] 
            
            if type(newData["pin"]) == str:
                newData["pin"] = int(newData["pin"])
            
            for i in newData:
               if newData[i] == userData[0][i]:
                   continue
               else:
                   userData[0][i] = newData[i]
                   
            Bank.__Update()
            print("Details updated successfully")                                    
                
                
    def DeleteAccount(self):
        accountNo = input("Enter your account number:- ")
        pin = int(input("Enter your pin:- "))
               
        userData = [i for i in Bank.data if i["accountNo"] == accountNo and i["pin"] == pin]
               
        if not userData:
              print("Invalid account number or pin")
        else:
            check = input("press y if you want to  Delete the account or press n for not Deleting:- ")
            if check == "n" or check == "N":
                print("Account not deleted")
            elif check == "y" or check == "Y":
                Bank.data.remove(userData[0])
                Bank.__Update()
                print("Account deleted successfully")
            else :
                print("Invalid input")
                
       
user = Bank()
print(Path("data.json").resolve())
print("press 1 for Creating an account")
print("press 2 for Depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for Updating the details")
print("press 6 for deleting your account")


check = int(input("tell you response:- "))

try:
    if check == 1:
         user.CreateAccount()
    elif check == 2:
         user.DepositMoney()
    elif check == 3:
         user.WithdrawingMoney()
    elif check == 4:
         user.CheckDetails()
    elif check == 5:
         user.UpdateDetails()
    elif check == 6:
         user.DeleteAccount()
    else:
        print("Invalid Input") 
except Exception as err :
    print(f"an error occured {err}")   