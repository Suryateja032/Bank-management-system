class Bank:
    def __init__(self,company) -> None:
        self.company=company
        self.d={}
    def addbankaccount(self,object):
        self.d[object.username]=[]
        self.d[object.username].append(object.username)
        self.d[object.username].append(object.password)
        self.d[object.username].append(object.bal)
        self.d[object.username].append(object.tran)
    def checkbalance(self,username):
        print("your balance is:",self.d[username][2])   
    def depositmoney(self,username,amount):
        self.d[username][2] +=amount
        print("deposited successful")
        print("current balance:",self.d[username][2])
        value="Deposited "+str(amount)+" curr balance is "+ str(self.d[username][2])
        self.d[username][3].append(value)
    def withdraw(self,username,amount):
        if amount<=self.d[username][2]:
           self.d[username][2] -=amount
           print("withdraw successful")
           print("current balance:",self.d[username][2])
           value="withdrawn "+str(amount)+" curr balance is "+ str(self.d[username][2])
           self.d[username][3].append(value)
        else:
            print("insufficient balance")
    def showtransaction(self,username):
        for i in self.d[username][3]:
            print(i)
    def sendmoney(self,username,reciever):
       amount=int(input("enter the amount"))
       while amount>self.d[username][2]:
           print("Low balance")
           amount=int(input("enter the amount"))
       else:
             self.d[username][2]>=amount
             self.d[username][2]-=amount
             self.d[reciever][2]+=amount
             value=("i haven sent")+str(amount)+"rs to"+ reciever + " curr balance is "+ str(self.d[username][2])
             self.d[username][3].append(value)
             value=("i haven recieved")+str(amount)+"from"+ username + " curr balance is "+ str(self.d[reciever][2])
             self.d[reciever][3].append(value)
             print("Transaction successfull")
class Account:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bal=0
        self.tran=[]
#homepage
b=Bank("Gpay")
option=0
while option!=3:
    print("")
    print("1.Create an account")
    print("2.Login in")
    print("3.Exit")
    
    print("")
    i=int(input("choose an option:"))
    if i==1:
        
        print("welcome to gpay:")
        username=input("Enter your username:")
        password=input("Set your password")
        if username in b.d:
            print("Account Already exists")
            continue
        username=Account(username,password)
        b.addbankaccount(username)
        print("Congrats, your account has been created ")
    elif i==2:
        print()
        print("")
        u=input("Enter your username: " )
        p=input("Enter your password: ")
        if u not in b.d:
                print("Account does not exits ")
                
                continue
        else:
            i=1
            while i<4:
                if p==b.d[u][1]:
                      print()
                      print("")
                      q=0
                      while( q<7):
                            print("welcome ,",b.d[u][0])
                            print("1.Check balance")
                            print("2.Deposit money")
                            print("3.Withdraw money")
                            print("4.Send Money")
                            print("5.Show transaction")
                            print("6.log out")
                            print()
                            i=int(input("Choose your option"))
                            if i==1:
                                b.checkbalance(u)
                            elif i==2:
                                m=int(input("Enter the deposit amount"))
                                b.depositmoney(u,m)
                            elif i==3:
                                m=int(input("Enter the withdraw amount"))
                                b.withdraw(u,m)
                            elif i==4:
                                r=input("Enter reciever username: ")
                                while r not in b.d:
                                    print("Enter Valid reciever name")
                                    r=input("Re enter")
                                else:
                                    b.sendmoney(u,r)
                                
                            elif i==5:
                                b.showtransaction(u)
                            elif i==6:
                                break
                            else:
                                print("invalid option")
                            print("")
                      break
                else:
                    print("wrong password",3-i,"attempt left")
                    p=input("Enter your password: ")
                i+=1         
    elif i==3:
        exit()
        
    else:
        print("Invalid option")
