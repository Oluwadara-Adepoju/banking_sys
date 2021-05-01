import os
import validate
user_database_path= 'data storage/user_record/'

def create(accountnumber_frm_user, first_name,last_name,email,password,phone_number):
    user_data = first_name+','+last_name','+email+','+password+','+str(phone_number)+ str(0)
    if does_accountnumber_exist(accountnumber_frm_user):
        return False
    if does_email_exist(email):
        print('User already exists')
        return False

    complete_state = False

    try:
        c = open('data storage/user_record/' + str(accountnumber_frm_user) + '.txt', 'a')

    except FileExistsError:
        print('User already exist in database')
        does_file_location_contain_data = read(user_database_path)+str(accountnumber_frm_user)+'.txt')
        if not does_file_location_contain_data:
            delete(accountnumber_frm_user)

    else:
        c.close()
        return complete_state


def update(userdetails):
    print('Update user record')


def read(accountnumber_frm_user):
    is_valid_account_nos = validate.account_number_validation(accountnumber_frm_user)
    try:
        if is_valid_account_nos:
            c = open(user_database_path +str(accountnumber_frm_user)+'.txt','r')
        else:
            c = open(user_database_path+accountnumber_frm_user,'r')
    except FileNotFoundError:
        print('User not found in database')
    except TypeError:
        print('Invalid account number format!')

    else:
        return c.readline()


def delete(user_accountnumber):
    delete_account = False
    confirm_delete =int(input('Are you sure you want to delete your account? Press (1)  \n'))
    if confirm_delete == 1:
        if os.path.exists(user_database_path + str(user_accountnumber) + '.txt'):

            try:
                os.remove(user_database_path+ str(user_accountnumber)+ '.txt')
                delete_account = True
            except FileNotFoundError:
                print('User not found in database')
            finally:
                return delete_account

    else:
        exit()







def find(user_accountnumber_frm_user):
    print('Scanning database')
def authenticated_user():
    print('Authenticating user')
def does_email_exist(accountnumber,email):
   all_users = os.listdir(user_database_path)
   for user in all_users:
       user_list = str.split(read(user),',')
       if email in user_list:
           return True
    return False
def does_account_number_exist(accountnumber):
    all_users = os.listdir(user_database_path)
    for user in all_users:
        if user == str(accountnumber) + '.txt':
            return True

    return False

def authenticated_user(accountnumber,password):
    if does_account_number_exist(accountnumber):
        user = str.split(read(accountnumber),',')
        if password == user[3]:
            return user
    return False






does_email_exist(2049088262,'adeolu@gmail.com')