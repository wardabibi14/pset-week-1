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


#optimized approach
from collections import Counter

def MinWindow(log, pattern):
    if not log or not pattern:
        return ""
    
    need = Counter(pattern)
    window = {}
    
    have = 0
    required = len(need)
    left = 0
    min_len = float('inf')
    result = ""
    
    for right in range(len(log)):
        char = log[right]
        window[char] = window.get(char, 0) + 1
        
        if char in need and window[char] == need[char]:
            have += 1
        
        while have == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = log[left:right+1]
            
            window[log[left]] -= 1
            if log[left] in need and window[log[left]] < need[log[left]]:
                have -= 1
            left += 1
    
    return result
log = input("log=").strip()
pattern = input("pattern=").strip()
print(MinWindow(log, pattern))