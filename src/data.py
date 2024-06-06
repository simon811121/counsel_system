import os
import csv
import datetime
import json
from enum import Enum
from runtime_type_checker import check_type
from typing import Any, Dict

config_file_name = "config.json"
acnt_info_file_name = "account_info.csv"
acnt_info_fieldnames = ['user_id', 'permission', 'permission_id', 'account', 'password', 'name', 'email', 'phone_num', 'register_time', 'last_login_time']
allowed_permissions = {'director', 'psychologist', 'manager', 'guest'}

class Config:
    def __init__(self):
        file_path = gen_file_path(config_file_name)
        self.file_path = file_path
        self.settings = self._read_settings()

    def _read_settings(self) -> Dict[str, Any]:
        with open(self.file_path, 'r') as file:
            settings = json.load(file)
        return settings

    def get_setting(self, section: str, key: str) -> Any:
        return self.settings.get(section, {}).get(key, None)

    def get_section(self, section: str) -> Dict[str, Any]:
        return self.settings.get(section, {})

    def update_setting(self, section: str, key: str, value: Any):
        if section in self.settings:
            self.settings[section][key] = value
        else:
            self.settings[section] = {key: value}

    def save_settings(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.settings, file, indent=4)


class Allow_Perm(Enum):
    director = 1
    psychologist = 2
    manager = 3
    guest = 4

class Account_Info:
    class Info:
        def __init__(self,
                     user_id: int,
                     permission: str,
                     account: str,
                     password: str,
                     name: str,
                     email: str,
                     phone_num: int,
                     register_time: str,
                     last_login_time: str):
            check_type(user_id, int)
            check_type(permission, str)
            check_type(account, str)
            check_type(password, str)
            check_type(name, str)
            check_type(email, str)
            check_type(phone_num, str)
            check_type(register_time, str)
            check_type(last_login_time, str)
            if permission not in allowed_permissions:
                raise ValueError("Invalid permission value. Allowed values: 'director', 'psychologist', 'manager', 'guest'")
            permission_id = Allow_Perm[permission]
            self.user_id = user_id
            self.permission = permission
            self.permission_id = permission_id.value
            self.account = account
            self.password = password
            self.name = name
            self.email = email
            self.phone_num = phone_num
            self.register_time = register_time
            self.last_login_time = last_login_time

    def __init__(self):
        self.file_name = "account_info.csv"
        self._build_file()
        self.infos = []
        self.glb_cfg = Config()
        self.setting = self.glb_cfg.get_section('acnt_info')

    def _build_file(self):
        file_path = gen_file_path(self.file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=acnt_info_fieldnames)
                writer.writeheader()

    def add_acnt_info(self,
                      permission: str,
                      account: str,
                      password: str,
                      name: str,
                      email: str,
                      phone_num: int,
                      register_time: str,
                      last_login_time: str):
        user_id = self.setting['nxt_user_id']
        max_user_id = self.setting['max_user_id']
        if (user_id < max_user_id):
            info = self.Info(user_id, permission, account, password, name, email, phone_num, register_time, last_login_time)
            self.infos.append(info)
            user_id += 1
            self.glb_cfg.update_setting('acnt_info', 'nxt_user_id', user_id)
            self.glb_cfg.save_settings()
            file_path = gen_file_path(self.file_name)
            with open(file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([info.user_id, info.permission, info.permission_id, info.account, info.password, info.name, info.email, info.phone_num, info.register_time, info.last_login_time])

def gen_file_path(file_name):
    cur_path = os.getcwd()
    file_path = os.path.join(cur_path, 'data', file_name)
    return file_path

if __name__ == '__main__':
    acnt_info = Account_Info()
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    acnt_info.add_acnt_info('director', 'abcd', 'qazwsx', 'Simon', 's@example.com', '12345678', for_time, for_time)
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    acnt_info.add_acnt_info('psychologist', 'efgh', 'edcrfv', 'Jing', 'J@example.com', '87654321', for_time, for_time)
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    acnt_info.add_acnt_info('manager', 'efgh', 'edcrfv', 'Jing', 'J@example.com', '87654321', for_time, for_time)