class ATM :
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(f"current balance : {self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit : "))
        if amount > 0 :
            self.balance += amount
            print(f"{amount} deposited successfully")
        else :
            print("invalid amount")

    def withdraw(self) :
        amount = float(input("enter amount to withdraw : "))
        if amount <= 0 :
            print("invalid amount!")
        elif amount >= self.balance :
            print("insufficent balance")
        else :
            self.balance -= amount
            print(f"{amount} withdrawn successfully")

    def menu(self) :
        while True :
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("enter your choice (1-4) : ")
            if choice == "1" :
                    self.check_balance()
            
            elif choice == "2":
                    self.deposit()
            
            elif choice == "3":
                    self.withdraw()
            
            elif choice == "4":
                    print("thank you for using atm")
                    break
            else:
                 print("invalid choice, try again")

#Main program

print("welcome to atm") 

pin = "1234"
for attempt in range(3):
     user_pin = input("enter 4-digit PIN : ")

     if user_pin == pin:
          print("login successfull")

          balance = float(input("enter initial balance : "))
          atm = ATM(balance)

          atm.menu()
          break 

     else:
          print("incorrect PIN")

else :
     print("account banned ! \n too many attemts")      

        
        