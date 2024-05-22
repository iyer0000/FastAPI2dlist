import datetime
from concurrent.futures import ProcessPoolExecutor
import logging
import sys 
def return_empty(ele_list:list):
    try:
        if len(ele_list)== 0:
            return True
        else:
            return False
    except Exception as e:
        return True
    
def get_sum_elements(ele_list:list):
    try:
        if return_empty(ele_list):
            return "empty"
        else:
            return sum(ele_list)
    except Exception as e:
        return "empty"

def get_current_date():
    return datetime.datetime.now()

def execute_process(input_list):
    output_list = []
    if len(input_list)-1<1:
        workers_count=1
    else:
        workers_count=len(input_list)-1
    with ProcessPoolExecutor(max_workers=workers_count) as pool:
        output_list.extend(pool.map(get_sum_elements, input_list))
    if len(output_list)>0:
        return output_list
    
def validate_output_list(input_list):
    temp=set(input_list)
    if 'empty' in temp and len(temp)==1:
        return True
    else:
        return False
    
def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(r'logs\log.txt', mode='a')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger