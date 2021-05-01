def account_number_validation(accountnumber):
    if accountnumber:
        if len(str(accountnumber))== 10:
            try:
                int(accountnumber)
                return True
            except ValueError:
                print('Invalid account number!, Account number enter is not an integer')
                return True
            except TypeError:
                print('Syntax error!,Invalid account number entered')
                return False
    return False
