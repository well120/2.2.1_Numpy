import numpy as nps
import scipy
import re
def t1_file_stat(filename):
    data = np.loadtxt(filename, delimiter = '\n', dtype = np.int, usecols = len(re.findall(r"[\n']+", filename))) 
    if data.size <= 2:
        return "Try again"
    else:
        return {                
        "mean": data.mean(),
        "max": data.max(),
        "min": data.min(),
        "std_dev": data.std(),
        "5th_central_moment": scipy.stats.moment(data, moment = 5, nan_policy='propagate'),
        }
def t2_sort_int(array):
    return sorted(array)
def t3_sort_complex(complex_array):
    a = []
    b = []
    if len(complex_array) == 0:
        return "Try again"
    else:
        for i in complex_array:
            a.append(abs(i))
        for j in complex_array:
            b.append(j.real)
        return (sorted(a), sorted(b)[::-1])
def t4_sort_string_len(string_array):
    a = []
    if len(string_array) == 1 or len(string_array) == 0:
        return "Try again"
    else:
        for i in string_array:
            a.append(len(i))
        return sorted(a)
def t5_sort_string_tuple(string_tuple):
    if len(string_tuple) == 1 or len(string_tuple) == 0:
        return "Try again"
    else:
        return sorted(sorted(string_tuple), key=str.upper)