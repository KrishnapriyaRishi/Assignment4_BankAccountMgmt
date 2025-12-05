
# Bank Account Management
# --------------------------------

# Write a python program to create a class BankAccount that supports the following : 

# Create an account with an initial balance
# Depositing money
# Withdrawing money (only if enough balance)
# Displaying the account balance.

# ----------------------------------------------------------------------------------------


class BankAccount:

	def __init__(self,acc_name,type,initial_deposit):
		self.acc_name = acc_name
		self.type = type
		self.acc_balance = initial_deposit
		# Calling create_Account() method
		self.create_Account()



	# Method to create an account with initial deposit of atleast Rs.5000
	def create_Account(self):
		print(f"{self.type} Account created for {self.acc_name} with an account balance Rs.{self.acc_balance}")
		self.transaction_Options(self.acc_name,self.acc_balance)



	# Method to display different services bank offers.
	def transaction_Options(self,acc_name,balance):
		bt_obj = Bank_Transactions(acc_name,balance)
		
		while True:
			print("---------Transaction Options--------\n")
			print(" 1.Deposit \n 2.Withdraw \n 3.Balance Enquiry\n 4.Transaction Details\n 5.Exit")
			choice = int(input("Enter your choice : "))
			
			# Based on user selection, they can deposit,withdraw,balance show and transaction history 
			if choice ==1:
				deposit_Amt = int(input("Enter the amount to deposit : "))
				bt_obj.deposit_Amount(deposit_Amt)

			elif choice == 2:
				withdraw_Amt = int(input("Enter the amount to withdraw : "))
				bt_obj.withdraw_Amount(withdraw_Amt)

			elif choice == 3:
				bt_obj.display_BalanceAmount()

			elif choice == 4:
				bt_obj.transaction_history_display()
			
			elif choice == 5:
				print("Exited successfully.")
				break


# -------------------------------------------------------------------------------------------



class Bank_Transactions(BankAccount):

	def __init__(self,name,balance):
		self.acc_name = name
		self.acc_balance = balance
		self.transactionDetails = list()
		self.transactionStatus = True
		self.transactionType = "Deposit"
		self.transaction_history_update(self.acc_name,self.transactionType,self.acc_balance,self.transactionStatus)


	# Method to deposit amount.
	def deposit_Amount(self,amount):
		self.transactionType = "Deposit"
		self.acc_balance += amount
		print(f"{self.acc_name} made a deposit of Rs.{amount}.\n")
		self.transactionStatus = True
		self.transaction_history_update(self.acc_name,self.transactionType,amount,self.transactionStatus)
		return self.acc_balance


	# Method to withdraw amount 
	def withdraw_Amount(self,withdraw_Amt):
		self.transactionType = "Withdraw"

		if self.acc_balance <= 2000:

			self.transactionStatus=False
			print("Sorry , You can't withdraw money now.Minimum balance required is Rs.2000\n")
			self.transaction_history_update(self.acc_name,self.transactionType,withdraw_Amt,self.transactionStatus)

		elif self.acc_balance > 2000:

			if (self.acc_balance - withdraw_Amt) >= 2000:
				
				self.acc_balance -= withdraw_Amt
				self.transactionStatus= True
				print(f"{self.acc_name} made a withdraw of Rs.{withdraw_Amt}.\n")
				self.transaction_history_update(self.acc_name,self.transactionType,withdraw_Amt,self.transactionStatus)
				return self.acc_balance
			
			else:
				self.transactionStatus=False
				print("Sorry , You can't withdraw money now.Minimum balance required is Rs.2000\n")
				self.transaction_history_update(self.acc_name,self.transactionType,withdraw_Amt,self.transactionStatus)

				

	# Method to add each transaction information
	def transaction_history_update(self,name,type,amount,status):
		self.valid = "Success" if status==True else "Failed"
		self.transactionDetails.append(f"{name} made a {type} - Rs.{amount} -- {self.valid}")


			
	# Method to display transaction history
	def transaction_history_display(self):
		for i in self.transactionDetails:
			print(i)

	
	# Method to display account balance.
	def display_BalanceAmount(self):
		print(f"{self.acc_name} has an account balance of Rs.{self.acc_balance}\n")
		
	

	
# ------------------------------------------------------------------------------------------
# main program

print("----------- Welcome to Banking -----------\n")

ch = input("Do you want to create an account?[y/n] : ").lower()

if ch == 'y':

	name = input("Enter your Name : ").capitalize()
	Acc_type = input("Enter your account type [Savings / Current]: ").capitalize()

	if Acc_type=='Savings' or Acc_type=='Current':

		print("You need to deposit atleast Rs.5000 to open an account.")
		initial_deposit = int(input("Enter the initial deposit amount :"))

		if initial_deposit >= 5000:
			bankAcc_obj = BankAccount(name,Acc_type,initial_deposit)
		else:
			print("Please enter an amount greater than or equal to 5000 rupees.")

	else:

		print(" Wrong Account type. We can't proceed further.")

# -------------------------------------------------------------------------------------------







		
		







