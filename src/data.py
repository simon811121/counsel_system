import os
import csv
import datetime

acnt_info_file_name = "account_info.csv"
fieldnames = ['user_id', 'permission', 'account', 'password', 'name', 'email', 'phone_num', 'register_time', 'last_login_time']
class Account_Info:
    class Info:
        def __init__(self, user_id, permission, account, password, name, email, phone_num, register_time, last_login_time):
            self.user_id = user_id
            self.permission = permission
            self.account = account
            self.password = password
            self.name = name
            self.email = email
            self.phone_num = phone_num
            self.register_time = register_time
            self.last_login_time = last_login_time
    def __init__(self):
        self.infos = []
    def add_info(self, user_id, permission, account, password, name, email, phone_num, register_time, last_login_time):
        info = self.Info(user_id, permission, account, password, name, email, phone_num, register_time, last_login_time)
        self.infos.append(info)

def gen_file_path(file_name):
    cur_path = os.getcwd()
    file_path = cur_path + "\\" + file_name
    return file_path

def check_file(file_name):
    return os.path.exists(gen_file_path(file_name))

def build_file(file_name):
    file_path = gen_file_path(file_name)
    if check_file(file_name) == True:
        print("File exist")
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            account_info = Account_Info()
            account_info.add_info(1, 'director', 'user1', 'pwd1', 'John Snow', 'john_snow@example.com', '12345678', formatted_datetime, formatted_datetime)
            account_info.add_info(2, 'director', 'user2', 'pwd2', 'Snow Peak', 'snow_peak@example.com', '87654321', formatted_datetime, formatted_datetime)
            for info in account_info.infos:
                writer.writerow([info.user_id, info.permission, info.account, info.password, info.name, info.email, info.phone_num, info.register_time, info.last_login_time])
    else:
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        print("File NOT exist, create one")

if __name__ == '__main__':
    build_file(acnt_info_file_name)