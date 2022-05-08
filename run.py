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
    print(account_logs)