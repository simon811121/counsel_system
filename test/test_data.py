import datetime
from src.data import Allow_Perm

def test_add_acnt_info(test_acnt_info):
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    test_acnt_info.add_acnt_info('director', 'abcd', 'qazwsx', 'Simon', 's@example.com', '12345678', for_time, for_time)
    acnt = test_acnt_info.find_acnt_info(0)
    assert acnt != None
    assert acnt['user_id'] == '0'
    assert acnt['permission'] == 'director'
    assert acnt['account'] == 'abcd'
    assert acnt['password'] == 'qazwsx'
    assert acnt['name'] == 'Simon'
    assert acnt['email'] == 's@example.com'
    assert acnt['phone_num'] == '12345678'
    assert acnt['register_time'] == for_time
    assert acnt['last_login_time'] == for_time
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    test_acnt_info.add_acnt_info('psychologist', 'efgh', 'asdfgh', 'Jobs', 'j@example.com', '87654321', for_time, for_time)
    acnt = test_acnt_info.find_acnt_info(1)
    assert acnt != None
    assert acnt['user_id'] == '1'
    assert acnt['permission'] == 'psychologist'
    assert acnt['account'] == 'efgh'
    assert acnt['password'] == 'asdfgh'
    assert acnt['name'] == 'Jobs'
    assert acnt['email'] == 'j@example.com'
    assert acnt['phone_num'] == '87654321'
    assert acnt['register_time'] == for_time
    assert acnt['last_login_time'] == for_time