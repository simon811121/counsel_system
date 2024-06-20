import datetime

def get_cur_time():
    cur_time = datetime.datetime.now()
    for_time = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    return for_time