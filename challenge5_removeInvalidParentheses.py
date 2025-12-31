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

expr = input("Enter expression: ")
result = removeInvalidParentheses(expr)
print(result)



#Optimized approach
def countRemovals(s):
    left = right = 0
    for ch in s:
        if ch == '(':
            left += 1
        elif ch == ')':
            if left > 0:
                left -= 1
            else:
                right += 1
    return left, right
def removeInvalidParentheses(expr):
    left_rem, right_rem = countRemovals(expr)
    res = set()

    def dfs(index, path, balance, l_rem, r_rem):
        # Invalid state
        if balance < 0 or l_rem < 0 or r_rem < 0:
            return

        # End of string
        if index == len(expr):
            if balance == 0 and l_rem == 0 and r_rem == 0:
                res.add(path)
            return

        ch = expr[index]

        if ch == '(':
            dfs(index + 1, path, balance, l_rem - 1, r_rem)
            dfs(index + 1, path + ch, balance + 1, l_rem, r_rem)

        elif ch == ')':
            dfs(index + 1, path, balance, l_rem, r_rem - 1)
            dfs(index + 1, path + ch, balance - 1, l_rem, r_rem)

        else:

            dfs(index + 1, path + ch, balance, l_rem, r_rem)

    dfs(0, "", 0, left_rem, right_rem)
    return list(res)

expr = input("Enter expression: ")
result = removeInvalidParentheses(expr)
print(result)

