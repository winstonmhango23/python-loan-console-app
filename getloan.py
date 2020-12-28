import  datetime
from datetime import date

print ('welcome to Quick Digital Loans banking services')
restart = ('Y')
pin_retry_chances = 3
balance = 10000.00
while pin_retry_chances >= 0:
	pin = int(input('Enter your 4 digit pin code:  '))
	# pin== (1994)
	if pin == (1994):
		#if user does not opt to quit
		while restart  not in ('n','N','NO','no'):
			print('Select the service options below: ')
			print('1 for BALANCE ENQUIRY')
			print('2 for LOAN REQUEST')
			print('3 for DEPOSITING')
			print('4 to CANCEL')
			option = int(input('WHAT SERVICE OPTION WOULD YOU LIKE ?  '))
			#bank balance enquiry
			if option == 1:
				print('Your Account Balance is $', balance)
				restart = input('Woul you like to go Back? ')
				if restart in ('n','NO','no','N'):
					print('THANKS FOR YOUR SERVICE')
					break
			#get a bank loan
			elif option == 2:
				#innitialising loan number to empty
				loan_number = ''
				print('What number of loan is this for You?')
				loan_number = int(input('Enter the number of loan in number...1,2,3,4...: '))
				
				loan_request = float(input('Enter loan amount $: ' ))

				#first time loan access
				if loan_request <= balance * 2 and loan_number == 1:
					print('You are only allowed to get X 2 your Account Balance')
					interest = 0.2
					
					#calculating loan payment date
					def loan_lastpay_day(loan_period):
						today = datetime.date.today()
						total_days = datetime.timedelta(int(loan_period))
						last_loan_day = today + total_days 
						return last_loan_day 

					balance = balance
					loan = loan_request
					Account_loan = loan
					# monthly= 30
					loan_period = input('Enter loan Period in number of days :' )
					number_of_days = loan_period
					loan_period = loan_lastpay_day(int(loan_period))
					pay_gross = (loan * interest)+ loan
					print('\nYou have requested loan for ',loan,'paid in',number_of_days,'days' )
					print('\nIf aproved You will pay $',pay_gross,'on',loan_period ,'at' ,interest,'interest')


					# balance = balance - loan_request
					# print('\nYour Account Balance  is Now $',balance)
					restart = input('Would you like to go back ? ')
					if restart in ('n','no','NO','N'):
						print('THANKS FOR YOUR SERVICE')

				#second loan access
				elif loan_request <= balance * 3 and loan_number == 2:
					print('You are only allowed to get X 3 your Account Balance')
					interest = 0.3
					#calculating loan payment date
					def loan_lastpay_day(loan_period):
						today = datetime.date.today()
						total_days = datetime.timedelta(int(loan_period))
						last_loan_day = today + total_days 
						return last_loan_day 
	
					
					balance = balance
					loan = loan_request
					Account_loan = loan
					# monthly= 30
					loan_period = input('Enter loan Period in number of days :' )
					number_of_days = loan_period
					loan_period = loan_lastpay_day(int(loan_period))
					pay_gross = (loan * interest)+ loan
					print('\nYou have requested loan for ',loan,'paid in',number_of_days,'days' )
					print('\nIf aproved You will pay $',pay_gross,'on',loan_period ,'at' ,interest,'interest')

					restart = input('Would you like to go back? ')
					if restart in ('n','no','NO','N'):
						print('THANKS FOR YOUR SERVICE')

				#third or more loan accesses
				elif loan_request <= balance * 3 and loan_number > 2:
					print('Your interest is now only at 20%!!')
					interest = 0.2
					#calculating loan payment date
					def loan_lastpay_day(loan_period):
						today = datetime.date.today()
						total_days = datetime.timedelta(int(loan_period))
						last_loan_day = today + total_days 
						return last_loan_day 
	
					
					balance = balance
					loan = loan_request
					Account_loan = loan
					# monthly= 30
					loan_period = input('Enter loan Period in number of days :' )
					number_of_days = loan_period
					loan_period = loan_lastpay_day(int(loan_period))
					pay_gross = (loan * interest)+ loan
					print('\nYou have requested loan for ',loan,'paid in',number_of_days,'days' )
					print('\nIf aproved You will pay $',pay_gross,'on',loan_period ,'at' ,interest,'interest')

					restart = input('Would you like to go back? ')
					if restart in ('n','no','NO','N'):
						print('THANKS FOR YOUR SERVICE')

				#loan for more than 3 times borrowers
				elif loan_request >= balance * 5  and loan_number > 3:
					print('You have earned our trust! Now you can get X 5 Your Balance at only 20%!!')
					interest = 0.2
					#calculating loan payment date
					def loan_lastpay_day(loan_period):
						today = datetime.date.today()
						total_days = datetime.timedelta(int(loan_period))
						last_loan_day = today + total_days 
						return last_loan_day 
	
					
					balance = balance
					loan = loan_request
					Account_loan = loan
					# monthly= 30
					loan_period = input('Enter loan Period in number of days :' )
					number_of_days = loan_period
					loan_period = loan_lastpay_day(int(loan_period))
					pay_gross = (loan * interest)+ loan
					print('\nYou have requested loan for ',loan,'paid in',number_of_days,'days' )
					print('\nIf aproved You will pay $',pay_gross,'on',loan_period ,'at' ,interest,'interest')

					restart = input('Would you like to go back? ')
					if restart in ('n','no','NO','N'):
						print('THANKS FOR YOUR SERVICE')

					#handling a first borrower requesting more than 3 times their account balances
				else:
					if loan_number ==1:
						print('Being your first loan and more than X 2 your Balance')
					print('Loans that are more than 3 x your Account balance are at 50%!!')
					# print('Your Account Balance is ',balance,'you can get ' balance * 3, 'or lower')
					loan_request = float(input('Enter amount more than X 3 Your Balance: '))
					if loan_request >= balance * 3 :
						interest = 0.5

						#calculating loan payment date
						def loan_lastpay_day(loan_period):
							today = datetime.date.today()
							total_days = datetime.timedelta(loan_period)
							last_loan_day = today + total_days 
							return last_loan_day 

							
						balance = balance
						loan = loan_request
						Account_loan = loan
						# monthly= 30
						loan_period = input('Enter loan Period in number of days :' )
						number_of_days = loan_period
						loan_period = loan_lastpay_day(int(loan_period))
						pay_gross = (loan * interest)+ loan
						print('\nYou have requested loan for ',loan,'paid in',number_of_days,'days' )
						print('\nIf aproved You will pay $',pay_gross,'on',loan_period ,'at' ,interest,'interest')

			#make a bank deposit
			elif option == 3:
				deposit = float(input('Enter your deposit amount: '))
				balance = balance + deposit
				print('\nYour Account Blance is now $:',balance)
				restart = input('Would you like to go back? ')
				if restart in ('no','n','NO','N'):
					print('THANKS FOR YOUR SERVICE')
					break
			#cancel any transaction
			elif option == 4:
				print('Thanks for using our service')
				print('Visit us again')
				exit()
			#if the wrong choice selected
			else:
				print('Please Enter the Correct option \n')
				print('Choose one of these : 1,2,3,or 4')
				restart = ('y')
	#if wrong pin entered
	elif pin != (1994) :
		print('Incorrect Pin code')
		#subtracting the number of pin retries
		pin_retry_chances = pin_retry_chances - 1
		# pin_retries_remender = pin_retry_chances
		print('You have ', pin_retry_chances,'Pin code retries remaining before you are blocked !!')
		if pin_retry_chances == 0:
			print('\nSeems you have lost your pin Code.')
			print('Please visit your bank Branch and ask for new Pin Code')
			break
