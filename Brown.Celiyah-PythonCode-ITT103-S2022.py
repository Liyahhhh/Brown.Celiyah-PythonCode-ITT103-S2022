'''
Author: Celiyah Brown 
Date Created: April 25, 2022
Course: ITT103
Purpose: <THIS PROGRAMME IS DESIGNED TO CALCULATE AND PRINT THE COMMISSION RECIEVED OF SALESPERSONS FROM JAMEX LIMITED.>
'''


def commission_rec():
    print('Good day,today we will be calculating your commision received. ')
    terminal =  str(input("To continue enter 'y' else enter 'n' "))
    terminal = terminal.strip()
    if terminal != 'y':
        terminal = str(input("Are you positive? Enter 'y' to continue the program else 'n' to end "))
        terminal = terminal.strip()
    while terminal == 'y':
        salesperson_no = str(input('Enter your salesperson number '))
        try:
            class_no = float(input('Enter your class number: either 1, 2 or 3 '))
        except ValueError:
            class_no = float(input('Enter your class number, ensure its strictly numerical: 1, 2 or 3 '))
        
        if class_no == 1:
            try:
                sales_amount = float(input('Enter your sales amount '))
            except ValueError:
                sales_amount = float(input('Enter your sales amount, ensure its strictly numerical '))

            #Calculating the commision received for class 1 workers with increased rates of either 6%, 7% or 10% depending on the amount made.
            if sales_amount <= 1000:
                commision_rec = (sales_amount + (sales_amount * .06))
                print('{} total commision recieved is {} in class {}. '.format(salesperson_no, commision_rec, class_no))
            elif sales_amount > 1000 and sales_amount <  2000:
                commision_rec = (sales_amount + (sales_amount * .07))
                print('{} total commision recieved is {} in class {}. '.format(salesperson_no, commision_rec, class_no))
            elif  sales_amount >= 2000:
                commision_rec = (sales_amount + (sales_amount * .10))
                print('{} total commision recieved is {} in class {}. '.format(salesperson_no, commision_rec, class_no))
            
        elif class_no == 2:
            try:
                sales_amount = float(input('Enter your sales amount '))
            except ValueError:
                sales_amount = float(input('Enter your sales amount, ensure its strictly numerical '))
            
            #Calculating the commision received for class 2 workers with increased rates of either 4% or 6% depending on the amount made.
            if sales_amount < 1000:
                commision_rec = (sales_amount + (sales_amount * .04))
                print('{} total commision recieved is {} in class {}. '.format(salesperson_no, commision_rec, class_no))
            elif sales_amount  >= 1000:
                commision_rec = (sales_amount + (sales_amount * .06))
                print('{} total commision recieved is {} in class {}. '.format(salesperson_no, commision_rec, class_no))

        elif class_no == 3:
            try:
                sales_amount = float(input('Enter your sales amount '))
            except ValueError:
                sales_amount = float(input('Enter your sales amount, ensure its strictly numerical '))
            
            #Calculating the commision received for class 3 workers with increased rates of 4.5% regardless of the amount made.
            commision_rec = (sales_amount + (sales_amount * .045))
            print('{} total commision recieved is {} in class {}. '.format(salesperson_no, commision_rec, class_no))
            
        else:
            print('This class does not exist please ensure to enter correct class.')
    
        terminal =  str(input("Would you like to continue enter 'y' else enter 'n' "))
        terminal = terminal.strip()
        if terminal != 'y':
            terminal = str(input("Are you positive? enter y to continue the program else 'n' to end  "))
            terminal = terminal.strip()
    print('Thank you!')

commission_rec()
