#!/usr/bin/env python3

# Set initial balances for account holders
BALANCES = {'Wanjiru':0, 'Juma':0, 'Linda':0}

# Open and read account logs from account_logs.txt
with open('account_logs.txt', 'r') as logs:
    data = logs.readlines()
    
    # Define an empty array to hold all logs
    account_logs = []

    for logs in data:
        log = logs.split(':') # Split data where there is a :
        account_logs.append(log) # Add each log to the list
    
    
    for log in account_logs:
        '''
        Loop through account_logs list checking whether
        a transaction is a Deposit,Withdraw or Transfer

        Deposit - Increment account balance by amount:
            Bal = 0 , Deposit = 100
            Return Bal + Deposit ; 100

        Withdraw - Check account balance, if amount is 
        enough reduce the bal:
            Bal = 500 , Withdraw = 300
            Return Bal-Withdraw ; 200

        Transfer - Check account balance, if amount is 
        enought reduce bal and increase bal for other acc
            Bal acc A = 900, Transfer = 500
            Return Bal acc A Bal-Transfer ; 400
            
            Bal acc B = 200 , Transfer = 500
            Return Bal acc B Bal+Transfer ; 700
        '''
        
        # BALANCES = {'Wanjiru':0, 'Juma':0, 'Linda':0}
        if log[0] == 'DEPOSIT':
            # List sample - ['DEPOSIT', 'Wanjiru', '152.00\n']
            if log[1] in BALANCES:
                # float for decimal numbers
                amount = float(BALANCES[log[1]]) + float(log[2])
                BALANCES[log[1]] = amount
                print('Deposit successful:', BALANCES)

        elif log[0] == 'WITHDRAW' and log[1] in BALANCES:
            if float(BALANCES[log[1]]) >= float(log[2]):
                amount = float(BALANCES[log[1]]) - float(log[2])
                BALANCES[log[1]] = amount
                print('Withdrawal successful:', BALANCES)
            else:
                print('Insufficient balance:', BALANCES)
        elif log[0] == 'TRANSFER' and log[1] in BALANCES and log[2] in BALANCES:
            # List sample - ['TRANSFER', 'Juma', 'Linda', '500.00\n']
            if float(BALANCES[log[1]]) >= float(log[3]):
                BALANCES[log[1]] = float(BALANCES[log[1]])-float(log[3])
                BALANCES[log[2]] = float(BALANCES[log[2]])+float(log[3])
                print('Transfer successful:', BALANCES)
            else:
                print('Insufficient balance:', BALANCES)
    print("\n")
    print('Final balances: ',BALANCES)