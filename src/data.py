import os
import csv
import json
from enum import Enum
from runtime_type_checker import check_type
from typing import Any, Dict

acnt_info_fieldnames = ['user_id', 'permission', 'account', 'password', 'name', 'email', 'phone_num', 'register_time', 'last_login_time']
class Allow_Perm(Enum):
    director = 1
    psychologist = 2
    manager = 3
    guest = 4

class Config:
    def __init__(self,
                 testing: bool):
        self.file_name = "config.json" if testing is False else "config_test.json"
        file_path = gen_file_path(self.file_name)
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
            self.allow_perm = {'director', 'psychologist', 'manager', 'guest'}
            if permission not in self.allow_perm:
                raise ValueError("Invalid permission value. Allowed values: 'director', 'psychologist', 'manager', 'guest'")
            self.user_id = user_id
            self.permission = permission
            self.account = account
            self.password = password
            self.name = name
            self.email = email
            self.phone_num = phone_num
            self.register_time = register_time
            self.last_login_time = last_login_time
        def __str__(self):
            return (f"Info(user_id = {self.user_id}\n"
                    f"     permission = {self.permission}\n"
                    f"     account = {self.account}\n"
                    f"     password = {self.password}\n"
                    f"     name = {self.name}\n"
                    f"     email = {self.email}\n"
                    f"     phone_num = {self.phone_num}\n"
                    f"     register_time = {self.register_time}\n"
                    f"     last_login_time = {self.last_login_time})")

    def __init__(self,
                 file_name: str = None):
        self.file_name = "account_info.csv" if file_name is None else file_name
        self.file_path = gen_file_path(self.file_name)
        self._build_file()
        self.infos = []
        self.glb_cfg = Config(False) if file_name is None else Config(True)
        self.setting = self.glb_cfg.get_section('acnt_info')

    def _build_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=acnt_info_fieldnames)
                writer.writeheader()

    def _refresh_file(self): # only for unit-testing
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            self._build_file()

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
            self.file_path = gen_file_path(self.file_name)
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([info.user_id, info.permission, info.account, info.password, info.name, info.email, info.phone_num, info.register_time, info.last_login_time])
            return True
        else:
            return False

    def find_acnt_info(self,
                       user_id: int):
        for infos in self.infos:
            if infos.user_id == user_id:
                return infos
        with open(self.file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Check if the user_id matches
                if int(row['user_id']) == user_id:
                    row['user_id'] = user_id
                    infos = self.Info(**row)
                    self.infos.append(infos)
                    return infos
            return None

def gen_file_path(file_name):
    cur_path = os.getcwd()
    file_path = os.path.join(cur_path, 'data', file_name)
    return file_path

acnt_info = Account_Info()