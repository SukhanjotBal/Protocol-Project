from collections import Counter
import numpy as np

def entropy(text):
    if text == "":
        return 0
    char_count = Counter(text)
    counts = []
    n = len(text)
    for i in char_count.values():
        counts.append(i/n)
    log_val = []
    for p in counts:
        log_val.append(np.log2(p))
    weighted_avg = np.average(log_val, weights=counts)
    H = -1 * (weighted_avg)
    return H
def byte_check(test1, check1):
    H = entropy(test1)
    return len(test1) * H / 8
test1 = "aaabb"
check1 = entropy(test1)
print(check1)
check2 = byte_check(test1, check1)
print(check2)