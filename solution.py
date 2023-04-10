import pandas as pd
import numpy as np
from scipy.stats import fisher_exact

chat_id = 453878141 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt : int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.04
    odds_ratio, p_value = fisher_exact([[x_success, x_cnt - x_success], [y_success, y_cnt - y_success]], alternative='less')
    if p_value < alpha and odds_ratio < 1:
        return True 
    else:
        return False
