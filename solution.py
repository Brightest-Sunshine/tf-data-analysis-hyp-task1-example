import pandas as pd
import numpy as np
from scipy.stats import binomtest


chat_id = 453878141 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt : int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha=0.04
    p_control_robot = x_success / x_cnt
    p_control_operator = (x_cnt - x_success) / x_cnt
    successes_robot = y_success
    successes_operator = y_success - (y_cnt - y_success) * (p_control_operator / p_control_robot)
    p_value = binomtest(successes_robot, n=y_cnt, p=p_control_operator, alternative='less').pvalue
    if p_value > alpha:
        return True
    else:
        return False
