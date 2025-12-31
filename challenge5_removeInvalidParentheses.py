#Brute force approach
def isValid(s):
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            if balance == 0:
                return False
            balance -= 1
    return balance == 0

def removeInvalidParentheses(expr):
    res = set()
    min_removed = float('inf')

    def dfs(s, idx, removed):
        nonlocal min_removed

        if idx == len(s):
            if isValid(s):
                if removed < min_removed:
                    res.clear()
                    min_removed = removed
                if removed == min_removed:
                    res.add(s)
            return

        if s[idx] in "()":
            dfs(s[:idx] + s[idx+1:], idx, removed + 1)

        dfs(s, idx + 1, removed)

    dfs(expr, 0, 0)
    return list(res)

