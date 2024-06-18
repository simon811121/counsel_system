import datetime

def test_add_acnt_info(test_acnt_info):
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    rslt = test_acnt_info.add_acnt_info('director', 'abcd', 'qazwsx', 'Simon', 's@example.com', '12345678', for_time, for_time)
    assert rslt == True
    acnt = test_acnt_info.find_acnt_info(0)
    assert acnt != None
    assert acnt.user_id == 0
    assert acnt.permission == 'director'
    assert acnt.account == 'abcd'
    assert acnt.password == 'qazwsx'
    assert acnt.name == 'Simon'
    assert acnt.email == 's@example.com'
    assert acnt.phone_num == '12345678'
    assert acnt.register_time == for_time
    assert acnt.last_login_time == for_time
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    rslt = test_acnt_info.add_acnt_info('psychologist', 'efgh', 'asdfgh', 'Jobs', 'j@example.com', '87654321', for_time, for_time)
    assert rslt == True
    acnt = test_acnt_info.find_acnt_info(1)
    assert acnt != None
    assert acnt.user_id == 1
    assert acnt.permission == 'psychologist'
    assert acnt.account == 'efgh'
    assert acnt.password == 'asdfgh'
    assert acnt.name == 'Jobs'
    assert acnt.email == 'j@example.com'
    assert acnt.phone_num == '87654321'
    assert acnt.register_time == for_time
    assert acnt.last_login_time == for_time

def test_add_acnt_info_full(test_acnt_info_set_nxt_user_id):
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    rslt = test_acnt_info_set_nxt_user_id.add_acnt_info('manager', 'ijkl', 'asdfgh', 'Jobs', 'h@example.com', '99999999', for_time, for_time)
    assert rslt == False