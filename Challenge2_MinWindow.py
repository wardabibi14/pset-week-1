#Brute force approach
from collections import Counter

def MinWindow(log, pattern):
    n = len(log)
    if not log or not pattern:
        return ""
    
    need = Counter(pattern)
    min_len = float('inf')
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            window = Counter(log[i:j+1])
            if all(window[c] >= need[c] for c in need):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    result = log[i:j+1]
    
    return result

log = input("log=").strip()
pattern = input("pattern=").strip()
print(MinWindow(log, pattern))