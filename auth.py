import random
import validate
import database
from getpass import getpass
#database = {2037811149: ['Seyi', 'Ade', 'xyz@gmail.com','pass', 234809999867, 200]
#            }

balance = 0

def init():
    print('==' * 30)
    print('Welcome to BankRuby!')

    create_account = int(input('Do you have an account with us :  Press 1(yes) 2 (no) \n'))
    if create_account == 1:
        login()
    elif create_account == 2:

        print(register())
    else:
        print('==' * 30)
        print(' Error! You have selected an invalid option')
        init()


def login():
    print('==' * 30)
    print('Please Log in to your account')

    accountnumber_frm_user = input('Enter your account number:\n')
    is_valid_account_number = validate.account_number_validation(accountnumber_frm_user)
    if is_valid_account_number:
        password = getpass('Enter your password:\n')
        user =database.authenticated_user(accountnumber_frm_user,password);

        if user:
            bankingOptions(user)
            print('Invalid account or password')
            login()
    else:
        init()



def register():
    print('========Register here!========')
    print('Please open and  register an account with us today!')
    first_name = input('Enter your first name:\n')
    surname = input('Enter your surname: \n')
    email = input('Please enter a valid email account: \n')
    password = input('Create a strong password: \n')
    phone_number = int(input('Enter a valid phone number: Please use 234 at the beginning of your number instead of 0\n'))

    accountnumber = generateAccountNum()
    user_file_created = database.create(accountnumber, [first_name, surname, email, password, phone_number, 0])

    if user_file_created == True:
        print('==' * 30)
        print('Your account has been created')
        print(f'Welcome to our family {first_name}!')
        print(f'Your account number is {accountnumber}')
        print('='*30)
        login()
    else:
        print('Something went wrong,Please try again later')
        register()


def withdrawaloperation():
    print('Withdrawal option')


def depositOperation():
    print('Deposit')


def generateAccountNum():
    print('==' * 30)
    print('Generating account number')
    return random.randrange(2000000000, 2099999999)
def set_user_balance(userdetails,balance):
    userdetails[5] = balance




def bankingOptions(user):
    print(f'Welcome {user[0]}, {user[1]}')
    selectedOption = int(
        input('Please select an option for the next step Press(1) for deposit,(2)Withdrawal,(3)Logout,(4)exit\n'))
    if selectedOption == 1:
        depositOperation()
    elif selectedOption == 2:
        withdrawaloperation()
    elif selectedOption == 3:
        logout()
    elif selectedOption== 4:
        exit()
    else:
        print('You have selected an invalid option')


def logout():
    print('You have successfully logged out!')
    login()

def check_balance(userdetails):
    return userdetails[5]

init()
