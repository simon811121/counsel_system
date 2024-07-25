from src.util import get_cur_time

def test_add_acnt_info(test_acnt_info):
    for_time = get_cur_time()
    rslt = test_acnt_info.add_acnt_info('director', 'abcd', 'qazwsx', 'Simon', 's@example.com', '12345678', for_time, for_time)
    assert rslt == True
    acnt = test_acnt_info.find_acnt_info(user_id=0)
    acnt_ = test_acnt_info.find_acnt_info(account='abcd')
    assert acnt != None
    assert acnt._equals(acnt_) == True
    assert acnt.user_id == 0
    assert acnt.permission == 'director'
    assert acnt.account == 'abcd'
    assert acnt.password == 'qazwsx'
    assert acnt.name == 'Simon'
    assert acnt.email == 's@example.com'
    assert acnt.phone_num == '12345678'
    assert acnt.register_time == for_time
    assert acnt.last_login_time == for_time
    for_time = get_cur_time()
    rslt = test_acnt_info.add_acnt_info('psychologist', 'efgh', 'asdfgh', 'Jobs', 'j@example.com', '87654321', for_time, for_time)
    assert rslt == True
    acnt = test_acnt_info.find_acnt_info(user_id=1)
    acnt_ = test_acnt_info.find_acnt_info(account='efgh')
    assert acnt != None
    assert acnt._equals(acnt_) == True
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
    for_time = get_cur_time()
    rslt = test_acnt_info_set_nxt_user_id.add_acnt_info('manager', 'ijkl', 'asdfgh', 'Jobs', 'h@example.com', '99999999', for_time, for_time)
    assert rslt == False

def test_update_acnt_info(test_acnt_info):
    for_time = get_cur_time()
    rslt = test_acnt_info.add_acnt_info('director', 'abcd', 'qazwsx', 'Simon', 's@example.com', '12345678', for_time, for_time)
    assert rslt == True
    test_acnt_info.update_acnt_info(user_id=0, password='edcrfv')
    acnt = test_acnt_info.find_acnt_info(user_id=0, skip_cache=True)
    assert acnt.password == 'edcrfv'
    test_acnt_info.update_acnt_info(user_id=0, name='nomiS')
    acnt = test_acnt_info.find_acnt_info(user_id=0, skip_cache=True)
    assert acnt.name == 'nomiS'
    test_acnt_info.update_acnt_info(user_id=0, email='i@exmaple.com')
    acnt = test_acnt_info.find_acnt_info(user_id=0, skip_cache=True)
    assert acnt.email == 'i@exmaple.com'
    test_acnt_info.update_acnt_info(user_id=0, phone_num='87654321')
    acnt = test_acnt_info.find_acnt_info(user_id=0, skip_cache=True)
    assert acnt.phone_num == '87654321'
    for_time = get_cur_time()
    test_acnt_info.update_acnt_info(account='abcd', last_login_time=for_time)
    acnt = test_acnt_info.find_acnt_info(account='abcd', skip_cache=True)
    assert acnt.last_login_time == for_time
    test_acnt_info.update_acnt_info(account='abcd', password='edcrfv')
    acnt = test_acnt_info.find_acnt_info(account='abcd', skip_cache=True)
    assert acnt.password == 'edcrfv'
    test_acnt_info.update_acnt_info(account='abcd', name='nomiS')
    acnt = test_acnt_info.find_acnt_info(account='abcd', skip_cache=True)
    assert acnt.name == 'nomiS'
    test_acnt_info.update_acnt_info(account='abcd', email='i@exmaple.com')
    acnt = test_acnt_info.find_acnt_info(account='abcd', skip_cache=True)
    assert acnt.email == 'i@exmaple.com'
    test_acnt_info.update_acnt_info(account='abcd', phone_num='87654321')
    acnt = test_acnt_info.find_acnt_info(account='abcd', skip_cache=True)
    assert acnt.phone_num == '87654321'
    for_time = get_cur_time()
    test_acnt_info.update_acnt_info(account='abcd', last_login_time=for_time)
    acnt = test_acnt_info.find_acnt_info(account='abcd', skip_cache=True)
    assert acnt.last_login_time == for_time

def test_add_cnsl_rcrd(test_cnsl_rcrd):
    record = {
        'name': 'John Doe',
        'bio_sex': 'Male',
        'birth_date': '1985-05-15',
        'id_num': '1234567890',
        'address': '123 Main St, Anytown, USA',
        'counsel_date': '2024-07-25',
        '01. Individual Counseling': True,
        '02. Couple/Family Counseling': False,
        '03. Parent/Child Counseling': False,
        '04. Tele-counseling': True,
        '01. Financial Issues': False,
        '02. Employment/Work': True,
        '03. Career Planning': False,
        '04. Psychological Issues Related to Medical Health': False,
        '05. Self-Awareness': True,
        '06. Emotional Distress': False,
        '07. Behavioral Issues': False,
        '08. Major Loss or Life Changes': False,
        '09. General Information': False,
        '10. Learning Issues': False,
        '11. Interpersonal Relationships': True,
        '12. Stress and Emotional Distress': True,
        '13. Domestic Violence': False,
        '14. Suicide/Self-Harm': False,
        '15. Sexual Assault': False,
        '16. Sexual Issues': False,
        '17. Death/Grief': False,
        '18. Family Issues': False,
        '19. Other': False,
        '01. Establish Relationship': True,
        '02. Focus on Work Goals': True,
        '03. Increase Self-Awareness': True,
        '04. Reduce Frustration': False,
        '05. Process Past Experiences': False,
        '06. Improve Interpersonal Relationships': True,
        '07. Enhance Emotional Management Skills': True,
        '08. Increase Coping Strategies': False,
        '09. Improve Environmental Adaptation Skills': False,
        '10. Other': False,
        '01. Goal Setting': True,
        '02. Empathy and Support': True,
        '03. Experience Integration': False,
        '04. Internal Focus': False,
        '05. Self-Exploration': True,
        '06. Empowerment': False,
        '07. Emotional Expression': True,
        '08. Reframing': False,
        '09. Information Provision': False,
        '10. Case Closure Preparation': False,
        '11. Other': False,
        'Summary': 'John discussed his career goals and strategies for improving interpersonal relationships and managing stress.'
    }

    test_cnsl_rcrd.add_record(record)

    read_data = test_cnsl_rcrd.read_record(1234567890)
    assert read_data == record